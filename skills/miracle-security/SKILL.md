---
name: miracle-security
description: |
  Security review with two modes: (1) code review — 5 parallel agents scan for OWASP Top 10,
  secrets leaks, auth issues, dependency risks, logic flaws; (2) enterprise assessment — 4 agents
  evaluate product through CISO lens (data handling, access control, compliance, resilience).
  Threat model calibration adjusts severity to deployment context.
  Use when: (1) Before deploy — security audit, (2) Enterprise sales — readiness assessment,
  (3) New project — baseline security posture, (4) After major changes — regression check.
  Triggers: "/security review", "/security assess", "/security", "security check".
---

# Miracle Security — Security Review & Enterprise Assessment

Two security review modes: code review (5 parallel auditor agents) and enterprise assessment (4 parallel evaluator agents). Architecture follows the `/directors` pattern.

## Triggers

- `/security review` — code review of the current project
- `/security assess` — enterprise assessment
- `/security` (no argument) — ask which mode is needed
- `security check`

## Mode Selection

If the user invoked `/security` without specifying a mode — ask:
- **review** — scan code for vulnerabilities (OWASP, secrets, auth, dependencies, logic)
- **assess** — evaluate enterprise readiness of the product (data handling, access control, compliance, resilience)

---

## Mode 1: Code Review

### Step 1: Identify the project stack

Use Glob to find stack markers:
- `package.json` / `package-lock.json` / `yarn.lock` → Node.js
- `requirements.txt` / `pyproject.toml` / `Pipfile` → Python
- `go.mod` → Go
- `Cargo.toml` → Rust
- `*.csproj` → .NET
- `next.config.*` → Next.js
- `docker-compose.*` / `Dockerfile` → Docker

Identify main configuration files, entry points, routes, and middleware.

### Step 2: Threat Model Assessment

Before launching agents — determine the project's threat model. This is **critical** for severity calibration.

Based on README, configuration, presence of servers/API, determine:

| Factor | Options | Impact on severity |
|--------|---------|---------------------|
| **Deployment** | local-only / self-hosted / cloud SaaS | local → severity -2, self-hosted → -1, SaaS → 0 |
| **Users** | single-user / multi-user / public | single → severity -2, multi → -1, public → 0 |
| **Network** | no network / localhost only / internet-facing | no network → severity -2, localhost → -1, internet → 0 |
| **Data sensitivity** | public / internal / PII / financial / health | public → -1, internal → 0, PII+ → +1 |
| **Auth surface** | none / local auth / SSO/OAuth / API keys | none → skip auth findings |

**Threat Profile — final classification:**

```
🏠 Personal Tool  — local, single-user, no network. Threat = physical access + malicious local process
🏢 Internal Tool  — self-hosted, multi-user, internal network. Threat = insider + lateral movement
🌐 Public Service — cloud, public, internet-facing. Threat = full external attack surface
```

**Calibration rules:**

- **🏠 Personal Tool:** Network-based threats (SSRF, CORS, CSRF) → INFO. Multi-user threats (IDOR, privilege escalation, session management) → INFO. File permissions → LOW (not MEDIUM). Main risks: secrets in code, command injection, data loss.
- **🏢 Internal Tool:** Reduce severity by 1 level for external-only vectors. Auth and access control remain important.
- **🌐 Public Service:** Full severity without calibration. All OWASP findings at full strength.

**Prompt injection in LLM applications** is an inherent limitation of the technology, NOT a project vulnerability. Do not include as a finding. May mention in "What Claude Can't Check".

### Step 3: Launch 5 agents IN PARALLEL

All 5 Task tool calls — **in one message**.

| # | Agent ID | Focus |
|---|----------|-------|
| 1 | `injection-hunter` | Injection & XSS |
| 2 | `auth-auditor` | Auth & Access Control |
| 3 | `secrets-scanner` | Secrets & Config |
| 4 | `dependency-checker` | Dependencies & Supply Chain |
| 5 | `logic-analyzer` | Business Logic & Error Handling |

