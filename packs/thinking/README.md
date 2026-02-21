# Thinking Pack

Five virtual experts argue about your project so you don't have to.

## What it does

You have a decision to make. You could think about it yourself, or you could launch 5 AI agents in parallel, each channeling a different expert perspective, and get a synthesized report with consensus, disagreements, and concrete recommendations.

The thinking pack gives Claude Code structured decision-making tools that go beyond "just think harder".

## What is included

### Skills (3)

| Skill | Command | What it does |
|-------|---------|-------------|
| **directors** | `/directors` | 5-director virtual advisory board, each evaluating through a unique lens |
| **frameworks** | `/frameworks` | 50 frameworks organized by project stage, with conflict resolution |
| **orchestrate** | `/orchestrate` | 2-4 specialized agents working in parallel on complex tasks |

### Supporting files

| File | Purpose |
|------|---------|
| `agents-library.json` | 12 agent definitions with system prompts and specializations |

## Directors

Five expert lenses evaluate your project simultaneously:

| Director | Lens |
|----------|------|
| **Mira Murati** | Product, rapid iteration, collaborative AI, ethics |
| **Ilya Sutskever** | First principles, generalization, long-term horizon |
| **Boris Cherny** | DX, verification loops, parallelization, institutional memory |
| **Andrej Karpathy** | 1.0/2.0/3.0 stack, verifiability, agent-friendly architecture |
| **Jony Ive** | Care, emotional resonance, simplicity, material integrity |

Each director evaluates EVERYTHING (product, engineering, UX, business, safety) through their unique perspective. The synthesis shows where they agree (strong signal) and where they disagree (attention needed).

## Frameworks

50 frameworks across 5 categories, activated by project stage:

| Stage | Frameworks activated |
|-------|---------------------|
| Ideation | First Principles, JTBD, Inversion, Chesterton's Fence, ... |
| Architecture | KISS, SOLID, Conway's Law, 12-Factor, ... |
| MVP | YAGNI, Worse is Better, Build-Measure-Learn, Pareto, ... |
| Growth | RICE, North Star, Kano, Autonomy Slider, ... |
| Polish | Dieter Rams, Progressive Disclosure, Jakob's Law, ... |
| Safety | Second-Order Thinking, POLA, Jagged Intelligence, ... |

The skill determines the project stage, applies only relevant frameworks, and explicitly surfaces conflicts between them (e.g., YAGNI vs future-proofing).

## Orchestrate

12 specialized agents that can be deployed in parallel:

| Agent | Specialization |
|-------|---------------|
| Researcher | Web search, 3+ sources |
| Developer | Code, TypeScript/Python/React |
| Debugger | Root cause analysis |
| DevOps | Deploy, CI/CD |
| Analyst | Business analysis |
| Designer | UI/UX |
| Writer | Content, documentation |
| Strategist | Planning, roadmap |
| CTO | Code review, security |
| Triangulator | Fact verification |
| Tester | TDD, edge cases |
| Deep Thinker | Contrarian analysis |

The orchestrator reads the task, selects 2-4 agents, launches them simultaneously, and synthesizes results.

## Extension points

- **Add directors**: Follow the system prompt pattern in the skill file
- **Add frameworks**: Add to any category, assign to stages
- **Add agents**: Edit `agents-library.json`, add the keyword mapping
