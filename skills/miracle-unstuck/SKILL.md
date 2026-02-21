---
name: miracle-unstuck
description: |
  Adaptive deep interview that extracts what you need but can't articulate, then acts on it.
  Use when: (1) User is stuck and can't formulate what they want, (2) User says "I don't know",
  (3) User gives contradictory requirements, (4) User keeps changing direction, (5) Brainstorm feels unfocused.
  Triggers: "/unstuck", "I'm stuck", "I don't know what to do", "I can't decide", "help me figure this out",
  "I can't formulate what I need".
---

# Miracle Unstuck

When someone is stuck, the problem is rarely a lack of information. It is the inability to articulate what they actually need. This skill first extracts hidden preferences through an adaptive interview, then acts: synthesizes an answer, runs targeted research, or reframes the problem entirely.

---

## Phase 0: Context Loading

Before the first question, understand who you are talking to and what they are working on.

### Project

If the work is tied to a project:
1. Read the project dossier from the memory directory
2. Read observations for the project
3. Determine project stage (new, active, mature, troubled)

### Preference Profile

Read the user's `unstuck-profile.md` from the memory directory (if it exists).
This file contains accumulated preference patterns from past sessions.

### Current Conversation

Analyze context before the skill was invoked:
- What was being discussed?
- Where exactly did the difficulty arise?
- What options were already considered and rejected?

**Phase result:** internal map: {project, stage, decision history, stuck point, known preferences}

---

## Phase 1: Diagnose the Type of Stuck

Based on context, identify the situation type. This determines the interview strategy.

| Type | Signals | Interview Strategy |
|------|---------|-------------------|
| **Fog** | "I don't know what I want", no clear criteria | Start with broad questions about values and feelings, gradually narrow |
| **Choice Paralysis** | Has 2+ options, can't choose | Help clarify selection criteria, then evaluate options |
| **False Dilemma** | Choosing between A and B, real answer is C | Challenge the framing, suggest a reframe |
| **Blind Spot** | Confident in direction, something doesn't add up | Ask clarifying questions, look for contradictions |
| **Information Hunger** | Knows what they want, doesn't know how | Quickly confirm "what", then move to research |

**The type can be reclassified** during the interview. If by question 3 you realize it's not "fog" but "choice paralysis", adapt.

---

## Phase 2: Deep Interview (5-10 questions)

### Principles

1. **One question at a time.** Never ask two questions in one message.
2. **Every question with context.** Explain why you are asking and what depends on the answer.
3. **Adaptive format.** Choose the question format based on the situation:

| Format | When to use |
|--------|------------|
| **Options with explanations** | When you can offer concrete choices, each with consequences |
| **Open question** | When you need to hear how the person formulates it themselves |
| **Metaphor/analogy** | When logic hasn't formed yet, images might help |
| **Provocative statement** | When you need to trigger a reaction: "What if this isn't needed at all?" |
| **Narrowing question** | When you need to shrink the option space: "Definitely not X?" |
| **Mirror** | Repeat what you heard in your own words. Often the person says "no, not like that, more like this" |

4. **After every answer, assess:**
   - Is there enough information to act? If yes, move to Phase 3.
   - What type of next question will be most productive?
   - Does the stuck type need reclassification?

5. **Don't interrogate.** If you see fatigue (short answers, repeated "I don't know"), offer a pause or move to action with what you have.

### Strategies by Stuck Type

**Fog:**
```
Q1-2: Broad, values-based ("What matters more here: speed or quality?")
Q3-4: About feelings ("Imagine it's done. What feels good? What doesn't?")
Q5-6: Narrowing ("Definitely not option A? If you could only pick one?")
Q7+: Concretizing ("OK, if X, what's the first step?")
```

**Choice Paralysis:**
```
Q1: "What options are on the table?" (if not clear from context)
Q2: "If you could pick just one criterion to decide, which would it be?"
Q3-4: Test each option: "If you pick X, what's the worst that happens?"
Q5: "Is there an option you definitely DON'T want?" (elimination)
Q6+: Converge to recommendation
```

**False Dilemma:**
```
Q1: Mirror: "Am I right that the choice is between A and B?"
Q2: "What if neither A nor B? What would you want ideally?"
Q3: "What problem are you solving with this choice?" (return to root)
Q4+: Propose alternative frames
```

**Blind Spot:**
```
Q1-2: "Tell me how you see it" (let them talk)
Q3: Provocation: "What about [contradiction]?"
Q4: "Who else will use / see / depend on this?"
Q5+: Clarify the discovered gap
```

