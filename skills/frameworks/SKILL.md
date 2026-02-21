---
name: frameworks
description: |
  Library of 50 engineering, product, design, and thinking frameworks organized by project stage.
  Determines stage, activates the right set, delivers specific recommendations with conflict resolution.
  Use when: (1) user says "/frameworks", "run through frameworks", "which principles apply here",
  (2) evaluating a project against engineering best practices, (3) need structured analysis by project stage.
---

# Frameworks: Project Stage Framework Library

Determines the project stage, activates the relevant framework set, applies each one **specifically** to the project, explicitly surfaces conflicts and their resolution.

Works with any project type: AI product, service, course, content, business model, text, design, architecture, code, presentation.

## Triggers

- `/frameworks <project description>`
- `Run [X] through frameworks`
- `Which frameworks apply to [X]?`
- `Evaluate [X] at stage [stage]`
- `Which principles apply here?`
- `Check [X] against DRY / KISS / SOLID / JTBD / ...` (specific framework)
- `What stage are we at and what should we do?`

## Workflow

### Step 1: Determine stage

From context or user indication. If unclear, ask.

| # | Stage | What happens |
|---|-------|-------------|
| 1 | **Ideation / Problem Framing** | Formulating the problem, finding leverage, defining audience |
| 2 | **Architecture / Design** | Choosing stack, designing structure, component boundaries |
| 3 | **MVP / First Launch** | Building the first working version, shipping |
| 4 | **Iteration / Growth** | Feedback, iterations, expanding functionality |
| 5 | **Polish / Scale** | Refinement, scaling, retention, love |
| 6 | **Safety / Consequence Audit** | Assessing consequences before scaling, sensitive data |

### Step 2: Activate stage frameworks

**Do not dump all 50.** Only the ones relevant to the current stage.

#### Stage 1: Ideation / Problem Framing
First Principles, JTBD, Inversion, Chesterton's Fence, Second-Order Thinking, Gall's Law, Occam's Razor.

#### Stage 2: Architecture / Design
Software 1.0/2.0/3.0, Separation of Concerns, KISS, Conway's Law, CAP, 12-Factor, POLA, Composition over Inheritance, Event-Driven Architecture.

#### Stage 3: MVP / First Launch
Worse is Better, YAGNI, Build-Measure-Learn, Pareto, Fail Fast, Convention over Configuration, Reversible Decisions, Verification > Generation.

#### Stage 4: Iteration / Growth
RICE, North Star Metric, Kano Model, Evals-Driven Development, HITL, Autonomy Slider, Context Engineering, SOLID, DRY, Strategic Patience + Tactical Impatience.

#### Stage 5: Polish / Scale
Dieter Rams' 10 Principles, Affordance, Progressive Disclosure, Jakob's Law, MLP, Lindy Effect, Hick's Law, Miller's Law, Principle of Least Surprise.

#### Stage 6: Safety / Consequence Audit
Second-Order Thinking, Inversion, POLA, HITL, Principle of Least Surprise, Jagged Intelligence.

### Step 3: Apply each framework SPECIFICALLY

**Not** "use KISS". **Instead**: "here is what specifically to remove / simplify / change".
**Not** "JTBD". **Instead**: "here is the job the user hires this product to do".

Each active framework = a specific observation about the project + an action.

### Step 4: Check for conflicts

If two active frameworks give opposite recommendations, surface the conflict explicitly and apply the resolution rule (see "Conflict Points" section).

### Step 5: Deliver recommendations

Prioritized action list. Each action is tied to a framework.

---

## Framework Catalog

### Category A: "Remove the unnecessary"
Cut to the essence, remove everything that does not carry value.

| Framework | Core idea |
|-----------|-----------|
| **DRY** | Every piece of knowledge has a single representation |
| **KISS** | Simplest solution that works |
| **YAGNI** | Do not build what is not needed now |
| **Occam's Razor** | All else equal, the simplest explanation |
| **Dieter Rams' 10 Principles** | Innovative, useful, aesthetic, understandable, unobtrusive, honest, long-lasting, thorough, environmentally friendly, as little design as possible |
| **Progressive Disclosure** | Reveal complexity gradually |
| **Hick's Law** | More options = longer decision time |
| **Miller's Law** | 7 plus or minus 2 items in working memory |

### Category B: "Structure correctly"
Right boundaries between system parts.

| Framework | Core idea |
|-----------|-----------|
| **SOLID** | Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion |
| **Separation of Concerns** | Each module handles one thing |
| **Unix Philosophy** | Do one thing well, combine through pipes |
| **Composition over Inheritance** | Build from parts instead of deep hierarchies |
| **12-Factor App** | Config, dependencies, statelessness for SaaS |
| **Conway's Law** | Architecture mirrors organization structure |
| **POLA** | Minimum privileges for a component |
| **CAP Theorem** | Consistency, availability, partition tolerance: pick two |
| **Event-Driven Architecture** | Components communicate through events |
| **Convention over Configuration** | Sensible defaults over endless settings |

