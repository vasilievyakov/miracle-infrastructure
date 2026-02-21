---
name: orchestrate
description: "Agent orchestrator. Analyzes tasks and launches 2-4 specialized agents in parallel, then synthesizes results. Invoke via '/orchestrate task' or 'run orchestrator: task'. 12 agents built from analysis of real usage patterns."
---

# Orchestrate

Launches specialized agents in parallel for complex tasks.

## Workflow

1. **Load library** from agents-library.json (located in the same directory as this skill)
2. **Select agents** by task keywords (max 4)
3. **Launch in parallel** via Task tool
4. **Synthesize** results into a final report

---

## Task to Agent Mapping

| Keywords | Agents |
|----------|--------|
| research, find, information | `researcher`, `triangulator` |
| write code, implement, function, component | `developer`, `tester` |
| bug, error, fix, not working | `debugger`, `developer` |
| deploy, vercel, railway, push, git | `devops` |
| analyze, evaluate, review, weak spots | `analyst`, `cto` |
| design, ui, frontend, style | `designer` |
| text, post, article, documentation, readme | `writer` |
| plan, strategy, roadmap, priorities | `strategist` |
| ultrathink, deep, detailed | `ultrathink`, `analyst` |
| triangulate, verify fact, verification | `triangulator`, `researcher` |
| test, validation | `tester`, `developer` |

---

## 12 Agents

Detailed system prompts are in `agents-library.json`.

| ID | Name | Specialization |
|----|------|---------------|
| `researcher` | Deep Researcher | Web search, 3+ sources, verification |
| `developer` | Code Developer | Code, TypeScript/Python/React |
| `debugger` | Systematic Debugger | Root cause, systematic debugging |
| `devops` | DevOps Engineer | Deploy, CI/CD, Git, Vercel, Railway |
| `analyst` | Business Analyst | Business analysis, recommendations |
| `designer` | Frontend Designer | UI/UX, React, Tailwind, shadcn |
| `writer` | Content Writer | Text, posts, documentation |
| `strategist` | Product Strategist | Planning, roadmap |
| `cto` | CTO Advisor | Code review, architecture, security |
| `triangulator` | Fact Triangulator | Fact verification through 3+ sources |
| `tester` | QA Engineer | TDD, pytest, Jest, edge cases |
| `ultrathink` | Deep Thinker | Deep analysis, contrarian view |

---

## Instructions

On receiving a task with `/orchestrate`:

### Step 1: Load library

```
Read {skill_directory}/agents-library.json
```

### Step 2: Select agents

Pick 2-4 agents using the mapping above. Prefer agents with higher `priority`.

### Step 3: Launch in parallel

For each agent, launch a Task tool **simultaneously**:

```
Task tool:
- description: "{agent.name} - {brief task description}"
- subagent_type: "general-purpose"
- prompt: "{agent.system_prompt}\n\n---\n\nTASK: {user_task}\n\n---\n\nComplete the task according to your specialization.\nFormat: {agent.output_format}"
```

**CRITICAL:** All Task tool calls in ONE message for parallel execution.

### Step 4: Synthesis

After receiving all results:

1. Merge key findings
2. Resolve contradictions (flag if present)
3. Produce a structured report:
   - Executive Summary
   - Results by agent (brief)
   - Synthesized conclusions
   - Prioritized recommendations

---

## Examples

### Business analysis
```
/orchestrate Analyze the business model of company X and find weak spots
```
**Agents:** analyst, researcher, strategist, cto

### Debugging
```
/orchestrate Bug: API returns 500 on large payload
```
**Agents:** debugger, developer

### Research
```
/orchestrate Find best practices for RAG in 2026
```
**Agents:** researcher, triangulator

### Deep analysis
```
/orchestrate ultrathink: why does retention drop after onboarding
```
**Agents:** ultrathink, analyst, researcher, strategist

### Content creation
```
/orchestrate Write a landing page for an AI course with modern design
```
**Agents:** designer, writer, developer

---

## Extension

To add an agent, edit `agents-library.json`:

```json
{
  "id": "new_agent",
  "name": "Agent Name",
  "system_prompt": "...",
  "typical_tasks": ["task 1", "task 2"],
  "tools": ["Read", "Write"],
  "output_format": "structured_report"
}
```

Then add the mapping in `orchestration_rules.task_to_agents_mapping`.
