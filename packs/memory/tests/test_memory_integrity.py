#!/usr/bin/env python3
"""
Integration tests for Miracle Infrastructure memory system integrity.
Validates consistency across all memory files (MEMORY.md, dossiers, observations).

Run: python3 ~/.claude/memory/tests/test_memory_integrity.py
"""

import json
import os
import re
import unittest

# Config-driven paths
CONFIG_PATH = os.path.expanduser("~/.claude/memory/memory-config.json")


def get_memory_path():
    """Get memory base path from config or use default."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        path = config.get("memory_path", "~/.claude/memory")
        return os.path.expanduser(path)
    return os.path.expanduser("~/.claude/memory")


def get_valid_types():
    """Get valid observation types from config or use defaults."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        return set(
            config.get(
                "observation_types",
                ["decision", "bugfix", "feature", "discovery", "problem"],
            )
        )
    return {"decision", "bugfix", "feature", "discovery", "problem"}


MEMORY_BASE = get_memory_path()
MEMORY_MD = os.path.join(MEMORY_BASE, "MEMORY.md")
PROJECTS_DIR = os.path.join(MEMORY_BASE, "projects")
VALID_OBS_TYPES = get_valid_types()


def read_file(path):
    with open(path, "r") as f:
        return f.read()


def list_dossiers():
    """List all project dossier files (*.md, not *.observations.md)."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    return [
        f
        for f in os.listdir(PROJECTS_DIR)
        if f.endswith(".md") and not f.endswith(".observations.md")
    ]


def list_observations():
    """List all observation files."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    return [f for f in os.listdir(PROJECTS_DIR) if f.endswith(".observations.md")]


class TestMemoryMdStructure(unittest.TestCase):
    """MEMORY.md has correct structure."""

    def setUp(self):
        if not os.path.exists(MEMORY_MD):
            self.skipTest("MEMORY.md not found")
        self.content = read_file(MEMORY_MD)

    def test_exists(self):
        self.assertTrue(os.path.exists(MEMORY_MD), "MEMORY.md should exist")

    def test_has_project_table(self):
        self.assertTrue(
            "| Project" in self.content or "|Project" in self.content,
            "MEMORY.md should have a project table",
        )

    def test_under_200_lines(self):
        lines = self.content.strip().split("\n")
        self.assertLessEqual(
            len(lines), 200, f"MEMORY.md is {len(lines)} lines, should be <=200"
        )

    def test_no_secrets(self):
        """No API keys, tokens, or passwords."""
        secret_patterns = [
            r"sk-[a-zA-Z0-9]{20,}",
            r"ghp_[a-zA-Z0-9]{36}",
            r"password\s*[:=]\s*\S+",
            r"api[_-]?key\s*[:=]\s*\S+",
        ]
        for pattern in secret_patterns:
            self.assertIsNone(
                re.search(pattern, self.content, re.IGNORECASE),
                f"Possible secret found matching: {pattern}",
            )


class TestProjectTableConsistency(unittest.TestCase):
    """Project table in MEMORY.md matches actual files."""

    def setUp(self):
        if not os.path.exists(MEMORY_MD):
            self.skipTest("MEMORY.md not found")
        self.content = read_file(MEMORY_MD)
        self.dossiers = list_dossiers()

    def test_all_dossiers_in_table(self):
        """Every dossier file should be referenced in MEMORY.md table."""
        for dossier in self.dossiers:
            project_name = dossier.replace(".md", "")
            self.assertIn(
                project_name,
                self.content,
                f"Dossier {dossier} not referenced in MEMORY.md",
            )

    def test_table_references_exist(self):
        """Every project referenced in table should have a dossier file."""
        pattern = r"`projects/([^`]+)\.md`"
        for match in re.finditer(pattern, self.content):
            project = match.group(1)
            dossier_file = f"{project}.md"
            self.assertIn(
                dossier_file,
                self.dossiers,
                f"MEMORY.md references {project} but {dossier_file} doesn't exist",
            )


class TestObservationCounts(unittest.TestCase):
    """Observation counts in MEMORY.md match actual files."""

    def setUp(self):
        if not os.path.exists(MEMORY_MD):
            self.skipTest("MEMORY.md not found")
        self.content = read_file(MEMORY_MD)

    def test_counts_match(self):
        """Observation counts in table should match actual Index rows."""
        pattern = r"\((\d+)\s*entr(?:y|ies)\)"
        # Also support the format: (N entries)
        for match in re.finditer(
            r"`projects/([^`]+)\.md`[^|]*\|\s*[^|]*\((\d+)\s*entr", self.content
        ):
            project = match.group(1)
            claimed_count = int(match.group(2))

            obs_path = os.path.join(PROJECTS_DIR, f"{project}.observations.md")
            if not os.path.exists(obs_path):
                self.fail(
                    f"MEMORY.md claims {claimed_count} observations for {project} "
                    f"but file doesn't exist"
                )

            obs_content = read_file(obs_path)
            actual_count = len(re.findall(r"^\| \d+", obs_content, re.MULTILINE))
            self.assertEqual(
                claimed_count,
                actual_count,
                f"Count mismatch for {project}: "
                f"MEMORY.md says {claimed_count}, actual {actual_count}",
            )