**Each agent receives the threat profile in its prompt:**

```
Task tool:
- description: "Security: {agent_id}"
- subagent_type: "general-purpose"
- prompt: "{agent system_prompt}\n\n---\n\nPROJECT: {project path}\nSTACK: {detected stack}\nTHREAT PROFILE: {🏠/🏢/🌐} {description}\n\nSeverity calibration rules for this profile:\n{rules from the table above}\n\n---\n\nPerform the audit. Return findings in table format."
```

### Step 4: Synthesize results

After receiving all 5 results:
1. Merge all findings
2. **Recalibrate severity** by threat profile (agents may still overrate)
3. Deduplicate (different agents may find the same issue — convergence = strong signal)
4. Sort by severity: CRITICAL → HIGH → MEDIUM → LOW → INFO
5. Collapse positive findings (INFO "all good") into a single "Positive Observations" paragraph
6. Produce the final report

### Severity System

```
🔴 CRITICAL — Exploitable now, data breach risk, immediate fix required
🟠 HIGH     — Significant vulnerability, fix before deploy
🟡 MEDIUM   — Should be fixed, but not immediately exploitable
🔵 LOW      — Best practice improvement, defense in depth
⚪ INFO     — Observation, no immediate action needed
```

### Security Posture (overall rating)

| Posture | Condition |
|---------|---------|
| 🔴 Critical | At least 1 CRITICAL finding |
| 🟠 Needs Work | No CRITICAL, but has HIGH findings |
| 🟡 Fair | No CRITICAL/HIGH, has MEDIUM |
| 🟢 Good | Only LOW and INFO |
| 🟢 Strong | 0-2 LOW findings |

### Output Format — Code Review

```markdown
## 🔒 Security Review — {project name}

### Threat Profile
**{🏠/🏢/🌐} {Personal Tool / Internal Tool / Public Service}** — {1-sentence description}
Deployment: {local/self-hosted/cloud} | Users: {single/multi/public} | Network: {none/localhost/internet}

### Summary
- **Findings:** {N} total ({critical} critical, {high} high, {medium} medium, {low} low)
- **Security Posture:** {Critical / Needs Work / Fair / Good / Strong}
- **Top Risk:** {1-sentence description}
- **Severity calibrated for:** {threat profile name}

### Critical & High Findings
| # | Severity | Category | File:Line | Description | Fix |
|---|----------|----------|-----------|-------------|-----|
| 1 | 🔴 CRITICAL | Secrets | src/config.js:42 | Hardcoded API key | Move to env variable |

### Medium & Low Findings
| # | Severity | Category | File:Line | Description |
|---|----------|----------|-----------|-------------|

### Top 3 Actions
1. [CRITICAL] ...
2. [HIGH] ...
3. [MEDIUM] ...

### Positive Observations
{Collapsed paragraph: what the project does well — parameterized SQL, no secrets, minimal deps, etc.}

### What Claude Can't Check
- Runtime exploitability (need DAST: OWASP ZAP)
- Dependency CVEs (need SCA: `npm audit`, Snyk)
- Git history secrets (need: TruffleHog, Gitleaks)
- Network/infra security (need pentest)
- Prompt injection in LLM features (inherent limitation)
```

---

## Mode 2: Enterprise Assessment

### Step 1: Identify product context

From README, package.json, configuration determine:
- Product type (SaaS, API, mobile app, etc.)
- Target market (SMB, mid-market, enterprise)
- Current stage (MVP, growth, scale)

### Step 2: Launch 4 agents IN PARALLEL

All 4 Task tool calls — **in one message**.

| # | Agent ID | Focus |
|---|----------|-------|
| 1 | `data-guardian` | Data Handling |
| 2 | `access-architect` | Access Control |
| 3 | `compliance-navigator` | Compliance & Trust |
| 4 | `resilience-engineer` | Operations & Resilience |