**Information Hunger:**
```
Q1-2: Quickly confirm "what" (2-3 key parameters)
Q3: "What have you already tried / looked at?"
-> Move to research after 3-4 questions
```

### Question Number

Show progress: **"Question 3 of ~7"** (approximate, because adaptive).

---

## Phase 3: Exit Diagnosis

After the interview, determine which exit mode provides the most value.

### Mode: Synthesis ("You already know")

**When:** answers were confident and consistent, the person just couldn't assemble them into a whole.

**Action:**
```
I noticed a pattern in your answers:
- When asked about X, you chose Y
- When asked about A, you said B
- When I asked about C, you answered D without hesitation

It looks like what you actually want is: {synthesis in 2-3 sentences}.

Does this resonate? Or am I missing something?
```

### Mode: Targeted Research

**When:** direction is clear, external data is needed to make the decision.

**Action:**
1. Formulate a specific search query based on the interview
2. Show the user: "Here's what I'll search for: {query}. Is that right?"
3. Run the search (see Phase 4: Research)
4. Present results filtered through the user's preference lens

### Mode: Reframe ("Different question")

**When:** the interview revealed that the real problem differs from the stated one.

**Action:**
```
You came with the question: "{original question}"

Based on our conversation, the real task is different:
- {What actually concerns you}
- {Why the original framing was imprecise}

I suggest reframing:
"{new problem statement}"

Is this closer to the truth?
```

---

## Phase 4: Research (if needed)

### Search Strategy

1. **Formulate the query** based on the interview, not generic, but specific to the discovered preferences
2. **Run 2-3 searches in parallel** from different angles (if multiple search tools are available)
3. **Filter results** through the user's preference lens:
   - Exclude what contradicts discovered preferences
   - Prioritize what aligns with patterns from the profile
4. **Synthesize** in a format matching the situation:
   - If "choice paralysis": comparison table
   - If "information hunger": step-by-step guide
   - If "fog": map of possibilities with a recommendation

### Presenting Results

```
===========================================
   RESEARCH: "{what was searched}"
===========================================

Searched with your preferences in mind:
- {preference 1 from interview}
- {preference 2 from interview}

## Findings

{results, filtered and ranked}

## Recommendation

Based on what I learned about you + search data:
{concrete recommendation}

## Sources
{links}
===========================================
```

---

## Phase 5: Profile Update

After every unstuck session, update the preference profile.

**File:** `unstuck-profile.md` in the project memory directory.

### Profile Structure

```markdown
# Unstuck Profile: Preference Patterns

## Last updated: {date}

## Stable Patterns
| Domain | Pattern | Confidence | Examples |
|--------|---------|-----------|----------|
| Architecture | Prefers simplicity over flexibility | High (3 sessions) | JWT vs sessions, monolith vs micro |
| UX | Minimalism, fewer steps | Medium (2 sessions) | Registration form, navigation |

## Meta-patterns
- Stuck type: most often {type} ({N} of {M} sessions)
- Responds best to: {question format}
- Usual exit path: {synthesis / research / reframe}

## Session History
| Date | Topic | Stuck Type | Exit | Outcome |
|------|-------|-----------|------|---------|
```

### Update Rules

- Add a new row to "Session History"
- If a pattern repeated 2+ times, add it to "Stable Patterns"
- If a pattern was disproven, lower confidence or remove it
- Do not record one-off preferences, only stable ones

---

## Auto-detect: When to Suggest /unstuck

If the skill was not invoked explicitly, watch for signals of being stuck in the conversation:

### Strong Signals (suggest immediately)
- User says "I don't know", "I can't decide", "I'm stuck" 2+ times
- User changes direction 3+ times in a row
- User rejects all proposed options

### Weak Signals (suggest gently, once)
- Short uncertain answers
- Long pauses between messages
- Phrases like "well, maybe...", "not sure..."

### Suggestion Format
```
Looks like we're going in circles. Want to try /unstuck?
It's a deep interview mode. I'll ask you 5-10 questions
to figure out what you actually need, then find a solution.
```

**Suggest at most once per conversation.** If declined, don't insist.

---

## Anti-patterns (what NOT to do)

- **Don't propose a solution before the interview.** Even if it's "obvious", understand the person first.
- **Don't ask questions for the sake of asking.** If after 3 questions the picture is clear, move to action.
- **Don't turn it into an interrogation.** Maximum 10 questions. If that's not enough, you have the wrong questions.
- **Don't ignore "I don't know".** "I don't know" is a valuable signal. Don't repeat the question, try a different format.
- **Don't force your recommendation.** Synthesize, don't decide for the person.
