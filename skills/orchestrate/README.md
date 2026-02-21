# Orchestrate

2-4 specialized agents working in parallel on your task, then synthesized into one coherent answer.

## Why

Some tasks are naturally multi-faceted. "Research this API, write an integration, and test edge cases" is three jobs, not one. When you ask a single Claude session to do all three sequentially, you get a long, meandering response where the research quality drops because the model is already thinking about the code. Orchestrate splits the work across specialized agents, runs them simultaneously, and merges the results. Faster, better, and each agent stays focused on what it does well.

The restraint matters as much as the power. A simple question deserves a simple answer, not a committee. The skill works best on tasks that genuinely benefit from parallel specialization.

## How It Works

```
User: /orchestrate Analyze why our API response time doubled after the Redis migration

Step 1: Parse task keywords ── "analyze", "API", "bug"
Step 2: Select agents ──────── debugger, developer, cto
Step 3: Launch in parallel ─── 3 Task tool calls, one message
Step 4: Synthesize ─────────── Merge findings, resolve contradictions,
                               produce prioritized recommendations
```

**12 agents available, built from analysis of real usage patterns:**

| Agent | Specialization | Triggered by |
|-------|---------------|-------------|
| Researcher | Web search, 3+ sources, verification | research, find |
| Developer | Code, TypeScript/Python/React | implement, function, component |
| Debugger | Root cause analysis, systematic | bug, error, not working |
| DevOps | Deploy, CI/CD, Git, Vercel, Railway | deploy, push, git |
| Analyst | Business analysis, recommendations | analyze, evaluate, review |
| Designer | UI/UX, React, Tailwind, shadcn | design, ui, frontend |
| Writer | Content, posts, documentation | text, post, article |
| Strategist | Planning, roadmap, priorities | plan, strategy, roadmap |
| CTO | Code review, architecture, security | review, weak spots |
| Triangulator | Fact verification through 3+ sources | verify, triangulate |
| Tester | TDD, pytest, Jest, edge cases | test, validation |
| Deep Thinker | Deep analysis, contrarian view | ultrathink, deep, detailed |

Keyword mapping handles auto-selection. You can also name agents explicitly if the auto-selection picks wrong.

Agent definitions live in `agents-library.json`, which means you can add your own. Define a system prompt, typical tasks, and keyword triggers. The new agent is available to `/orchestrate` immediately.

## Quick Install

```bash
# As part of Thinking pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Thinking pack

# Just this skill:
mkdir -p ~/.claude/skills/orchestrate
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/orchestrate/SKILL.md \
  -o ~/.claude/skills/orchestrate/SKILL.md
# Also grab the agent definitions:
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/orchestrate/agents-library.json \
  -o ~/.claude/skills/orchestrate/agents-library.json
```

## Example

```
> /orchestrate Write a landing page for a developer tool that converts
  Figma designs to React components, with modern design and SEO copy

Agents selected: designer, writer, developer

--- Designer ---
Layout: hero with live demo GIF, 3 feature cards, social proof
strip, single CTA. Tailwind + shadcn. Dark mode default, toggle
available. Font: Inter. Accent: blue-500...

--- Writer ---
Headline: "Figma to React in 30 seconds. Not 30 hours."
Subhead: "Paste a Figma link. Get production-ready components..."
Feature copy: ...
SEO: title tag, meta description, OG tags...

--- Developer ---
Next.js 14 app router. Static export for speed. Components:
Hero, FeatureGrid, SocialProof, CTASection. Tailwind config
with custom theme tokens...

=== Synthesis ===

## Executive Summary
Three agents produced a complete landing page: visual design
system, conversion-focused copy, and implementation scaffold.

## Recommendations (prioritized)
1. Start with the Developer scaffold, drop in Writer copy
2. Replace placeholder GIF with actual screen recording
3. Add Lighthouse CI to catch performance regressions
4. A/B test the headline ("30 seconds" vs "one click")
```

## Part of

[Thinking Pack](../../packs/thinking/README.md) — structured decision-making tools