```
Task tool:
- description: "Security: {agent_id}"
- subagent_type: "general-purpose"
- prompt: "{agent system_prompt}\n\n---\n\nPRODUCT: {product type}\nPATH: {project path}\nCONTEXT: {market, stage}\n\n---\n\nPerform the assessment. Return scorecard + gaps + actions."
```

### Step 3: Synthesize results

1. Collect maturity scores from each agent
2. Calculate overall maturity (average)
3. Gap analysis — merge findings
4. Roadmap — top 5 actions by priority

### Maturity System

```
⬛ Not Started  (0/5) — Not implemented, no plans
🟥 Beginning    (1/5) — Initial steps, ad hoc
🟧 Developing   (2/5) — In progress, partial implementation
🟩 Established  (3/5) — Working, documented, verified
🟦 Advanced     (4/5) — Automated, continuous, best practices
```

### Output Format — Enterprise Assessment

```markdown
## 🏢 Enterprise Security Assessment — {project name}

### Maturity Scorecard
| Domain | Level | Score |
|--------|-------|-------|
| Data Handling | 🟧 Developing | 2/5 |
| Access Control | 🟥 Beginning | 1/5 |
| Compliance | ⬛ Not Started | 0/5 |
| Operations & Resilience | 🟧 Developing | 2/5 |
| **Overall** | **🟧 Developing** | **1.25/5** |

### Gap Analysis
#### Data Handling
- ✅ HTTPS enforced
- ⚠️ No data classification scheme
- ❌ No encryption at rest documentation

#### Access Control
- ...

#### Compliance
- ...

#### Operations & Resilience
- ...

### Enterprise Readiness Roadmap
**Phase 1 (Month 1-3):** Foundation
1. ...

**Phase 2 (Month 3-6):** SOC 2 Type I
2. ...

**Phase 3 (Month 6-12):** Scale
3. ...

### Deal Size Alignment
Based on current maturity, this product is ready for:
- ✅ < $10K/yr deals
- ⚠️ $10-50K/yr deals (gaps: SSO, DPA)
- ❌ $50K+ deals (need SOC 2, pen test)
```

---

## Agent System Prompts — Code Review

### injection-hunter — Injection & XSS

```
You are a security auditor specializing in injection vulnerabilities.

Your task: scan the project and find ALL potential injection vulnerabilities.

What to look for:
- SQL injection: string concatenation in SQL queries, missing parameterized queries, raw queries with user input
- NoSQL injection: $where, $regex with unfiltered input in MongoDB
- Command injection: exec(), spawn(), system() with user input, template strings in shell commands
- SSTI (Server-Side Template Injection): user input in template engines without escaping
- XSS: dangerouslySetInnerHTML, innerHTML, document.write, v-html, [innerHTML], unescaped output in templates
- SSRF: fetch/axios/http.get with URL from user input without validation
- Path traversal: path concatenation with user input, missing path normalization

How to scan:
1. Use Glob to find files by extension (.js, .ts, .py, .go, etc.)
2. Use Grep to search for dangerous patterns (see above)
3. Use Read to examine suspicious files and confirm findings
4. Verify that the found pattern is actually vulnerable (not a false positive)

Response format — findings table:
| Severity | Category | File:Line | Description | Fix |
|----------|----------|-----------|-------------|-----|

Severity: 🔴 CRITICAL, 🟠 HIGH, 🟡 MEDIUM, 🔵 LOW, ⚪ INFO

If nothing is found in a category — say so. Do not fabricate findings.
```

---

### auth-auditor — Auth & Access Control

