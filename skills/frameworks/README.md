# Frameworks

50 engineering, product, design, and thinking frameworks organized by project stage, with built-in conflict resolution for when they disagree with each other.

## Why

Frameworks are useful when applied at the right time. YAGNI is gospel during an MVP. It is sabotage during a scaling phase. The hard part was never knowing that KISS exists. The hard part is knowing which frameworks matter right now, applying them to your specific situation with concrete actions, and resolving the contradictions when two frameworks point in opposite directions.

This skill handles all three. It detects your project stage, activates only the relevant frameworks, applies each one specifically (not "use KISS" but "remove the settings panel, it serves 2% of users"), and surfaces conflicts with resolution rules.

## How It Works

```
User: /frameworks My AI writing assistant

Step 1: Detect stage ─────── MVP / First Launch
Step 2: Activate frameworks ─ YAGNI, Worse is Better, Build-Measure-Learn,
                              Pareto, Fail Fast, Verification > Generation, ...
Step 3: Apply specifically ── "YAGNI: remove the 'custom tone' feature,
                              ship with 3 preset tones first"
Step 4: Check conflicts ───── YAGNI vs Future-proofing?
                              Resolution: YAGNI for features,
                              future-proof the API interface
Step 5: Deliver priorities ── Ordered action list, each tied to a framework
```

**6 stages, 50 frameworks, 5 categories:**

| Category | Focus | Examples |
|----------|-------|---------|
| A: Remove the unnecessary | Cut to the essence | DRY, KISS, YAGNI, Occam's Razor, Hick's Law |
| B: Structure correctly | Right boundaries | SOLID, Separation of Concerns, Conway's Law, CAP |
| C: Move smart | Right priorities | JTBD, RICE, North Star Metric, Pareto, Fail Fast |
| D: Think deeper | Don't fool yourself | First Principles, Inversion, Chesterton's Fence |
| E: AI-specific | Frameworks for the AI era | Software 1.0/2.0/3.0, Jagged Intelligence, HITL |

**Built-in conflict resolution:**

| Conflict | Resolution |
|----------|------------|
| YAGNI vs Future-proofing | YAGNI for features, future-proof interfaces |
| KISS vs SOLID | KISS solo, SOLID when team > 3 |
| Worse is Better vs Quality | Worse is Better at MVP, Quality at Polish |
| Fail Fast vs Safety-first | Fail Fast for tech errors, Safety for people impact |

## Quick Install

```bash
# As part of Thinking pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Thinking pack

# Just this skill:
mkdir -p ~/.claude/skills/frameworks
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/frameworks/SKILL.md \
  -o ~/.claude/skills/frameworks/SKILL.md
```

## Example

```
> /frameworks Online course platform, just launched beta

## Frameworks: Online Course Platform
### Stage: [3] - MVP / First Launch

### Active Frameworks

**Category A: "Remove the unnecessary"**
- **YAGNI:** Drop the certificate generator. Nobody has finished
  a course yet. Build it when someone actually completes one.
- **Hick's Law:** Landing page has 6 CTAs. Pick one. "Start free lesson."

**Category C: "Move smart"**
- **Build-Measure-Learn:** You have 40 beta users and no analytics.
  Add Mixpanel before adding features. You are flying blind.
- **Pareto:** 3 of your 12 lessons drive 80% of completions.
  Double down on what works, shelve the rest.

**Category E: "AI-specific"**
- **Verification > Generation:** Your AI quiz generator has
  no answer verification. Students will find the first wrong
  answer in week one. Add a self-check loop.

### Framework Conflicts
- **YAGNI vs Design for model 6mo from now:** Your AI quiz API
  currently returns plain text. YAGNI says that is fine. But in
  6 months, models will return structured JSON natively. Resolution:
  keep plain text in the UI, but wrap the API response in a parser
  interface you can swap later. 5 minutes of work, saves a rewrite.

### Recommendations (prioritized)
1. Add analytics before any new feature <- Build-Measure-Learn
2. Cut landing page to single CTA <- Hick's Law
3. Add quiz answer verification loop <- Verification > Generation
4. Wrap AI API response in parser interface <- Future-proofing
5. Remove certificate generator from roadmap <- YAGNI
```

## Part of

[Thinking Pack](../../packs/thinking/README.md) — structured decision-making tools
