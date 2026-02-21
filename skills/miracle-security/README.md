# miracle-security

Two security audits in one skill. Code review scans for vulnerabilities with five parallel agents. Enterprise assessment evaluates your product through the eyes of a CISO.

## Why

You ask Claude to "look at this from a security perspective" and get a different answer every time. Sometimes it catches the SQL injection. Sometimes it misses the hardcoded API key staring at it from line 42. The problem is not capability. The problem is that a single pass through an entire codebase with no structure produces inconsistent results.

This skill runs five specialized agents simultaneously, each looking for a specific class of vulnerability. What one agent misses, another catches. When three agents independently flag the same issue, that's a strong signal. When only one does, it might be a false positive. The convergence pattern is the real value.

The enterprise assessment mode flips the lens: instead of "what's broken in the code," it asks "would a CISO let this product into their organization?" Four agents evaluate data handling, access control, compliance readiness, and operational resilience, producing a maturity scorecard that maps directly to deal sizes.

## How It Works

### Mode 1: Code Review (`/security review`)

Five agents launch in parallel, each scanning the codebase through a different security lens:

```
User: /security review

          ┌─────────┐
          │  Detect  │
          │  Stack   │
          └────┬─────┘
               │
          ┌────┴─────┐
          │  Threat   │
          │  Model    │
          └────┬─────┘
               │
    ┌──────┬───┼───┬──────┐
    ▼      ▼   ▼   ▼      ▼
 Inject  Auth  Sec  Deps  Logic
 Hunter  Audit Scan Check Anlyz
    │      │   │   │      │
    └──────┴───┼───┴──────┘
               ▼
        ┌─────────────┐
        │  Calibrate   │
        │  Deduplicate │
        │  Synthesize  │
        └─────────────┘
```

| Agent | Focus | What it catches |
|-------|-------|-----------------|
| **injection-hunter** | Injection & XSS | SQL/NoSQL/command injection, SSTI, XSS, SSRF, path traversal |
| **auth-auditor** | Auth & Access | Missing auth, IDOR, privilege escalation, JWT issues, CSRF |
| **secrets-scanner** | Secrets & Config | Hardcoded keys/tokens, debug mode, permissive CORS, unsafe cookies |
| **dependency-checker** | Dependencies | Missing lock files, eval/exec/pickle, prototype pollution |
| **logic-analyzer** | Business Logic | Race conditions, missing rate limits, PII in logs, failing open |

Before launching agents, the skill determines a **threat profile** that calibrates severity to the actual deployment context:

| Profile | Context | Effect |
|---------|---------|--------|
| Personal Tool | Local, single-user, no network | Network/multi-user threats downgraded 2 levels |
| Internal Tool | Self-hosted, multi-user, internal | External-only vectors downgraded 1 level |
| Public Service | Cloud, public, internet-facing | Full OWASP severity, no calibration |

This prevents the skill from crying wolf on a personal desktop app about CSRF protection it doesn't need.

### Mode 2: Enterprise Assessment (`/security assess`)

Four agents evaluate product readiness for enterprise buyers:

| Agent | Domain | What it evaluates |
|-------|--------|-------------------|
| **data-guardian** | Data Handling | Classification, encryption, residency, retention, PII |
| **access-architect** | Access Control | SSO/SAML/SCIM, MFA, RBAC, audit logging |
| **compliance-navigator** | Compliance | SOC 2, ISO 27001, GDPR, trust page readiness |
| **resilience-engineer** | Operations | Incident response, BCP/DR, monitoring, patching |

Each domain gets a maturity score from 0 (Not Started) to 5 (Advanced). The synthesis produces a gap analysis and maps current maturity to deal size readiness.

## Quick Install

```bash
# As part of Meta pack:
git clone https://github.com/vasilievyakov/miracle-infrastructure.git
cd miracle-infrastructure && bash install.sh  # select Meta pack

# Just this skill:
mkdir -p ~/.claude/skills/miracle-security/references
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/miracle-security/SKILL.md \
  -o ~/.claude/skills/miracle-security/SKILL.md
curl -sL https://raw.githubusercontent.com/vasilievyakov/miracle-infrastructure/main/skills/miracle-security/references/checklists.md \
  -o ~/.claude/skills/miracle-security/references/checklists.md
```

## Example

### Code Review

```
> /security review

## Threat Profile
Personal Tool — local macOS app, single user, no network surface
Deployment: local | Users: single | Network: localhost only

## Summary
- Findings: 8 total (0 critical, 0 high, 1 medium, 3 low)
- Security Posture: Good
- Top Risk: SQLite concurrent access without WAL mode
- Severity calibrated for: Personal Tool

## Medium Findings
| # | Severity | Category       | File:Line              | Description                |
|---|----------|----------------|------------------------|----------------------------|
| 1 | MEDIUM   | Concurrent DB  | src/database.py:130    | No WAL mode, SQLITE_BUSY   |

## Low Findings
| # | Severity | Category       | File:Line              | Description                |
|---|----------|----------------|------------------------|----------------------------|
| 2 | LOW      | FTS5 Injection | app/.../SQLiteDB.swift | Search query not sanitized  |
| 3 | LOW      | Logs in /tmp   | launchd/plist:31       | Daemon stderr world-readable|
| 4 | LOW      | Unpinned Deps  | requirements.txt       | psutil without version pin  |

## Top 3 Actions
1. [MEDIUM] Set PRAGMA journal_mode=WAL in Python Database._conn()
2. [LOW] Sanitize FTS5 search queries in Swift (like chat.py does)
3. [LOW] Move launchd stdout/stderr from /tmp to ~/app/logs/

## Positive Observations
Parameterized SQL everywhere (both Python and Swift). No hardcoded secrets.
Minimal dependency footprint (1 Python package, 0 Swift packages). No eval/exec/pickle.
Proper .gitignore covering .env, data/, logs/.

## What Claude Can't Check
- Dependency CVEs (run: pip audit, npm audit)
- Git history secrets (run: TruffleHog, Gitleaks)
- Runtime exploitability (need DAST)
- Prompt injection in LLM features (inherent limitation)
```

### Enterprise Assessment

```
> /security assess

## Enterprise Security Assessment — Acme SaaS

### Maturity Scorecard
| Domain                 | Level            | Score |
|------------------------|------------------|-------|
| Data Handling          | Developing       | 2/5   |
| Access Control         | Beginning        | 1/5   |
| Compliance             | Not Started      | 0/5   |
| Operations & Resilience| Developing       | 2/5   |
| Overall                | Beginning        | 1.25/5|

### Deal Size Alignment
- < $10K/yr deals: Ready
- $10-50K/yr deals: Gaps (SSO, DPA needed)
- $50K+ deals: Not ready (need SOC 2, pen test)
```

## Works great with

- [Directors](../directors/) — get five expert perspectives on the same project the security review just scanned
- [Frameworks](../frameworks/) — apply engineering principles to prioritize the security roadmap
- [Skill Checkup](../skill-checkup/) — audit your skills library health alongside your code security

## Part of

[Meta Pack](../../packs/meta/README.md) — structural audits for your infrastructure and code.