```
You are a security auditor specializing in authentication and authorization.

Your task: scan the project and find auth and access control issues.

What to look for:
- Missing auth middleware: API endpoints without authentication checks
- IDOR (Insecure Direct Object Reference): object access by ID without ownership verification
- Privilege escalation: ability to elevate privileges, missing role checks
- Broken access control: horizontal/vertical privilege escalation
- Weak session management: missing expiration, predictable session IDs
- JWT issues: missing signature verification, algorithm confusion, sensitive data in payload, missing expiration
- CSRF: missing CSRF tokens on state-changing operations, SameSite cookie not configured
- Password handling: plaintext passwords, weak hashing (MD5, SHA1), missing salt

How to scan:
1. Find routing files (routes, controllers, handlers)
2. Find authentication/authorization middleware
3. Check each endpoint — does it have auth middleware?
4. Find JWT/session handling code
5. Check RBAC/ACL logic

Response format — findings table:
| Severity | Category | File:Line | Description | Fix |
|----------|----------|-----------|-------------|-----|

Severity: 🔴 CRITICAL, 🟠 HIGH, 🟡 MEDIUM, 🔵 LOW, ⚪ INFO

If nothing is found — say so. Do not fabricate findings.
```

---

### secrets-scanner — Secrets & Config

```
You are a security auditor specializing in secrets leaks and insecure configuration.

Your task: scan the project for hardcoded secrets and misconfigurations.

What to look for (secrets):
- Hardcoded API keys: strings like sk_live_, pk_live_, AKIA, AIza, ghp_, gho_, glpat-, xoxb-, xoxp-
- Hardcoded passwords: password = "...", passwd, secret, variables with "key" in the name with string values
- Hardcoded tokens: Bearer tokens, JWT tokens in code, OAuth tokens
- Private keys: BEGIN RSA PRIVATE KEY, BEGIN EC PRIVATE KEY, BEGIN OPENSSH PRIVATE KEY
- Connection strings: mongodb://, postgres://, mysql:// with credentials
- .env files in git: check .gitignore for .env entries

What to look for (config):
- Debug mode in production: DEBUG=true, NODE_ENV=development in production config
- Permissive CORS: Access-Control-Allow-Origin: *, credentials: true + wildcard origin
- Missing security headers: HSTS, X-Content-Type-Options, X-Frame-Options, CSP
- Unsafe cookie flags: missing httpOnly, secure, SameSite
- Exposed error details: stack traces in production responses
- Open redirect: redirect URL from user input without validation

How to scan:
1. Grep for secret patterns (API keys, passwords, tokens)
2. Check .gitignore — are .env, *.pem, *.key included?
3. Find configuration files (config.*, .env.example, settings.*)
4. Check CORS settings
5. Check cookie settings

Response format — findings table:
| Severity | Category | File:Line | Description | Fix |
|----------|----------|-----------|-------------|-----|

Severity: 🔴 CRITICAL, 🟠 HIGH, 🟡 MEDIUM, 🔵 LOW, ⚪ INFO

If nothing is found — say so. Do not fabricate findings.
```

---

### dependency-checker — Dependencies & Supply Chain

```
You are a security auditor specializing in dependencies and supply chain.

Your task: scan the project for dependency-related issues.

What to look for:
- Lock file presence: is there package-lock.json / yarn.lock / pnpm-lock.yaml? Without a lock file — supply chain risk
- Suspicious dependencies: unusually small packages with broad permissions, typosquatting (lodas instead of lodash)
- Unsafe imports: eval(), exec(), pickle.loads(), yaml.load() (without SafeLoader), subprocess with shell=True
- Dangerous dynamic imports: import() with variables, require() with user input
- Prototype pollution: Object.assign with untrusted data, merge/extend without protection, __proto__ in input
- Deserialization: JSON.parse without schema validation, unserialize with user input
- Outdated runtime: check engines in package.json, python_requires, etc.
- Post-install scripts: check scripts.postinstall in dependencies

How to scan:
1. Read package.json / requirements.txt / go.mod — dependency list
2. Grep for eval, exec, pickle, yaml.load, subprocess
3. Check for lock file presence
4. Check postinstall scripts
5. Evaluate quantity and quality of dependencies

Response format — findings table:
| Severity | Category | File:Line | Description | Fix |
|----------|----------|-----------|-------------|-----|

Severity: 🔴 CRITICAL, 🟠 HIGH, 🟡 MEDIUM, 🔵 LOW, ⚪ INFO

If nothing is found — say so. Do not fabricate findings.
```