### Category C: "Move smart"
Right priorities and speed.

| Framework | Core idea |
|-----------|-----------|
| **Build-Measure-Learn** | Fast cycle: hypothesis, experiment, data |
| **JTBD** | People "hire" a product for a specific job |
| **RICE** | Reach, Impact, Confidence, Effort for prioritization |
| **North Star Metric** | Single metric defining success |
| **Pareto (80/20)** | 20% effort yields 80% results |
| **Kano Model** | Must-have, performance, delighters |
| **MLP** | Minimum Lovable Product |
| **Double Diamond** | Discover, define, develop, deliver |
| **Reversible vs Irreversible Decisions** | Type 1 vs Type 2 doors. Reversible ones: go fast |
| **Fail Fast** | Errors surface as early as possible |
| **Strategic Patience, Tactical Impatience** | Long-term vision, daily urgency |

### Category D: "Think deeper"
Do not fool yourself, dig to the truth.

| Framework | Core idea |
|-----------|-----------|
| **First Principles** | Break down to basic truths, reassemble |
| **Inversion** | "How to guarantee failure?" and avoid that |
| **Second-Order Thinking** | What is the consequence of the consequence? |
| **Chesterton's Fence** | Do not remove a fence until you understand why it was put there |
| **Lindy Effect** | Survived long = will survive equally long |
| **Gall's Law** | Working complex systems evolve from working simple systems |
| **Worse is Better** | Simple, slightly incorrect implementation beats complex correct one |
| **Principle of Least Surprise** | System behaves as user expects |
| **Affordance** | Object suggests how to use it |
| **Jakob's Law** | Users expect products to work like other products |

### Category E: "AI-specific"
Frameworks for the AI era.

| Framework | Core idea |
|-----------|-----------|
| **Software 1.0 / 2.0 / 3.0** | Explicit code, trained models, prompts. Each layer subsumes the previous |
| **Autonomy Slider** | User chooses AI autonomy level |
| **Jagged Intelligence** | LLMs are brilliant and stupid simultaneously, unpredictably |
| **Anterograde Amnesia** | LLMs do not consolidate knowledge between sessions |
| **HITL** | Human in the loop for decisions |
| **Evals-Driven Development** | Development through evaluation sets |
| **Context Engineering** | Designing what enters the context window |
| **Prompt, Plan, Execute, Verify** | AI agent work cycle |
| **Verification > Generation** | Feedback loop matters more than generation |
| **Design for the model 6 months from now** | Design for future AI capabilities |

---

## Conflict Points Between Frameworks

When a conflict is detected, surface it explicitly and apply the rule:

| Conflict | Resolution |
|----------|-----------|
| **YAGNI** vs **Design for model 6mo from now** | YAGNI for features (do not add "just in case"), future-proofing for interfaces (build flexibility into foundations) |
| **Worse is Better** vs **Dieter Rams / MLP** | Worse is Better at MVP/Launch, Rams/MLP at Polish/Scale |
| **KISS** vs **SOLID** | KISS by default, SOLID when team > 3 or codebase crosses complexity threshold |
| **Convention over Config** vs **Autonomy Slider** | Convention for builders (sensible defaults), Autonomy Slider for end users (control) |
| **Build-Measure-Learn** vs **Research-first** | BML for product-market fit, research-first for foundational capabilities and safety-critical work |
| **Fail Fast** vs **Safety-first** | Fail Fast for technical errors (bugs, API), Safety First for impact on people (data, privacy, bias) |

---

## Output Format

```markdown
## Frameworks: [project/feature name]
### Stage: [N] - [stage name]

### Active Frameworks

**Category [X]: "[name]"**
- **[Framework]:** [specific application to this project]
- **[Framework]:** [specific application]

**Category [Y]: "[name]"**
- **[Framework]:** [specific application]

### Framework Conflicts
[If any: nature of the divergence, which resolution rule, why]

### Recommendations (prioritized)
1. [action] <- [framework]
2. [action] <- [framework]
3. [action] <- [framework]
```

---

## Principles

1. **Frameworks are tools, not dogma.** Project context beats framework. Note this explicitly.
2. **Specificity is mandatory.** No abstract "apply KISS". Only specific observations and actions.
3. **Stage is the routing key.** Some frameworks give opposite recommendations at different stages. Stage resolves.
4. **Not all frameworks are active.** Each stage has its own set. Do not dump all 50.
5. **Conflicts are surfaced explicitly.** Show the divergence + apply the resolution rule.

---

## Special invocation modes

**Specific framework:** "Check against JTBD" applies JTBD + shows related relevant frameworks.

**No stage specified:** Claude determines stage from project context.

**Multiple stages:** If the project spans stages (part in MVP, part already in Growth), activate frameworks for both stages and note this.