class TestDossierFormat(unittest.TestCase):
    """Each dossier has required sections."""

    REQUIRED_SECTIONS = [
        "## Status",
        "## Description",
        "## Current State",
        "## Session History",
    ]

    def test_all_dossiers_have_sections(self):
        for dossier in list_dossiers():
            content = read_file(os.path.join(PROJECTS_DIR, dossier))
            for section in self.REQUIRED_SECTIONS:
                self.assertIn(
                    section,
                    content,
                    f"{dossier} missing section: {section}",
                )

    def test_under_200_lines(self):
        for dossier in list_dossiers():
            content = read_file(os.path.join(PROJECTS_DIR, dossier))
            lines = content.strip().split("\n")
            self.assertLessEqual(
                len(lines),
                200,
                f"{dossier} is {len(lines)} lines, should be <=200",
            )


class TestObservationsFormat(unittest.TestCase):
    """Observation files have correct format."""

    def test_has_index_table(self):
        for obs_file in list_observations():
            content = read_file(os.path.join(PROJECTS_DIR, obs_file))
            self.assertIn("## Index", content, f"{obs_file} missing Index section")
            self.assertIn(
                "| # | Date | Type | Summary | Files |",
                content,
                f"{obs_file} missing Index header",
            )

    def test_has_details_section(self):
        for obs_file in list_observations():
            content = read_file(os.path.join(PROJECTS_DIR, obs_file))
            self.assertIn("## Details", content, f"{obs_file} missing Details section")

    def test_valid_types(self):
        """All observation types should be from the valid set."""
        for obs_file in list_observations():
            content = read_file(os.path.join(PROJECTS_DIR, obs_file))
            types = re.findall(r"^\| \d+ \| [\d-]+ \| (\w+) \|", content, re.MULTILINE)
            for obs_type in types:
                self.assertIn(
                    obs_type,
                    VALID_OBS_TYPES,
                    f"{obs_file} has invalid type: {obs_type}",
                )

    def test_sequential_numbers(self):
        """Observation numbers should be sequential starting from 1."""
        for obs_file in list_observations():
            content = read_file(os.path.join(PROJECTS_DIR, obs_file))
            numbers = [
                int(m) for m in re.findall(r"^\| (\d+) \|", content, re.MULTILINE)
            ]
            if not numbers:
                continue
            expected = list(range(1, len(numbers) + 1))
            self.assertEqual(
                numbers,
                expected,
                f"{obs_file} numbers not sequential: {numbers}",
            )

    def test_index_details_match(self):
        """Every Index row should have a matching Details entry."""
        for obs_file in list_observations():
            content = read_file(os.path.join(PROJECTS_DIR, obs_file))
            index_nums = re.findall(r"^\| (\d+) \|", content, re.MULTILINE)
            for num in index_nums:
                self.assertIn(
                    f"### [{num}]",
                    content,
                    f"{obs_file}: Index entry #{num} has no matching Details",
                )

    def test_details_have_context(self):
        """Details entries should have Before/After or Context fields."""
        for obs_file in list_observations():
            content = read_file(os.path.join(PROJECTS_DIR, obs_file))
            details_entries = re.findall(r"### \[(\d+)\][^\n]+", content)
            for num in details_entries:
                pattern = rf"### \[{num}\].*?(?=### \[|$)"
                block = re.search(pattern, content, re.DOTALL)
                if block:
                    block_text = block.group()
                    has_context = any(
                        kw in block_text
                        for kw in [
                            "**Before:**",
                            "**After:**",
                            "**Context:**",
                            "**Symptoms:**",
                            "**What:**",
                            "**Signal:**",
                        ]
                    )
                    self.assertTrue(
                        has_context,
                        f"{obs_file} #{num}: Details entry lacks context "
                        f"(Before/After/Context)",
                    )


class TestConfigExists(unittest.TestCase):
    """memory-config.json exists and is valid."""

    def test_config_exists(self):
        self.assertTrue(
            os.path.exists(CONFIG_PATH), f"Config not found at {CONFIG_PATH}"
        )

    def test_config_valid_json(self):
        if not os.path.exists(CONFIG_PATH):
            self.skipTest("Config not found")
        with open(CONFIG_PATH) as f:
            config = json.load(f)
        self.assertIn("memory_path", config)
        self.assertIn("projects", config)
        self.assertIn("fallback_project", config)


if __name__ == "__main__":
    unittest.main(verbosity=2)
