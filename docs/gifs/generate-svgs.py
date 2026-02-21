#!/usr/bin/env python3
"""Generate SVG terminal recordings for README documentation."""

import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def make_svg(
    lines,
    title="Terminal",
    width=720,
    line_height=20,
    pad_top=48,
    pad_bottom=16,
    pad_x=16,
):
    """Create an SVG terminal window with typed command and response lines.

    Each line is a tuple: (text, color, [delay_ms])
    Colors: prompt=#89b4fa, cmd=#cdd6f4, dim=#6c7086, green=#a6e3a1,
            yellow=#f9e2af, red=#f38ba8, accent=#cba6f7, white=#cdd6f4
    """
    height = pad_top + len(lines) * line_height + pad_bottom

    text_elements = []
    for i, line in enumerate(lines):
        text = line[0]
        color = line[1] if len(line) > 1 else "#a6adc8"
        delay = line[2] if len(line) > 2 else 0
        y = pad_top + i * line_height

        # Handle mixed-color lines (prompt + command)
        if isinstance(text, list):
            spans = []
            for seg in text:
                spans.append(f'<tspan fill="{seg[1]}">{esc(seg[0])}</tspan>')
            text_elements.append(
                f"  <text x=\"{pad_x}\" y=\"{y}\" font-family=\"'SF Mono','Fira Code','Cascadia Code',monospace\" "
                f'font-size="13" fill="{color}">'
                + "".join(spans)
                + (
                    f'<animate attributeName="opacity" from="0" to="1" dur="0.3s" begin="{delay / 1000}s" fill="freeze"/>'
                    if delay
                    else ""
                )
                + "</text>"
            )
        else:
            opacity = ' opacity="0"' if delay else ""
            anim = (
                (
                    f'<animate attributeName="opacity" from="0" to="1" dur="0.3s" '
                    f'begin="{delay / 1000}s" fill="freeze"/>'
                )
                if delay
                else ""
            )
            text_elements.append(
                f"  <text x=\"{pad_x}\" y=\"{y}\" font-family=\"'SF Mono','Fira Code','Cascadia Code',monospace\" "
                f'font-size="13" fill="{color}"{opacity}>{esc(text)}{anim}</text>'
            )

    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect width="{width}" height="{height}" rx="10" fill="#1e1e2e"/>
  <rect width="{width}" height="32" rx="10" fill="#313244"/>
  <rect y="22" width="{width}" height="10" fill="#313244"/>
  <circle cx="20" cy="16" r="6" fill="#f38ba8"/>
  <circle cx="40" cy="16" r="6" fill="#f9e2af"/>
  <circle cx="60" cy="16" r="6" fill="#a6e3a1"/>
  <text x="{width // 2}" y="20" font-family="\'SF Mono\',monospace" font-size="12" fill="#6c7086" text-anchor="middle">{esc(title)}</text>
{"chr(10)".join(text_elements)}
</svg>'''


def esc(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


# -- Session Save --
session_save = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/session-save", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Detecting project... my-app (matched: keyword 'dashboard')", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("Gathering context:", "#a6adc8", 800),
        ("  git log    : 7 commits today", "#a6e3a1", 1000),
        ("  git diff   : 3 files modified", "#a6e3a1", 1100),
        ("  session    : 23 messages exchanged", "#a6e3a1", 1200),
        ("", "#1e1e2e"),
        ("Updating dossier... done", "#a6adc8", 1600),
        ("Updating observations:", "#a6adc8", 1900),
        ("  + [decision] Chose Postgres over SQLite for multi-user", "#cba6f7", 2100),
        ("  + [feature]  Added /api/users endpoint", "#89b4fa", 2300),
        ("  + [bugfix]   Fixed race condition in auth middleware", "#a6e3a1", 2500),
        ("Syncing MEMORY.md... done", "#a6adc8", 2800),
        ("", "#1e1e2e"),
        ("Session saved. 3 observations recorded.", "#a6e3a1", 3200),
    ],
    title="session-save",
    width=640,
)

# -- Search Memory --
search_memory = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/search-memory type:decision project:my-app", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Searching observations... 4 matches in my-app", "#6c7086", 400),
        ("", "#1e1e2e"),
        (
            "| #  | Date       | Type     | Summary                          |",
            "#a6adc8",
            800,
        ),
        (
            "|----|------------|----------|----------------------------------|",
            "#6c7086",
            800,
        ),
        (
            "| 12 | 2026-02-18 | decision | Chose Postgres over SQLite       |",
            "#cdd6f4",
            1000,
        ),
        (
            "| 9  | 2026-02-14 | decision | JWT tokens, 15min expiry         |",
            "#cdd6f4",
            1100,
        ),
        (
            "| 6  | 2026-02-10 | decision | React over Vue for frontend      |",
            "#cdd6f4",
            1200,
        ),
        (
            "| 3  | 2026-02-03 | decision | Monorepo with Turborepo          |",
            "#cdd6f4",
            1300,
        ),
        ("", "#1e1e2e"),
        ("Show details for which entry? (number or 'all')", "#6c7086", 1700),
    ],
    title="search-memory",
    width=640,
)

# -- Directors --
directors = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/directors AI-powered code review tool for small teams", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Launching 5 directors in parallel...", "#6c7086", 400),
        ("  Murati     evaluating...", "#f9e2af", 600),
        ("  Sutskever  evaluating...", "#f9e2af", 700),
        ("  Cherny     evaluating...", "#f9e2af", 800),
        ("  Karpathy   evaluating...", "#f9e2af", 900),
        ("  Ive        evaluating...", "#f9e2af", 1000),
        ("", "#1e1e2e"),
        ("All 5 evaluations received. Synthesizing...", "#a6e3a1", 3000),
        ("", "#1e1e2e"),
        ("## Board Verdict", "#cba6f7", 3500),
        ("", "#1e1e2e"),
        (
            "Consensus: verification loops are the moat, not AI generation",
            "#a6e3a1",
            3800,
        ),
        ("Disagreement: Sutskever vs Murati on pricing model", "#f38ba8", 4100),
        ("Top question: what happens when the model improves 10x?", "#f9e2af", 4400),
    ],
    title="directors",
    width=640,
)

# -- Orchestrate --
orchestrate = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/orchestrate Find best practices for RAG in 2026", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Selecting agents: researcher, triangulator", "#6c7086", 400),
        ("Launching 2 agents in parallel...", "#6c7086", 700),
        ("", "#1e1e2e"),
        ("  [researcher]    searching web...   12 sources found", "#89b4fa", 1200),
        ("  [triangulator]  verifying claims... 8 claims checked", "#cba6f7", 1500),
        ("", "#1e1e2e"),
        ("All agents completed. Synthesizing...", "#a6e3a1", 3000),
        ("", "#1e1e2e"),
        ("Key findings:", "#cdd6f4", 3500),
        ("  1. Hybrid search (vector + BM25) outperforms pure vector", "#a6adc8", 3700),
        ("  2. Chunk size 512-1024 tokens optimal for most use cases", "#a6adc8", 3900),
        ("  3. Re-ranking with cross-encoders adds 15-20% accuracy", "#a6adc8", 4100),
        ("", "#1e1e2e"),
        (
            "Confidence: 0.87 (3 sources agree, 1 partially contradicts)",
            "#a6e3a1",
            4500,
        ),
    ],
    title="orchestrate",
    width=640,
)

# -- Research --
research = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ('/research "Is Bun faster than Node for HTTP servers?"', "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Classifying query... comparative, technical", "#6c7086", 400),
        ("Searching 4 engines in parallel...", "#6c7086", 700),
        ("  Progress: [=========>        ] 6/11 pages", "#89b4fa", 1500),
        ("  Progress: [==================] 11/11 pages analyzed", "#a6e3a1", 3000),
        ("", "#1e1e2e"),
        ("Sources scored:", "#a6adc8", 3500),
        ("  [0.92] Official Bun benchmarks (bun.sh)", "#a6e3a1", 3700),
        ("  [0.88] TechEmpower Round 23 results", "#a6e3a1", 3800),
        ("  [0.71] Medium article with custom benchmarks", "#f9e2af", 3900),
        ("  [0.45] Reddit thread (anecdotal)", "#f38ba8", 4000),
        ("", "#1e1e2e"),
        ("Contradiction detected: official vs independent benchmarks", "#f9e2af", 4400),
        ("Generating comparison table...", "#6c7086", 4700),
    ],
    title="researching-web",
    width=640,
)

# -- Triangulate --
triangulate = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                (
                    '/triangulate "React Server Components reduce bundle size by 30%"',
                    "#cdd6f4",
                ),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Claim type: FACT (quantitative, verifiable)", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("Searching 3+ independent sources...", "#6c7086", 800),
        ("  Source 1: Next.js docs (primary)         confirms", "#a6e3a1", 1200),
        ("  Source 2: Vercel blog (same ecosystem)    confirms", "#f9e2af", 1500),
        ("  Source 3: Chrome DevRel benchmark         PARTIAL", "#f9e2af", 1800),
        ("  Source 4: Independent audit (BuilderIO)   30-40% range", "#a6e3a1", 2100),
        ("", "#1e1e2e"),
        ("Warning: echo bias (sources 1-2 share ecosystem)", "#f38ba8", 2800),
        ("", "#1e1e2e"),
        ("Verdict: PARTIAL CONFIRMATION", "#f9e2af", 3200),
        ("Confidence: 0.72", "#a6adc8", 3400),
        ("  Consensus:  +0.25  (3/4 confirm direction)", "#6c7086", 3500),
        ("  Evidence:   +0.30  (benchmarks exist)", "#6c7086", 3600),
        ("  Bias:       -0.15  (echo between sources)", "#6c7086", 3700),
        ("  Precision:  -0.08  (range is 25-40%, not exactly 30%)", "#6c7086", 3800),
    ],
    title="triangulate",
    width=680,
)

# -- Action Items --
action_items = make_svg(
    [
        (
            [("$ ", "#89b4fa"), ("/action-items meeting-notes-feb20.txt", "#cdd6f4")],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Reading file... 847 lines, 4 participants detected", "#6c7086", 400),
        ("Extracting tasks...", "#6c7086", 800),
        ("", "#1e1e2e"),
        ("## P0: Blockers", "#f38ba8", 1200),
        ("- [ ] Fix auth flow before launch  @alex  | Mon Feb 24", "#cdd6f4", 1400),
        ('      > "we cannot ship until the login redirect works"', "#6c7086", 1500),
        ("", "#1e1e2e"),
        ("## P1: Urgent", "#f9e2af", 1800),
        ("- [ ] Update API docs for v2 endpoints  @maria  | Feb 28", "#cdd6f4", 2000),
        ("- [ ] Load test the new caching layer    @alex   | Feb 26", "#cdd6f4", 2100),
        ("", "#1e1e2e"),
        ("## Unanswered Questions", "#cba6f7", 2500),
        ("- Do we need GDPR compliance for the EU launch?", "#a6adc8", 2700),
        ("- Who owns the monitoring dashboard?", "#a6adc8", 2800),
        ("", "#1e1e2e"),
        ("Found: 2 blockers, 5 urgent, 3 normal, 2 questions", "#a6e3a1", 3200),
    ],
    title="action-items",
    width=640,
)

# -- Checkup --
checkup = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/checkup --full", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Scanning ~/.claude/skills/... 15 skills found", "#6c7086", 400),
        ("", "#1e1e2e"),
        ("Phase 0 (binary):", "#a6adc8", 800),
        ("  All file references valid", "#a6e3a1", 1000),
        ("  All paths resolve", "#a6e3a1", 1100),
        ("", "#1e1e2e"),
        ("Phase 1 (structural):", "#a6adc8", 1400),
        ("  [!] frameworks: description exceeds 500 chars", "#f9e2af", 1600),
        ("  [x] old-skill: references deleted file utils.py", "#f38ba8", 1800),
        ("", "#1e1e2e"),
        ("Phase 2 (semantic):", "#a6adc8", 2200),
        ("  [~] research + triangulate: similar descriptions", "#cba6f7", 2400),
        ("  14/15 skills healthy", "#a6e3a1", 2600),
        ("", "#1e1e2e"),
        ("1 broken, 1 warning, 1 suggestion", "#f9e2af", 3000),
    ],
    title="skill-checkup",
    width=640,
)

# -- Proposal --
proposal = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                ("/proposal product.md call-transcript.txt", "#cdd6f4"),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Reading product description... done", "#6c7086", 400),
        ("Reading transcript... 2,340 lines, 47 min call", "#6c7086", 700),
        ("", "#1e1e2e"),
        ("Extracting pain points:", "#a6adc8", 1100),
        ("  Trigger:  manual reporting takes 3 days/month", "#f38ba8", 1300),
        ("  Active:   no real-time visibility into pipeline", "#f9e2af", 1500),
        ("  Latent:   team scaling will break current process", "#6c7086", 1700),
        ("", "#1e1e2e"),
        ("--- Checkpoint 1: confirm pains? (yes/edit) ---", "#cba6f7", 2200),
        ([("$ ", "#89b4fa"), ("yes", "#a6e3a1")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Mapping solutions... generating architecture...", "#6c7086", 2800),
        ("Writing proposal.md... done", "#a6e3a1", 3500),
        ("Writing architecture.md... done", "#a6e3a1", 3700),
        ("Building prototype.html... done (Tailwind, dark theme)", "#a6e3a1", 4200),
        ("", "#1e1e2e"),
        ("3 files created. Open prototype.html in browser.", "#a6e3a1", 4600),
    ],
    title="transcript-to-proposal",
    width=640,
)

# -- AQAL Review --
aqal_review = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/aqal-review", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Gathering week data...", "#6c7086", 400),
        ("  3 projects active, 28 commits, 5 sessions", "#a6adc8", 700),
        ("", "#1e1e2e"),
        ("Quadrant Assessment:", "#cdd6f4", 1100),
        ("  I  (Interior)     75  up    reflection improved", "#a6e3a1", 1300),
        ("  WE (Collective)   70  --    client call missed", "#f9e2af", 1500),
        ("  IT (Technical)    82  up    new CI pipeline", "#a6e3a1", 1700),
        ("  ITS (Systems)     68  down  staging broke twice", "#f38ba8", 1900),
        ("", "#1e1e2e"),
        ("Development Lines:", "#cdd6f4", 2300),
        ("  cognitive: 85%  technical: 78%  product: 82%", "#a6adc8", 2500),
        ("  emotional: 65%  interpersonal: 70%", "#a6adc8", 2600),
        ("", "#1e1e2e"),
        ("Week status: NORMAL (2 up, 1 stable, 1 down)", "#f9e2af", 3000),
        ("Focus next week: system stability, client follow-up", "#a6adc8", 3200),
        ("", "#1e1e2e"),
        ("Saved to ~/.claude/aqal-history.json (week 8)", "#a6e3a1", 3600),
    ],
    title="aqal-review",
    width=640,
)

# -- Memory Init --
memory_init = make_svg(
    [
        ([("$ ", "#89b4fa"), ("/memory-init", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Creating directory structure...", "#6c7086", 400),
        ("  ~/.claude/memory/              created", "#a6e3a1", 600),
        ("  ~/.claude/memory/projects/     created", "#a6e3a1", 700),
        ("  ~/.claude/memory/tests/        created", "#a6e3a1", 800),
        ("", "#1e1e2e"),
        ("Scanning for git projects...", "#6c7086", 1200),
        ("  Found: my-app       (~/projects/my-app)", "#a6adc8", 1500),
        ("  Found: landing-page (~/projects/landing-page)", "#a6adc8", 1700),
        ("  Found: api-server   (~/work/api-server)", "#a6adc8", 1900),
        ("", "#1e1e2e"),
        ("Generated:", "#a6adc8", 2300),
        ("  memory-config.json    3 projects mapped", "#a6e3a1", 2500),
        ("  MEMORY.md             index created", "#a6e3a1", 2600),
        ("  general.md            starter dossier", "#a6e3a1", 2700),
        ("", "#1e1e2e"),
        (
            "Memory system ready. Start working, /session-save when done.",
            "#a6e3a1",
            3100,
        ),
    ],
    title="memory-init",
    width=640,
)

# -- Install --
install = make_svg(
    [
        ([("$ ", "#89b4fa"), ("bash install.sh", "#cdd6f4")], "#cdd6f4"),
        ("", "#1e1e2e"),
        ("Welcome to Miracle Infrastructure", "#cdd6f4", 300),
        ("15 skills for Claude Code that solve actual problems.", "#6c7086", 300),
        ("", "#1e1e2e"),
        ("Available packs:", "#a6adc8", 600),
        ("  [1] memory       5 skills + 3 rules", "#89b4fa", 700),
        ("  [2] thinking     3 skills", "#89b4fa", 800),
        ("  [3] research     3 skills", "#89b4fa", 900),
        ("  [4] business     1 skill", "#89b4fa", 1000),
        ("  [5] content      1 skill", "#89b4fa", 1100),
        ("  [6] productivity 1 skill", "#89b4fa", 1200),
        ("  [7] meta         1 skill", "#89b4fa", 1300),
        ("  [A] All packs", "#a6e3a1", 1400),
        ("", "#1e1e2e"),
        (
            [("Select packs (e.g., 1 3 7 or A): ", "#a6adc8"), ("A", "#a6e3a1")],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Installing... 15 skills, 3 rules, templates, tests", "#6c7086", 1800),
        ("Done. Open Claude Code and try: /session-save", "#a6e3a1", 2400),
    ],
    title="install.sh",
    width=640,
)

# -- Frameworks --
frameworks = make_svg(
    [
        (
            [
                ("$ ", "#89b4fa"),
                (
                    "/frameworks My SaaS is at MVP stage, preparing for launch",
                    "#cdd6f4",
                ),
            ],
            "#cdd6f4",
        ),
        ("", "#1e1e2e"),
        ("Detecting stage... Stage 3: MVP / First Launch", "#6c7086", 400),
        ("Activating 8 frameworks:", "#a6adc8", 800),
        ("", "#1e1e2e"),
        ("  Worse is Better    ship the 80% version now", "#a6e3a1", 1000),
        ("  YAGNI              cut the admin panel, nobody asked", "#a6e3a1", 1200),
        ("  Build-Measure-     deploy, watch metrics, iterate", "#a6e3a1", 1400),
        ("  Pareto 80/20       3 features cover 80% of use cases", "#a6e3a1", 1600),
        ("  Fail Fast          add error tracking before launch", "#f9e2af", 1800),
        ("", "#1e1e2e"),
        ("Conflict detected:", "#f38ba8", 2400),
        ("  YAGNI vs Design-for-future: YAGNI wins at MVP stage", "#f9e2af", 2600),
        ("  (build flexibility into interfaces, not features)", "#6c7086", 2700),
        ("", "#1e1e2e"),
        ("Recommendations:", "#cdd6f4", 3100),
        ("  1. Remove admin panel from v1       <- YAGNI", "#a6adc8", 3300),
        ("  2. Add Sentry before launch         <- Fail Fast", "#a6adc8", 3500),
        ("  3. Ship to 10 users this week       <- BML", "#a6adc8", 3700),
    ],
    title="frameworks",
    width=640,
)


# Generate all SVGs
svgs = {
    "session-save.svg": session_save,
    "search-memory.svg": search_memory,
    "directors.svg": directors,
    "orchestrate.svg": orchestrate,
    "research.svg": research,
    "triangulate.svg": triangulate,
    "action-items.svg": action_items,
    "checkup.svg": checkup,
    "proposal.svg": proposal,
    "aqal-review.svg": aqal_review,
    "memory-init.svg": memory_init,
    "install.svg": install,
    "frameworks.svg": frameworks,
}

for name, svg in svgs.items():
    path = os.path.join(SCRIPT_DIR, name)
    with open(path, "w") as f:
        f.write(svg)
    print(f"  [ok] {name}")

print(f"\nGenerated {len(svgs)} SVGs in {SCRIPT_DIR}")
