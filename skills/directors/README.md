# Directors

A virtual advisory board of five expert directors who evaluate your project in parallel, then synthesize where they agree and where they fight.

## Why

You are about to make a decision that matters. You could think about it from your own angle. Or you could get five genuinely different perspectives simultaneously, each filtering the same problem through a distinct lens. The value is not in any single director being "right." The value is in the disagreements. The director who catches the blind spot rotates unpredictably, which is exactly why you run all five.

One LLM, five system prompts, five different conclusions. Mixture-of-experts through prompting.

## How It Works

Five directors launch as parallel agents, each with a detailed system prompt encoding their philosophy and evaluation style:

```
User: /directors My SaaS app for restaurant inventory management

          ┌─────────┐
          │  Input   │
          └────┬─────┘
               │
    ┌──────────┼──────────┐──────────┐──────────┐
    ▼          ▼          ▼          ▼          ▼
 Murati    Sutskever   Cherny    Karpathy     Ive
 Product   Science     DX/Eng    AI Arch     Design
    │          │          │          │          │
    └──────────┼──────────┘──────────┘──────────┘
               ▼
        ┌─────────────┐
        │  Synthesis   │
        │  Consensus   │
        │  Conflicts   │
        │  Questions   │
        └─────────────┘
```

| Director | Lens |
|----------|------|
| **Mira Murati** | Product vision, rapid iteration, collaborative AI, ethics |
| **Ilya Sutskever** | First principles, generalization, long-term horizon |
| **Boris Cherny** | Developer experience, verification loops, institutional memory |
| **Andrej Karpathy** | 1.0/2.0/3.0 stack, verifiability, agent-friendly architecture |
| **Jony Ive** | Care, emotional resonance, simplicity, material integrity |

Each director evaluates everything: product, architecture, engineering, UX, safety, scaling, business. Through their lens. The synthesis then shows consensus (strong signal) and disagreements (where the interesting problems hide).

You can also summon individual directors: `Run Murati on X` or call a subset: `Call Cherny and Karpathy`.

## Quick Install

```bash
# As part of Thinking pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Thinking pack

# Just this skill:
mkdir -p ~/.claude/skills/directors
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/directors/SKILL.md \
  -o ~/.claude/skills/directors/SKILL.md
```

## Example

```
> /directors JWT-based auth system for a multi-tenant B2B platform

## Mira Murati: Product and Leadership
Bottom line: Ship with JWT but design the token refresh as a
collaborative flow where admins can see and revoke sessions.
Strengths: Fast path to MVP, widely understood...
Concerns: Tenant isolation in shared token stores...

## Ilya Sutskever: Scientific Strategy
Bottom line: The real question is not JWT vs sessions. It is
whether your auth model generalizes across tenant boundaries.
...

## Boris Cherny: Engineering and DX
Bottom line: JWT is fine. The DX concern is token refresh.
Design the verification loop first, the token format second.
...

## Andrej Karpathy: Architecture and Paradigms
Bottom line: Auth is a 1.0 problem masquerading as complex.
Keep it in explicit code. Do not over-engineer.
...

## Jony Ive: Design and Experience
Bottom line: The login experience communicates trust.
If the auth feels clunky, the product feels untrustworthy.
...

## Board Verdict
### Consensus
- JWT is appropriate for this stage
- Token refresh UX needs explicit design attention

### Disagreements
- Sutskever wants generalized multi-tenant model now; Karpathy says keep it simple
- Ive prioritizes login feel; Cherny prioritizes developer verification flow

### Top 3 Critical Questions
1. How do you handle tenant isolation in the token store?
2. What happens when a token is compromised across tenants?
3. Have you designed the admin revocation experience?
```

## Part of

[Thinking Pack](../../packs/thinking/README.md) — structured decision-making tools
