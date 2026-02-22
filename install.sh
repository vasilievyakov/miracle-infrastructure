#!/usr/bin/env bash
set -euo pipefail

# Miracle Infrastructure Installer
# Copies selected skill packs to ~/.claude/skills/ and ~/.claude/rules/

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"
RULES_DIR="$HOME/.claude/rules"
MEMORY_DIR="$HOME/.claude/memory"
BACKUP_SUFFIX=".backup.$(date +%Y%m%d%H%M%S)"

# Colors (if terminal supports them)
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    BOLD='\033[1m'
    NC='\033[0m'
else
    GREEN='' YELLOW='' BLUE='' BOLD='' NC=''
fi

echo ""
echo -e "${BOLD}Welcome to Miracle Infrastructure${NC}"
echo "17 skills for Claude Code that solve actual problems."
echo ""
echo "Available packs:"
echo ""
echo -e "  ${BLUE}[1]${NC} memory       - Session memory system (5 skills + 3 rules + templates)"
echo -e "  ${BLUE}[2]${NC} thinking     - Decision-making tools (4 skills)"
echo -e "  ${BLUE}[3]${NC} research     - Research and verification (3 skills)"
echo -e "  ${BLUE}[4]${NC} business     - Business workflows (1 skill)"
echo -e "  ${BLUE}[5]${NC} content      - Content processing (1 skill)"
echo -e "  ${BLUE}[6]${NC} productivity - Personal productivity (1 skill)"
echo -e "  ${BLUE}[7]${NC} meta         - Tooling & security (2 skills)"
echo -e "  ${BLUE}[A]${NC} All packs"
echo ""
read -rp "Select packs to install (e.g., 1 3 7 or A for all): " SELECTION

# Parse selection
INSTALL_MEMORY=false
INSTALL_THINKING=false
INSTALL_RESEARCH=false
INSTALL_BUSINESS=false
INSTALL_CONTENT=false
INSTALL_PRODUCTIVITY=false
INSTALL_META=false

if [[ "$SELECTION" =~ [Aa] ]]; then
    INSTALL_MEMORY=true
    INSTALL_THINKING=true
    INSTALL_RESEARCH=true
    INSTALL_BUSINESS=true
    INSTALL_CONTENT=true
    INSTALL_PRODUCTIVITY=true
    INSTALL_META=true
else
    for num in $SELECTION; do
        case $num in
            1) INSTALL_MEMORY=true ;;
            2) INSTALL_THINKING=true ;;
            3) INSTALL_RESEARCH=true ;;
            4) INSTALL_BUSINESS=true ;;
            5) INSTALL_CONTENT=true ;;
            6) INSTALL_PRODUCTIVITY=true ;;
            7) INSTALL_META=true ;;
            *) echo -e "${YELLOW}Unknown option: $num (skipping)${NC}" ;;
        esac
    done
fi

# Ensure base directories exist
mkdir -p "$SKILLS_DIR"
mkdir -p "$RULES_DIR"

installed_skills=0
installed_rules=0

# Helper: install a skill directory
install_skill() {
    local pack="$1"
    local skill="$2"
    local src="$SCRIPT_DIR/skills/$skill"
    local dst="$SKILLS_DIR/$skill"

    if [ ! -d "$src" ]; then
        echo -e "  ${YELLOW}[skip]${NC} $skill (source not found)"
        return
    fi

    if [ -d "$dst" ]; then
        # Back up existing
        cp -r "$dst" "${dst}${BACKUP_SUFFIX}"
    fi

    mkdir -p "$dst"
    cp "$src/SKILL.md" "$dst/SKILL.md"

    # Copy supporting files (like agents-library.json) if they exist
    for f in "$src"/*.json "$src"/*.py "$src"/*.md; do
        [ -f "$f" ] || continue
        local fname
        fname="$(basename "$f")"
        [ "$fname" = "SKILL.md" ] && continue
        cp "$f" "$dst/$fname"
    done

    # Copy subdirectories (like references/) if they exist
    for d in "$src"/*/; do
        [ -d "$d" ] || continue
        local dname
        dname="$(basename "$d")"
        mkdir -p "$dst/$dname"
        cp -r "$d"* "$dst/$dname/" 2>/dev/null || true
    done

    echo -e "  ${GREEN}[ok]${NC} $skill"
    installed_skills=$((installed_skills + 1))
}

# Helper: install a rule file
install_rule() {
    local src="$1"
    local name
    name="$(basename "$src")"
    local dst="$RULES_DIR/$name"

    if [ -f "$dst" ]; then
        cp "$dst" "${dst}${BACKUP_SUFFIX}"
    fi

    cp "$src" "$dst"
    echo -e "  ${GREEN}[ok]${NC} $name"
    installed_rules=$((installed_rules + 1))
}

echo ""
echo -e "${BOLD}Installing...${NC}"
echo ""

