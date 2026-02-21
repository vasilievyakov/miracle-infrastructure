<h1 align="center">Miracle Infrastructure</h1>

<p align="center">
  <em>15 skills that give Claude Code a memory, opinions, and a research department.<br>Zero dependencies. Just Markdown.</em>
</p>

<p align="center">
  <a href="https://github.com/vasilievyakov/miracle-infrastructure/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="License: MIT" />
  </a>
  <img src="https://img.shields.io/badge/Skills-15-8A2BE2?style=flat-square" alt="15 Skills" />
  <img src="https://img.shields.io/badge/Packs-7-orange?style=flat-square" alt="7 Packs" />
  <img src="https://img.shields.io/badge/Dependencies-0-brightgreen?style=flat-square" alt="Zero Dependencies" />
  <img src="https://img.shields.io/badge/Sessions_Tested-1169+-informational?style=flat-square" alt="1169+ Sessions" />
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/vasilievyakov/miracle-infrastructure?style=flat-square&label=Stars" alt="GitHub Stars" />
  <img src="https://img.shields.io/github/forks/vasilievyakov/miracle-infrastructure?style=flat-square&label=Forks" alt="GitHub Forks" />
  <img src="https://img.shields.io/github/last-commit/vasilievyakov/miracle-infrastructure?style=flat-square&label=Last%20Commit" alt="Last Commit" />
</p>

---

## The Problem

Claude Code forgets everything between sessions.

You explain your project architecture on Monday. By Tuesday it asks what framework you use. You make a decision about JWT vs sessions on Wednesday. On Thursday, it proposes sessions again. You fix a race condition in token refresh. Next week, the same pattern shows up and nobody remembers the fix.

Without external memory, your agent re-derives conclusions you already settled. It proposes solutions you already rejected. It debates options you already chose between. Every session starts at zero.

Miracle Infrastructure fixes that. Fifteen skills, seven packs, zero dependencies. Your agent remembers decisions, argues with itself before committing to architecture, verifies claims through multiple sources, and builds proposals from call transcripts.

All of it is Markdown files. No servers. No databases. No Docker containers pretending to be simple.

## Install

```bash
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh
```

<p align="center">
  <img src="docs/gifs/install.svg" alt="Installation" width="640" />
</p>

> [!TIP]
> The installer shows an interactive menu. Pick individual packs or install everything. Existing files are backed up before overwriting. Safe to re-run.

**2 minutes. Zero dependencies.** No Docker, no database, no MCP server, no npm. Just Markdown and bash.

---

## Contents

