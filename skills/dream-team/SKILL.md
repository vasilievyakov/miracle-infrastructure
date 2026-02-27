---
name: dream-team
description: |
  Dynamic expert team assembly for planning. Selects 3-5 real-world expert personas
  tailored to the task, runs parallel analysis, facilitates a debate round on key
  contradictions, then synthesizes into a plan with explicit tradeoffs.
  Use when: (1) planning a new feature or project, (2) user says "/dream-team",
  "assemble a dream team", "pick experts for X", (3) need diverse perspectives
  before committing to an approach.
---

# Dream Team — Dynamic Expert Assembly

> **Note:** The experts are fictional personas inspired by the public work and philosophy of real individuals. They do not represent the actual views or endorsements of these people.

Dynamically assembles 3-5 real-world experts tailored to the user's task. Each expert speaks in first person in their characteristic style. After independent analysis, experts debate key contradictions. The synthesis surfaces unresolved disagreements as decision points, not smoothed-over consensus.

**Key difference from Directors:** Directors is a fixed board for **evaluating** what exists. Dream Team is a dynamic team for **planning** what to build.

## Triggers

- `/dream-team <task description>`
- `Assemble a dream team for X`
- `Pick experts for this task`
- `Who would you bring in to plan X?`
- `Dream team for X`

---

## Step 1: Analyze task and assemble team

One internal step (not a separate agent). Analyze the user's task:

1. **Task type**: technical / product / creative / strategic / operational
2. **Key uncertainties**: 3-5 questions that need answers
3. **Expert selection**: for each uncertainty, who in the world has thought deepest about this?

Selection rules:
- **3-5 experts** — count determined by number of orthogonal uncertainties
- **Real people** — concrete names, not abstract roles. "Linus Torvalds" activates a precise cognitive stance; "skeptical engineer" does not
- **Mandatory skeptic** — at least one expert who will say "don't do this" or "you're solving the wrong problem"
- **Max 2 from same domain** — diversity over depth
- **At least one unexpected pick** — someone you would not expect in this context, whose perspective expands the view
- **Explicit bias for each** — an expert without a stated bias is just another generic assistant

Present the team to the user:

```markdown
## Dream Team for: {task}

| # | Expert | Lens | Why them |
|---|--------|------|----------|
| 1 | **Name** | Area/approach | 1 sentence |
| ... | ... | ... | ... |

Launch this team? Or swap / add someone?
```

**Wait for user confirmation.** The user can:
- Approve → proceed to Step 2
- Swap an expert → adjust and show again
- Add an expert (up to 5) → add and show again

---

## Step 2: Independent perspectives (parallel)

For each expert, create a separate Task tool call, **all in one message**.

```
Task tool:
- description: "Dream Team: {name} perspective"
- subagent_type: "general-purpose"
- prompt: "{expert system_prompt}\n\n---\n\nTASK:\n{task description + context}\n\n---\n\n{instructions}"
```

### Generating expert system prompts

For each expert, generate a system prompt:

```
You are {Full Name}. You speak in first person, in your characteristic style.

Background: {2-3 sentences — key achievements and experience, public facts only}

Methodology: {3-5 bullets — known principles, approaches, beliefs of this person}

Bias: {1 sentence — what this expert overvalues or undervalues}
```

### Instructions for each expert

```
Give your perspective on this task. Speak in first person, in your characteristic style.

Response format (strict):

## {Name} — {lens in 2-3 words}

**My position:** [2-3 sentences — what to do and why]

**Main risk:** [what goes wrong with this approach]

**What I'd challenge:** [what common wisdom or obvious approach is wrong here]

**First move:** [one concrete action]

Limit: 200 words max. Be specific. Reference actual task context, not generic best practices.
```

---

## Step 3: Debate (parallel)

After receiving all perspectives, identify 2-3 key contradictions between experts.

For each expert, create a new Task tool call, **all in one message**.

```
Task tool:
- description: "Dream Team: {name} reaction"
- subagent_type: "general-purpose"
- prompt: "{expert system_prompt}\n\n---\n\nYour position:\n{their perspective from Step 2}\n\nOther positions:\n{perspectives from other experts}\n\nKey contradictions:\n{list of 2-3 contradictions}\n\n---\n\n{instructions}"
```

### Instructions for debate phase

```
You see the other experts' positions and the key contradictions.

Pick ONE contradiction where your position is strongest and respond.

Format (strict):

**{Name} responds to {opponent name}:**
[3-5 sentences. Do not agree out of politeness. If you are right, insist. If the opponent is convincing, acknowledge specifically what, but say what they are missing.]

Limit: 100 words.
```

---

## Step 4: Synthesis

After receiving all reactions, produce the final report. This is done by you (Claude), not a separate agent.

```markdown
## Dream Team: Result

### Task
{task statement}

### Team
{names and lenses, one line}

### Consensus
[Where all or most agree — this is the plan's foundation]

### Unresolved disagreements
[Contradictions NOT resolved in debate. For each:]
- **Question:** {core of the disagreement}
- **Position A ({name}):** {brief}
- **Position B ({name}):** {brief}
- **What this means for you:** {when to choose A, when to choose B}

### Plan
[Concrete sequence of steps, built on consensus. For each step: what we validate and how we know it's time for the next one]

### First move
[One concrete action right now]
```

After synthesis, offer:

> Ready to execute the plan? Or want to reassemble the team / dig into a specific disagreement?

---

## Rules

- **Step 2: all agents SIMULTANEOUSLY** in one message via Task tool
- **Step 3: all agents SIMULTANEOUSLY** in one message via Task tool
- Experts speak **in first person** in their characteristic style
- Each expert **does not know** the others in Step 2 (independence). In Step 3 **sees everyone** (debate)
- Synthesis is **not averaging** — it is a decision map: "if X matters more, do A; if Y, do B"
- Contradictions are **the main value**. Do not smooth them over. Surface them
- If all experts agree, **the selection was bad**. Add a contrasting voice
- Limits: 200 words per perspective (Step 2), 100 words per reaction (Step 3)
- If the task is tactical (a specific bug, a SQL query), **do not use Dream Team**. Say: "This task is too specific for Dream Team. Let me solve it directly."

---

## Important

- **Do NOT fabricate** specific quotes or positions these people never took. Stay within their documented philosophy and public work
- **Do NOT let experts converge** out of politeness. The model defaults to agreement; the prompt must counteract this
- **Be specific.** Generic wisdom is noise. Concrete advice grounded in the actual task is signal
- **Keep limits strict.** 200 words per expert, 100 words per reaction. Discipline creates clarity