---

### logic-analyzer — Business Logic & Error Handling

```
You are a security auditor specializing in business logic and error handling.

Your task: scan the project for logic vulnerabilities.

What to look for:
- Race conditions: TOCTOU, double-spend, concurrent access without locks, missing transactions
- Missing rate limiting: API endpoints without rate limits (login, register, password reset, API keys)
- Verbose error messages: stack traces in responses, database errors exposed, internal paths in errors
- Sensitive data in logs: passwords, tokens, PII in console.log/logger
- Failing open: try/catch that swallows errors and continues, default allow
- Missing input validation: no type, length, or format validation at API inputs
- Mass assignment: Object.assign(model, req.body), spread without whitelist, **kwargs in Django
- Insecure randomness: Math.random() for security-critical operations (tokens, IDs)
- Timing attacks: string comparison for secrets instead of constant-time comparison

How to scan:
1. Find API endpoints and their handlers
2. Check error handling (try/catch, error processing)
3. Check input validation
4. Find logging — what gets logged
5. Check random value generation for security

Response format — findings table:
| Severity | Category | File:Line | Description | Fix |
|----------|----------|-----------|-------------|-----|

Severity: 🔴 CRITICAL, 🟠 HIGH, 🟡 MEDIUM, 🔵 LOW, ⚪ INFO

If nothing is found — say so. Do not fabricate findings.
```

---

## Agent System Prompts — Enterprise Assessment

### data-guardian — Data Handling

```
You are a CISO-level expert in data handling. Evaluate the project as an enterprise security director deciding whether to allow this product into your organization.

Evaluation areas:
1. **Data Classification** — is there a data classification scheme? How are PII, sensitive, and public data separated?
2. **Encryption at Rest** — is data encrypted in storage? What algorithm?
3. **Encryption in Transit** — is HTTPS enforced? TLS version? Certificate pinning?
4. **Data Residency** — where is data stored? Is there a region selection option? Cross-border transfers?
5. **Retention & Deletion** — is there a data retention policy? Automated deletion? Right to erasure?
6. **PII Handling** — how is personal data processed? Masking? Minimization?
7. **Backup & Recovery** — are there backups? Is recovery tested?

How to scan:
1. Read README, documentation, privacy policy if available
2. Find data models (schemas, models, migrations)
3. Check database configuration
4. Find PII handling (email, phone, address, SSN, credit card)
5. Check encryption (crypto, bcrypt, AES, encryption)
6. Check HTTPS configuration

Response format:

**Maturity Level:** {⬛/🟥/🟧/🟩/🟦} {Not Started/Beginning/Developing/Established/Advanced} ({0-5}/5)

**Gap Analysis:**
- ✅ {what is implemented}
- ⚠️ {what is partial}
- ❌ {what is missing}

**Top 3 Actions:**
1. ...
2. ...
3. ...
```

---

### access-architect — Access Control

```
You are a CISO-level expert in access management. Evaluate the project as an enterprise security director.

Evaluation areas:
1. **SSO/SAML/OIDC** — is enterprise SSO supported? Which providers?
2. **MFA** — is multi-factor authentication available? Mandatory or optional?
3. **RBAC/ABAC** — is there a role model? Granularity of permissions?
4. **SCIM** — automated user provisioning/deprovisioning?
5. **Audit Logging** — are user actions logged? Immutable logs?
6. **Session Management** — timeout, concurrent sessions, device management?
7. **API Authentication** — API keys, OAuth2, scopes, rate limiting per key?

How to scan:
1. Find auth module (auth, login, session, middleware)
2. Check user models (roles, permissions, groups)
3. Find authorization middleware
4. Check SSO integration (SAML, OAuth, OIDC)
5. Find audit/event logging
6. Check API authentication

Response format:

**Maturity Level:** {⬛/🟥/🟧/🟩/🟦} {Not Started/Beginning/Developing/Established/Advanced} ({0-5}/5)

**Gap Analysis:**
- ✅ {what is implemented}
- ⚠️ {what is partial}
- ❌ {what is missing}

**Top 3 Actions:**
1. ...
2. ...
3. ...
```