# Memory pack
if [ "$INSTALL_MEMORY" = true ]; then
    echo -e "${BLUE}Memory pack:${NC}"
    install_skill "memory" "session-save"
    install_skill "memory" "search-memory"
    install_skill "memory" "memory-health"
    install_skill "memory" "memory-init"
    install_skill "memory" "project-status"

    echo ""
    echo -e "${BLUE}Memory rules:${NC}"
    install_rule "$SCRIPT_DIR/packs/memory/rules/session-start.md"
    install_rule "$SCRIPT_DIR/packs/memory/rules/session-end.md"
    install_rule "$SCRIPT_DIR/packs/memory/rules/auto-observe.md"

    # Set up memory directory structure
    echo ""
    echo -e "${BLUE}Memory structure:${NC}"
    mkdir -p "$MEMORY_DIR/projects"
    mkdir -p "$MEMORY_DIR/tests"

    if [ ! -f "$MEMORY_DIR/memory-config.json" ]; then
        cp "$SCRIPT_DIR/packs/memory/templates/memory-config.json" "$MEMORY_DIR/memory-config.json"
        echo -e "  ${GREEN}[ok]${NC} memory-config.json"
    else
        echo -e "  ${YELLOW}[exists]${NC} memory-config.json (kept existing)"
    fi

    if [ ! -f "$MEMORY_DIR/MEMORY.md" ]; then
        cp "$SCRIPT_DIR/packs/memory/templates/MEMORY.md" "$MEMORY_DIR/MEMORY.md"
        echo -e "  ${GREEN}[ok]${NC} MEMORY.md"
    else
        echo -e "  ${YELLOW}[exists]${NC} MEMORY.md (kept existing)"
    fi

    if [ ! -f "$MEMORY_DIR/projects/general.md" ]; then
        cat > "$MEMORY_DIR/projects/general.md" <<'DOSSIER'
# General

## Status
Permanent. Catch-all for sessions not tied to a specific project.

## Description
Default dossier for miscellaneous work: infrastructure setup, research, experiments, one-off tasks.

## Current State
- Last session: (not yet)
- Done: Memory system initialized
- Uncommitted: no

## Unresolved Problems
(none)

## Decisions Made
- Memory system initialized with Miracle Infrastructure

## Next Steps
1. Add projects to memory-config.json
2. Start using /session-save at end of work sessions

## Session History
- Memory system initialized
DOSSIER
        echo -e "  ${GREEN}[ok]${NC} general.md (starter dossier)"
    else
        echo -e "  ${YELLOW}[exists]${NC} general.md (kept existing)"
    fi

    if [ ! -f "$MEMORY_DIR/projects/general.observations.md" ]; then
        cat > "$MEMORY_DIR/projects/general.observations.md" <<'OBS'
# Observations - general

## Index
| # | Date | Type | Summary | Files |
|---|------|------|---------|-------|

## Details
OBS
        echo -e "  ${GREEN}[ok]${NC} general.observations.md"
    else
        echo -e "  ${YELLOW}[exists]${NC} general.observations.md (kept existing)"
    fi

    cp "$SCRIPT_DIR/packs/memory/tests/test_memory_integrity.py" "$MEMORY_DIR/tests/test_memory_integrity.py"
    echo -e "  ${GREEN}[ok]${NC} test_memory_integrity.py"
    echo ""
fi

# Thinking pack
if [ "$INSTALL_THINKING" = true ]; then
    echo -e "${BLUE}Thinking pack:${NC}"
    install_skill "thinking" "directors"
    install_skill "thinking" "frameworks"
    install_skill "thinking" "orchestrate"
    install_skill "thinking" "miracle-unstuck"
    echo ""
fi

# Research pack
if [ "$INSTALL_RESEARCH" = true ]; then
    echo -e "${BLUE}Research pack:${NC}"
    install_skill "research" "researching-web"
    install_skill "research" "triangulate"
    install_skill "research" "learned-lessons"
    echo ""
fi

# Business pack
if [ "$INSTALL_BUSINESS" = true ]; then
    echo -e "${BLUE}Business pack:${NC}"
    install_skill "business" "transcript-to-proposal"
    echo ""
fi

# Content pack
if [ "$INSTALL_CONTENT" = true ]; then
    echo -e "${BLUE}Content pack:${NC}"
    install_skill "content" "action-items"
    echo ""
fi

# Productivity pack
if [ "$INSTALL_PRODUCTIVITY" = true ]; then
    echo -e "${BLUE}Productivity pack:${NC}"
    install_skill "productivity" "aqal-review"
    echo ""
fi

# Meta pack
if [ "$INSTALL_META" = true ]; then
    echo -e "${BLUE}Meta pack:${NC}"
    install_skill "meta" "skill-checkup"
    install_skill "meta" "miracle-security"
    echo ""
fi

# Summary
echo -e "${BOLD}Done.${NC}"
echo ""
echo "  Skills installed: $installed_skills"
echo "  Rules installed:  $installed_rules"
echo ""

if [ "$INSTALL_MEMORY" = true ]; then
    echo "Memory system ready at: $MEMORY_DIR"
    echo "  Run /memory-init in Claude Code to auto-detect your projects."
    echo "  Or edit $MEMORY_DIR/memory-config.json manually."
    echo ""
fi

echo "Open Claude Code and try: /session-save, /directors, /research"
echo ""
echo "Existing files were backed up with suffix: $BACKUP_SUFFIX"
echo ""
