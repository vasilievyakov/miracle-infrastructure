# Miracle Unstuck

An adaptive deep interview that extracts what you actually need when you cannot articulate it, then acts on the answer.

## Why

When you are stuck, the problem is almost never "I need more information." The problem is "I cannot formulate what I need." You end up in a 20-minute back-and-forth where neither you nor the AI can pin down what the actual question is. You try option A, reject it. Try option B, reject it. Go back to A. The conversation spirals.

This skill replaces that circular conversation with a structured extraction process. 5-10 targeted questions, one at a time, each with context about why it is being asked. It diagnoses the type of stuck, adapts the questioning strategy mid-interview, and exits into concrete action: a synthesis, targeted research, or a complete reframe of the problem.

## How It Works

Five phases, and the skill can jump between them as needed:

```
Phase 0: Context Loading
  Read project dossier, past preferences, conversation history
        │
Phase 1: Diagnose the Stuck Type
  Fog? Choice Paralysis? False Dilemma? Blind Spot? Info Hunger?
        │
Phase 2: Deep Interview (5-10 questions, adaptive)
  One question at a time. Format changes based on responses.
  Can reclassify the stuck type mid-interview.
        │
Phase 3: Exit Diagnosis
  ├── Synthesis: "You already knew the answer"
  ├── Targeted Research: search filtered through your preferences
  └── Reframe: "The real question is different"
        │
Phase 4: Profile Update
  Save preference patterns for faster extraction next time
```

**Five stuck types, five interview strategies:**

| Type | Signals | Strategy |
|------|---------|----------|
| **Fog** | "I don't know what I want" | Start broad (values), narrow to concrete |
| **Choice Paralysis** | Has options, can't pick | Clarify criteria, test each option's worst case |
| **False Dilemma** | Choosing A or B, real answer is C | Challenge the framing, return to root problem |
| **Blind Spot** | Confident but something's off | Let them talk, find contradictions |
| **Info Hunger** | Knows what, not how | Quick confirm, then research |

The skill also builds a preference profile over sessions. It records your stable patterns (you consistently prefer simplicity over flexibility, you respond best to metaphors, your usual exit is reframe). The more you use it, the fewer questions it needs to reach the core.

## Quick Install

```bash
# As part of Thinking pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Thinking pack

# Just this skill:
mkdir -p ~/.claude/skills/miracle-unstuck
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/miracle-unstuck/SKILL.md \
  -o ~/.claude/skills/miracle-unstuck/SKILL.md
```

## Example

```
> /unstuck I need to pick a database for my project but I keep going
  in circles between Postgres and MongoDB

[Diagnosed: Choice Paralysis]

Question 1 of ~6:
If you could pick just one criterion to decide between them,
what would it be? Speed, flexibility of schema, ecosystem, team
familiarity, or something else?

> I guess... schema flexibility? But also I want good tooling.

Question 2 of ~6:
Two criteria: schema flexibility and tooling. If they conflict
(flexible schema but worse tooling, or rigid schema but great
tooling), which wins?

> Tooling. I don't want to fight my database.

Question 3 of ~6:
What does your data actually look like? Is it mostly relational
(users have orders have items) or mostly documents (varied
shapes, nested structures)?

> Mostly relational honestly. Some config blobs but 90% relational.

Question 4 of ~6:
Last question before I have enough. What made you consider
MongoDB in the first place? Something specific, or general
"it's popular" gravity?

> A blog post said it's better for prototyping. But now I'm not sure.

---

I noticed a pattern in your answers:
- When asked about criteria, you picked tooling over flexibility
- Your data is 90% relational
- The MongoDB consideration came from a single blog post, not
  a structural need

It looks like you already know the answer: Postgres. The blog
post created a false choice. Your data is relational, you value
tooling, and Postgres has the stronger ecosystem for both.

The 10% config blobs? JSONB column. Postgres handles that natively.

Does this resonate?
```

## Works great with

- [Memory Pack](../../packs/memory/) — when installed, the skill loads your project dossier for context, making the interview faster and more targeted
- [Directors](../directors/) — once unstuck, get the board's evaluation of your decision
- [Frameworks](../frameworks/) — apply structured decision frameworks to the choice you just clarified

## Part of

[Thinking Pack](../../packs/thinking/README.md) — structured decision-making tools