- [What 1,169 Sessions Actually Taught Us](#what-1169-sessions-actually-taught-us)
  - [The Philosophy](#the-philosophy)
  - [Hard-Won Lessons](#hard-won-lessons)
  - [What Actually Gets Used](#what-actually-gets-used)
  - [The Dead Ends](#the-dead-ends)
  - [Why Markdown and Not a Database](#why-markdown-and-not-a-database)
- [Packs](#packs)
  - [Memory](#memory) -- session persistence, typed observations
  - [Thinking](#thinking) -- directors, frameworks, agent orchestrator
  - [Research](#research) -- web research, triangulation, knowledge base
  - [Business](#business) -- transcript to proposal + prototype
  - [Content](#content) -- extract action items from text
  - [Productivity](#productivity) -- weekly integral review
  - [Meta](#meta) -- skills library health audit
- [How It Compares](#how-it-compares)
- [For AI Researchers](#for-ai-researchers)
- [Architecture](#for-the-curious)
- [Background](#background)
- [License](#license)

---

## What 1,169 Sessions Actually Taught Us

This section exists because every tool's README promises the moon. Here is what we learned across 1,169 sessions and 10 projects over 6 months of daily use. Including the parts where we were wrong.

### The Philosophy

**Workshop + Nervous System.** Not Iron Man's suit. We explicitly rejected the "AI superpower" metaphor after months of actual use.

A workshop: tools in their places, each one purpose-built, and you know which one to grab without thinking. A nervous system: agents as extensions of your thinking, capturing observations, loading context, prompting you to save what matters.

The system is proactive. Rules make the agent act without being asked. Skills give it tools when asked. `auto-observe` captures decisions as they happen. `session-start` loads context before you request it. `session-end` reminds you to save. You stop managing the agent and start working *with* it.

**Agents are precision instruments.** Not general-purpose cannons. Sometimes you need automatic transmission, sometimes manual. Sometimes the handbrake, sometimes the brake pedal. Sometimes cruise control, sometimes you need to stop and think. Stack should be a function of the task you are solving, not what you already have.

```mermaid
graph LR
    T[Your task] --> Q{What do you need?}
    Q -->|Remember| M["/session-save\n/search-memory"]
    Q -->|Decide| D["/directors\n/frameworks"]
    Q -->|Verify| R["/research\n/triangulate"]
    Q -->|Execute| O["/orchestrate\n2-4 agents"]
    Q -->|Extract| A["/action-items\n/proposal"]

    style T fill:#1e1e2e,stroke:#cba6f7,color:#cdd6f4
    style Q fill:#1e1e2e,stroke:#89b4fa,color:#cdd6f4
    style M fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
    style D fill:#1e1e2e,stroke:#f9e2af,color:#f9e2af
    style R fill:#1e1e2e,stroke:#89b4fa,color:#89b4fa
    style O fill:#1e1e2e,stroke:#cba6f7,color:#cba6f7
    style A fill:#1e1e2e,stroke:#f38ba8,color:#f38ba8
```

### Hard-Won Lessons

<p align="center">
  <img src="docs/gifs/insight-structure.svg" alt="Lesson 1: Structure beats Freedom" width="640" />
</p>

**Structure beats freedom.** This was counterintuitive. We expected that giving the agent more freedom would produce more creative output. The opposite happened. Constraints produce better results. Typed observations, mandatory Before/After fields, resolution tracking for problems. The structure is what makes data useful six months later. Without it, you get a pile of notes that nobody (human or AI) can navigate.

**Shorter prompts beat longer prompts.** We tried writing exhaustive system prompts that covered every edge case. They performed worse than concise, precise instructions. The model handles ambiguity well. It handles walls of text less well.

**Agent proactivity is the underrated superpower.** The combination of rules and skills creates an agent that acts before you ask. `session-start` loads your project context automatically. `auto-observe` captures decisions in the moment. `session-end` prompts you to save. This saves more time than any individual skill, because it eliminates the overhead of remembering to manage your own tooling.

<p align="center">
  <img src="docs/gifs/insight-bottleneck.svg" alt="Lesson 2: The Operator is the Bottleneck" width="640" />
</p>

**The operator is the bottleneck.** The system does not creak. The operator does. The human with limited context, limited attention, limited working memory. That is the constraint. The system's job is to compensate for *your* limitations, not the model's.

**When to make a skill vs. when to just prompt.** Principles come first: repetition, workflow complexity. Then intuition through practice. When you start, you try to over-control everything. When you get good at it, you develop a feel for what will be useful and what will not. Apply, reflect, and when you have a good understanding of your infrastructure, start trusting it.

### What Actually Gets Used

<p align="center">
  <img src="docs/gifs/insight-memory.svg" alt="Why memory matters" width="640" />
</p>

`/session-save` runs at the end of roughly 70% of sessions. The other 30% are quick questions that do not produce anything worth remembering.

`auto-observe` captures 1 to 3 observations per session automatically. You do not invoke it. It watches for decisions, bugfixes, discoveries, and problems, then appends them to the project's observation log. The most valuable observation types turned out to be **decisions** and **discoveries**. These are knowledge types impossible to reconstruct from code alone. "Why we chose A over B" and "API actually limits 100 req/min." Things that evaporate unless written down in the moment.

`/search-memory` gets used 2 to 3 times per week. The typical query is something like "what did we decide about auth?" The memory system prevented the same JWT-vs-sessions debate from happening 4 times. Four times the agent would have proposed a solution that had already been evaluated and rejected. External declarative memory prevents re-derivation of previously settled conclusions. That alone justified building all of this.

`/directors` gets called for any project above $5k or any architectural decision. Five virtual experts arguing is cheaper than one real regret.

`/frameworks` when starting a new project phase. It picks the relevant subset of 50 frameworks based on your stage. Not all 50 at once. That would be insane.

`/orchestrate` for tasks that need parallel research and implementation. Researcher finds the information, Developer writes the code, Tester validates it. Simultaneously.

`/research` and `/triangulate` for any claim that sounds too good. Trust, then verify. Or just verify.

### The Dead Ends

Honesty about failures. These cost real time and real tokens to discover.

<p align="center">
  <img src="docs/gifs/insight-precision.svg" alt="Lesson 3: Precision, Not Power" width="640" />
</p>

**Long prompts worked worse than short ones.** Mentioned above, worth repeating. We invested serious effort into comprehensive system prompts that anticipated every scenario. The result was worse output. The model gets confused by instruction overload the same way a person does.

**Universal "do everything" skills do not work.** We tried building a single skill that handled research, analysis, and recommendations. Specialization wins. Every time. A `/research` skill and a `/triangulate` skill outperform a single `/research-and-verify` skill.

**Adding all possible skills without deliberation produces noise.** More tools does not mean more capability. It means more context consumed, more busywork, more tokens burned on irrelevant processing. "Agents are precision instruments for jeweler's tasks. When you unleash all agents at once, you get work for work's sake and tokens burned inefficiently."

**Mass agent launches are wasteful.** Five directors evaluating your grocery list is a waste. The car metaphor applies here: you do not floor the accelerator in a parking lot.

### Why Markdown and Not a Database

Zero dependencies. Works offline. Version-controllable. Readable by humans.

```mermaid
graph LR
    subgraph "Vector DB approach"
        V1[Your code] --> V2[MCP Server] --> V3[Qdrant/Pinecone] --> V4[Docker]
        V4 --> V5["maintenance<br/>debugging<br/>migrations"]
    end

    subgraph "This approach"
        M1[Your code] --> M2["Markdown files<br/>in ~/.claude/"]
        M2 --> M3["done."]
    end

    style V1 fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
    style V2 fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
    style V3 fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
    style V4 fill:#1e1e2e,stroke:#f38ba8,color:#cdd6f4
    style V5 fill:#1e1e2e,stroke:#f38ba8,color:#f38ba8
    style M1 fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style M2 fill:#1e1e2e,stroke:#a6e3a1,color:#cdd6f4
    style M3 fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
```

A SQLite database would be faster to query. A vector store would have better semantic search. Both would require installation steps, maintenance, and debugging when they break. Markdown files in a git repo require nothing. They survive OS upgrades, editor changes, and the inevitable migration to the next AI tool.

The non-dogmatic take: "One does not interfere with the other. There are no right tools and wrong tools. Only timely usage and excessive usage." If your project genuinely needs a vector store, use one. A big mistake is trying to use nothing and thinking you are smarter than everyone. Stack should match the task.

### Design Principles

**Progressive disclosure.** Only load what is needed.

```mermaid
graph TD
    A["MEMORY.md<br/><b>~200 tokens</b><br/>every session"] -->|project mentioned| B["project.md<br/><b>~800 tokens</b><br/>on demand"]
    B -->|search query| C["observations Index<br/><b>~40 tokens/row</b><br/>scan titles only"]
    C -->|match found| D["observations Details<br/><b>~150 tokens/row</b><br/>full context"]

    style A fill:#1e1e2e,stroke:#a6e3a1,color:#a6e3a1
    style B fill:#1e1e2e,stroke:#89b4fa,color:#89b4fa
    style C fill:#1e1e2e,stroke:#f9e2af,color:#f9e2af
    style D fill:#1e1e2e,stroke:#f38ba8,color:#f38ba8
```

100 observations across 10 projects: a search costs ~4,000 tokens. Without progressive disclosure: ~15,000 tokens. The difference compounds across sessions.

**The system is opinionated.** Observations have types (decision, bugfix, feature, discovery, problem). History is append-only. Problems track resolution status. You can extend the types, you cannot remove the structure. Constraints make the data useful six months later.

**Design for the model 6 months from now.** The interfaces are stable. The capabilities will improve. A skill that produces good results with today's model will produce better results with tomorrow's model, because the structure is right. Do not optimize for current limitations. Optimize for the contract.

---

## Packs

| | Pack | Skills | What it does |
|:---:|------|--------|-------------|
| :brain: | **[Memory](#memory)** | 5 skills + 3 rules | Your agent remembers yesterday, last week, and that bug from three months ago |
| :bulb: | **[Thinking](#thinking)** | 3 skills | Five virtual experts argue about your project so you don't have to |
| :mag: | **[Research](#research)** | 3 skills | Web research with confidence scores, fact verification, knowledge base |
| :briefcase: | **[Business](#business)** | 1 skill | Call transcript to proposal + architecture + clickable prototype |
| :clipboard: | **[Content](#content)** | 1 skill | Extract tasks from transcripts, chats, documents |
| :bar_chart: | **[Productivity](#productivity)** | 1 skill | Weekly integral review across 4 dimensions |
| :wrench: | **[Meta](#meta)** | 1 skill | Skills library health audit |

---

### Memory

Your agent remembers what happened yesterday. And last week. And that bug you fixed three months ago that is about to happen again.

> Prevented the same JWT-vs-sessions debate from happening 4 times. The agent kept proposing a solution that had already been evaluated and rejected. With memory, settled conclusions stay settled.

**Skills:** `session-save` `search-memory` `memory-health` `memory-init` `project-status`
**Rules:** `session-start` `session-end` `auto-observe`

<p align="center">
  <img src="docs/gifs/session-save.svg" alt="Session Save" width="640" />
</p>

How it works:

```mermaid
graph LR
    A[Session Start] --> B[Load dossier\nfrom memory]
    B --> C[Work]
    C --> D[Session End]
    C -.-> E[Capture events\ntyped observations]
    D --> F[Prompt\n/session-save]
```

The memory hierarchy uses progressive disclosure to stay token-efficient:

```
MEMORY.md (always loaded, ~200 tokens)
    |
    +-- project.md (on project mention, ~800 tokens)
    |
    +-- project.observations.md
        +-- Index (~40 tokens/row)
        +-- Details (~150 tokens/row, loaded only for matches)
```

With 100 observations across 10 projects, a search costs ~4,000 tokens instead of ~15,000. Your context window says thank you.

> [!NOTE]
> Start with `/memory-init` after installation. It auto-detects your projects and sets up the directory structure.

[Full documentation &#8594;](packs/memory/README.md)

---

### Thinking

Five virtual experts argue about your project. Each one sees everything through their unique lens: product, engineering, UX, business, safety.

> They frequently disagree. No single "best" director. The one who catches what others miss changes every time. The value is in the ensemble, not any single expert.

**Skills:** `directors` `frameworks` `orchestrate`

<p align="center">
  <img src="docs/gifs/directors.svg" alt="Directors Board" width="640" />
</p>

<details>
<summary><strong>Directors</strong> -- 5 agents evaluate your project in parallel</summary>

| Director | Lens |
|----------|------|
| **Mira Murati** | Product, rapid iteration, collaborative AI |
| **Ilya Sutskever** | First principles, generalization, long-term |
| **Boris Cherny** | DX, verification loops, institutional memory |
| **Andrej Karpathy** | 1.0/2.0/3.0 stack, verifiability, agent-friendly |
| **Jony Ive** | Care, emotional resonance, simplicity |

Produces a synthesis with consensus, disagreements, top 3 critical questions, and action items.

</details>

<details>
<summary><strong>Frameworks</strong> -- 50 frameworks, activated by project stage</summary>

Determines your project stage (ideation, architecture, MVP, growth, polish, safety), activates the relevant subset of 50 frameworks, applies each one specifically, and surfaces conflicts with resolution rules.

Not all 50 at once. That would be insane.

</details>

<details>
<summary><strong>Orchestrate</strong> -- 2-4 agents in parallel</summary>

Picks from a library of 12 specialized agents based on task keywords. Researcher + Triangulator for fact-finding. Developer + Tester for implementation. Debugger + Developer for fixing things.

Runs them in parallel, synthesizes results into a single report.

</details>

[Full documentation &#8594;](packs/thinking/README.md)

---

### Research

Your agent checks its homework.

**Skills:** `researching-web` `triangulate` `learned-lessons`

<p align="center">
  <img src="docs/gifs/research.svg" alt="Research" width="640" />
</p>

**Research** does web search with source scoring, contradiction detection, and confidence breakdown.

**Triangulate** verifies claims through 3+ independent sources. Classifies each claim as fact, opinion, or prediction. Shows exactly where the confidence comes from.

**Learned Lessons** keeps a knowledge base of solved problems. After you debug something with web search, it offers to record the solution. Next time a similar problem shows up, it checks the knowledge base first. Your agent stops googling the same error twice.

[Full documentation &#8594;](packs/research/README.md)

---

### Business

From "we had a call" to "here is the proposal, architecture, and clickable prototype."

> "We often look through our own focus and miss what the client is really trying to say. LLMs understand language patterns well enough to catch what you missed." The clickable prototype built with the client's own data and own words leaves an unforgettable impression. Used dozens of times. If you understand your client, you know what to sell to solve their specific problem.

**Skill:** `transcript-to-proposal`

<p align="center">
  <img src="docs/gifs/proposal.svg" alt="Transcript to Proposal" width="640" />
</p>

Give it a product description and a call transcript. It extracts pains, maps them to features, generates a proposal using the client's own words, builds system architecture, and creates an interactive HTML prototype. With checkpoints so you review before it continues.

[Full documentation &#8594;](packs/business/README.md)

---

### Content

Nobody reads meeting transcripts twice. This skill reads them once and extracts everything actionable.

**Skill:** `action-items`

<p align="center">
  <img src="docs/gifs/action-items.svg" alt="Action Items" width="640" />
</p>

Handles .txt transcripts, chat exports (JSON/HTML), PDFs, raw text. Produces a prioritized checklist with assignees, deadlines, and source quotes.

[Full documentation &#8594;](packs/content/README.md)

---

### Productivity

A weekly review that looks at more than your commit count.

**Skill:** `aqal-review`

<p align="center">
  <img src="docs/gifs/aqal-review.svg" alt="AQAL Review" width="640" />
</p>

Uses the AQAL integral model to evaluate progress across 4 quadrants (interior/exterior, individual/collective) and 5 development lines. Tracks trends over weeks. Tells you when you are shipping features at the cost of team health, or growing personally while the codebase rots.

[Full documentation &#8594;](packs/productivity/README.md)

---

### Meta

Your skills library has a doctor.

**Skill:** `skill-checkup`

<p align="center">
  <img src="docs/gifs/checkup.svg" alt="Skill Checkup" width="640" />
</p>

Validates file references, frontmatter, trigger uniqueness, and dependency drift. Reports problems. Does not auto-fix. A calm doctor, not a helicopter parent.

[Full documentation &#8594;](packs/meta/README.md)

---

## How It Compares

Different approaches, not competitors. "There are no right tools and wrong tools. Only timely usage and excessive usage."

| Feature | Miracle Infrastructure | memory-bank | claudemem |
|---------|:---------------------:|:-----------:|:---------:|
| Zero dependencies | :white_check_mark: | :x: MCP | :x: MCP |
| Setup under 2 min | :white_check_mark: | :x: | :white_check_mark: |
| Token efficient | :white_check_mark: Progressive disclosure | :x: | :x: |
| Typed observations | :white_check_mark: 5 types + custom | :x: | :x: |
| Self-validating | :white_check_mark: Integrity tests | :x: | :x: |
| Decision making | :white_check_mark: Directors + Frameworks | :x: | :x: |
| Research tools | :white_check_mark: 3 skills | :x: | :x: |
| Works offline | :white_check_mark: | :x: | :x: |

Each of these tools made a deliberate set of tradeoffs. MCP-based systems get tighter integration with external services. Database-backed systems get faster queries at scale. We chose zero dependencies and Markdown because we value portability, readability, and not debugging infrastructure when we should be debugging code. Your situation might call for something different.

> [!IMPORTANT]
> This comparison reflects our understanding of these tools as of February 2026. Features may have changed. If you maintain one of these projects and something is inaccurate, please open an issue.

---

## For AI Researchers

If you work on agentic systems, memory architectures, or human-AI interaction, several findings from 1,169 sessions may be worth your attention.

<p align="center">
  <img src="docs/gifs/insight-research.svg" alt="Research Concept Mapping" width="640" />
</p>

**Progressive disclosure as manual RAG without a vector store.** The memory hierarchy (MEMORY.md > project dossiers > observation indices > observation details) implements retrieval-augmented generation through file structure alone. Token cost scales with query specificity, not corpus size. No embeddings, no similarity search, no infrastructure. The tradeoff is obvious: it requires human-designed structure. The benefit is equally obvious: zero failure modes from retrieval errors.

**auto-observe as episodic memory.** The observation system captures typed episodic memories (decision, bugfix, feature, discovery, problem) with mandatory context fields (Before/After, Why). This creates a structured episodic memory that an LLM can query through pattern matching on the index. The most valuable observation types were decisions and discoveries, both of which are impossible to reconstruct from code artifacts alone.

**Mixture-of-experts through prompting.** The Directors system runs one LLM through 5 different system prompts (product, engineering, UX, business, safety lenses). They frequently disagree. Genuinely. No single director consistently outperforms the others. The one who catches what others miss changes every time. This suggests that system prompt variation creates meaningful diversity in reasoning, analogous to mixture-of-experts architectures, without requiring separate models or fine-tuning.

**Constraints improve output quality.** Across 1,169 sessions, structured and constrained prompts consistently outperformed open-ended ones. Shorter prompts outperformed longer prompts. This parallels findings in instruction tuning: specificity and structure in the prompt matter more than exhaustive coverage.

**External declarative memory prevents re-derivation.** Without persistent memory, the agent re-derives conclusions from first principles each session. It proposes solutions already rejected, re-evaluates tradeoffs already settled. External declarative memory (project dossiers with recorded decisions) eliminates this re-derivation, functioning as a persistent belief store that survives context window boundaries.

**The human is the bottleneck.** After 6 months of daily use, the consistent finding is that system performance is limited by the human operator, not the model. The human's context window is smaller, attention is less reliable, and working memory is more fragile. The system's most impactful features are the ones that compensate for human limitations: auto-loading context, auto-capturing decisions, prompting to save state.

---

## For the Curious

<details>
<summary><strong>How progressive disclosure saves tokens</strong></summary>

| What loads | When | Cost |
|-----------|------|------|
| MEMORY.md | Every session | ~200 tokens |
| project.md | On project mention | ~800 tokens |
| observations Index | On search | ~40 tokens/row |
| observations Details | Only for matches | ~150 tokens/row |

100 observations, searching by type: ~4,000 tokens loaded. Without progressive disclosure: ~15,000 tokens. The difference compounds across sessions.

</details>

<details>
<summary><strong>Extension points</strong></summary>

- **Add observation types**: edit `memory-config.json`
- **Add directors**: follow the system prompt pattern in `directors/SKILL.md`
- **Add frameworks**: add to any category, assign to stages
- **Add agents**: edit `agents-library.json`
- **Custom dossier sections**: add any `## Section` to a dossier file

[Full extension guide &#8594;](docs/customization.md)

</details>

<details>
<summary><strong>System architecture</strong></summary>

[See ARCHITECTURE.md for full system diagrams](ARCHITECTURE.md), including:
- Session lifecycle diagram
- Memory hierarchy with token costs
- Data flow between components
- File structure reference

</details>

---

## Background

It started simply: a solo developer got tired of re-explaining his own codebase to his own AI agent. Every Monday morning, same questions. Every architectural decision, re-debated. Every bugfix, forgotten by the next session.

Over 6 months and 1,169 sessions across 10 projects, that frustration became a philosophy about human-AI symbiosis. Not the "AI does everything" version. Not the "AI is just autocomplete" version. The version where a human with a workshop full of the right tools and an agent that extends their thinking can produce work that neither could alone.

The tools grew one at a time, each one solving a specific friction. Memory came first (stop re-explaining). Directors came next (stop making architectural decisions alone at 2am). Research followed (stop trusting the agent's confident-sounding hallucinations). Business skills last (stop losing client insights between the call and the proposal).

Every skill that survived earned its place through repeated use. The ones that did not make the cut, the universal "do everything" skill, the exhaustive system prompts, the mass agent launches, taught us something equally valuable: agents are precision instruments for jeweler's tasks, not sledgehammers.

The name "Miracle Infrastructure" comes from the original project name. The miracle is that it works with zero dependencies.

## License

MIT. Do whatever you want with it.

<p align="center">
  <a href="https://github.com/vasilievyakov/miracle-infrastructure">
    <img src="https://img.shields.io/badge/Get_Started-bash_install.sh-4F46E5?style=for-the-badge" alt="Get Started" />
  </a>
</p>
