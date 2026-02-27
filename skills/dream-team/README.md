# Dream Team

A dynamic expert assembly that picks 3-5 real-world thinkers tailored to your specific task, has them argue, and turns their disagreements into your plan.

## Why

Directors gives you five fixed lenses. That is perfect for evaluating what you already have. But when you are planning something new, the right experts depend on the problem. A database migration needs different minds than a go-to-market strategy. A security audit needs different minds than a design system.

Dream Team solves the selection problem. It reads your task, identifies the key uncertainties, and picks experts whose thinking styles create maximum productive friction. Then it does something Directors does not: a debate round. Experts see each other's positions and push back on the contradictions. The unresolved disagreements become your actual decision points.

The value is not in any single expert being right. The value is in the contradictions between them. Each contradiction is a decision you need to make.

## How It Works

```
User: /dream-team Redesign the auth system for multi-tenant SaaS

           ┌──────────────┐
           │  Analyze task │
           │  Select 3-5   │
           │  experts       │
           └──────┬───────┘
                  │
                  ▼
           ┌──────────────┐
           │ Show team     │◄── User approves / swaps
           └──────┬───────┘
                  │
     ┌────────────┼────────────┐────────────┐
     ▼            ▼            ▼            ▼
  Expert 1    Expert 2    Expert 3    Expert 4
  (independent perspectives, parallel)
     │            │            │            │
     └────────────┼────────────┘────────────┘
                  │
           ┌──────▼───────┐
           │ Identify 2-3  │
           │ contradictions │
           └──────┬───────┘
                  │
     ┌────────────┼────────────┐────────────┐
     ▼            ▼            ▼            ▼
  Expert 1    Expert 2    Expert 3    Expert 4
  (debate: react to contradictions, parallel)
     │            │            │            │
     └────────────┼────────────┘────────────┘
                  │
           ┌──────▼───────┐
           │  Synthesis    │
           │  Consensus    │
           │  Disagreements│
           │  Plan         │
           └──────────────┘
```

Key differences from Directors:

| | Directors | Dream Team |
|---|-----------|------------|
| **Purpose** | Evaluate what exists | Plan what to build |
| **Team** | 5 fixed experts | 3-5 dynamic, task-specific |
| **Selection** | Always the same board | Tailored to the task's uncertainties |
| **Interaction** | Independent, no debate | Independent + debate round |
| **Output** | Assessment with consensus/disagreements | Plan with explicit decision points |

## Quick Install

```bash
# As part of Thinking pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Thinking pack

# Just this skill:
mkdir -p ~/.claude/skills/dream-team
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/dream-team/SKILL.md \
  -o ~/.claude/skills/dream-team/SKILL.md
```

## Example

```
> /dream-team Design a plugin system for our CLI tool

## Dream Team for: Plugin system for CLI tool

| # | Expert | Lens | Why them |
|---|--------|------|----------|
| 1 | **Rich Hickey** | Simplicity and composability | Creator of Clojure, thinks deeply about accidental complexity |
| 2 | **Sindre Sorhus** | Developer experience | Maintains 1000+ npm packages, knows what makes APIs pleasant |
| 3 | **Linus Torvalds** | Minimalism and stability | Linux kernel module system is the canonical plugin architecture |
| 4 | **Sandi Metz** | Clean interfaces | OOP design principles that prevent plugin coupling |

Launch this team? Or swap / add someone?

> Go

## Rich Hickey — Simplicity
**My position:** Separate the plugin interface from the host...
**What I'd challenge:** "Extensibility" is not a feature. It is a design constraint...

## Sindre Sorhus — Developer Experience
**My position:** A plugin that takes more than 5 minutes to write will never get written...
**What I'd challenge:** Rich is right about simplicity, but wrong about timing...

## Linus Torvalds — Stability
**My position:** A stable ABI or you will regret it in 6 months...
**What I'd challenge:** Everyone here is overthinking the abstraction layer...

## Sandi Metz — Clean Interfaces
**My position:** Define the interface first, the implementation is a detail...

[Debate round — experts react to contradictions]

**Torvalds responds to Hickey:**
Rich, your "simple" data-only interface sounds elegant until someone needs...

**Hickey responds to Torvalds:**
Linus, a stable ABI is solving yesterday's problem. Data is the stable interface...

## Dream Team: Result

### Consensus
- Plugin interface must be data-in, data-out (no shared state)
- Documentation and examples before API design
- Version the plugin contract from day one

### Unresolved disagreements
- **Abstraction level:** Hickey wants pure data transforms; Torvalds wants a stable binary interface
  - Choose Hickey if: plugins are JS/TS and you control the ecosystem
  - Choose Torvalds if: plugins may be compiled or third-party maintained

### Plan
1. Define 3 concrete plugin use cases from real users
2. Write the plugin contract as a TypeScript interface
3. Build one internal plugin to validate the contract
4. Release with docs + example plugin before announcing the API

### First move
Interview 3 users about what they would extend.
```

## Works great with

- [Directors](../directors/) — evaluate the result after Dream Team plans it
- [Miracle Unstuck](../miracle-unstuck/) — clarify what you need before assembling the team
- [Frameworks](../frameworks/) — apply structured frameworks to the plan's decision points

## Part of

[Thinking Pack](../../packs/thinking/README.md) — structured decision-making tools