---

### compliance-navigator — Compliance & Trust

```
You are a CISO-level expert in compliance and trust. Evaluate the project as an enterprise security director.

Evaluation areas:
1. **SOC 2 Type II** — available? Process started? Which trust service criteria are covered?
2. **ISO 27001** — certification? ISMS documentation?
3. **GDPR** — DPA, privacy policy, consent management, data subject rights, DPO?
4. **HIPAA** — BAA, PHI handling, access controls, audit trails? (if applicable)
5. **PCI-DSS** — card processing? SAQ level? (if applicable)
6. **Trust Page** — public security page? Status page? Security.txt?
7. **Subprocessor List** — is the list of third parties documented?
8. **Vulnerability Disclosure** — is there a responsible disclosure policy?

How to scan:
1. Find documentation (docs, legal, compliance, security, trust)
2. Check for privacy policy, terms of service
3. Find security.txt, .well-known/security.txt
4. Check consent management (cookie banner, GDPR consent)
5. Find DPA, BAA templates
6. Check logging for audit trail

Response format:

**Maturity Level:** {⬛/🟥/🟧/🟩/🟦} {Not Started/Beginning/Developing/Established/Advanced} ({0-5}/5)

**Gap Analysis:**
- ✅ {what is implemented}
- ⚠️ {what is partial}
- ❌ {what is missing}

**Top 3 Actions:**
1. ...
2. ...
3. ...
```

---

### resilience-engineer — Operations & Resilience

```
You are a CISO-level expert in operational resilience. Evaluate the project as an enterprise security director.

Evaluation areas:
1. **Incident Response** — is there an IRP? Runbooks? Escalation matrix? Communication plan?
2. **BCP/DR** — are RPO/RTO defined? Disaster recovery plan? Tested?
3. **Monitoring & Alerting** — what is monitored? Alerting configured? Dashboards?
4. **Vulnerability Management** — patching process? SLA by severity? Scanning?
5. **Patching Cadence** — how often are dependencies updated? Automated?
6. **Bug Bounty** — is there a program? VDP (Vulnerability Disclosure Policy)?
7. **Infrastructure as Code** — IaC? Immutable infra? Configuration versioning?
8. **Secrets Management** — how are secrets managed in production? Vault? KMS? Rotation?

How to scan:
1. Find CI/CD configuration (.github/workflows, Jenkinsfile, .gitlab-ci.yml)
2. Check Docker/Kubernetes configuration
3. Find monitoring (Sentry, Datadog, PagerDuty, Grafana)
4. Check IaC (Terraform, CloudFormation, Pulumi)
5. Find runbooks, incident documentation
6. Check secrets management (vault, KMS, .env handling)

Response format:

**Maturity Level:** {⬛/🟥/🟧/🟩/🟦} {Not Started/Beginning/Developing/Established/Advanced} ({0-5}/5)

**Gap Analysis:**
- ✅ {what is implemented}
- ⚠️ {what is partial}
- ❌ {what is missing}

**Top 3 Actions:**
1. ...
2. ...
3. ...
```

---

## Rules

- **All agents launch SIMULTANEOUSLY** in one message via Task tool
- Each agent checks ONLY its own area — no duplication across agents
- Agents do not know about each other — each works independently
- If the project is too small for enterprise assessment — say so and suggest code review
- Findings must contain **specific** file:line references, not abstract recommendations
- Do NOT fabricate findings — if nothing is found, say so
- Detailed checklists for agents are in `references/checklists.md` (load when needed)
- Security posture and maturity level — calculate strictly by the rules, do not inflate or deflate
