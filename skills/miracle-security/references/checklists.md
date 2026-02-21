# Security Checklists — Reference Material

Детальные чеклисты для агентов miracle-security. Загружаются по необходимости (Level 3).

---

## OWASP Top 10 (2021) — Code Patterns

### A01: Broken Access Control
```
# Missing auth middleware
Grep: route|router|app\.(get|post|put|delete|patch)
Check: each endpoint has auth middleware

# IDOR
Grep: params\.id|req\.params|request\.params
Check: ownership verification before data access

# Directory traversal
Grep: path\.join|path\.resolve|readFile|readFileSync
Check: input not used directly in file paths
```

### A02: Cryptographic Failures
```
# Weak hashing
Grep: md5|sha1|createHash\(['"]md5|createHash\(['"]sha1
Fix: Use bcrypt/scrypt/argon2 for passwords, SHA-256+ for data

# Missing encryption
Grep: password|secret|token|apiKey|api_key
Check: not stored in plaintext

# Weak TLS
Grep: SSLv3|TLSv1\.0|TLSv1\.1|secureProtocol
Fix: TLS 1.2+ only
```

### A03: Injection
```
# SQL injection
Grep: query\(.*\+|query\(`|execute\(.*\+|\.raw\(|\.extra\(
Fix: Parameterized queries, ORM

# NoSQL injection
Grep: \$where|\$regex|\$gt|\$lt|\$ne
Check: user input not in query operators

# Command injection
Grep: exec\(|execSync\(|spawn\(|system\(|popen\(|subprocess
Check: no user input in commands

# SSTI
Grep: render_template_string|Template\(|Jinja2|nunjucks\.renderString
Check: no user input in template strings
```

### A04: Insecure Design
```
# Missing rate limiting
Grep: /login|/register|/reset|/forgot|/api/
Check: rate limiter middleware present

# No CAPTCHA on sensitive forms
Grep: login|register|contact|forgot
Check: bot protection on public forms
```

### A05: Security Misconfiguration
```
# Debug mode
Grep: DEBUG\s*=\s*[Tt]rue|NODE_ENV.*development|app\.debug
Check: not in production config

# Default credentials
Grep: admin:admin|root:root|password:password|test:test
Fix: Remove all default credentials

# Stack traces exposed
Grep: stackTrace|stack_trace|traceback|showStackTrace
Check: disabled in production

# CORS misconfiguration
Grep: Access-Control-Allow-Origin.*\*|cors\(\)|origin:\s*true
Check: not wildcard with credentials
```

### A06: Vulnerable Components
```
# Check for lock files
Glob: package-lock.json, yarn.lock, pnpm-lock.yaml, Pipfile.lock, poetry.lock, go.sum
Missing = HIGH risk

# Known vulnerable patterns
Grep: lodash.*<4\.17|express.*<4\.17|django.*<3\.2|flask.*<2\.0
```

### A07: Auth Failures
```
# Weak JWT
Grep: algorithm.*none|verify.*false|jwt\.decode\(|HS256
Check: RS256/ES256, verify=true, proper expiration

# Session fixation
Grep: session\.regenerate|regenerateSession|session_regenerate_id
Check: session regenerated after login

# Missing password policy
Grep: password.*length|minLength|password.*validation
Check: minimum 8 chars, complexity requirements
```

### A08: Data Integrity
```
# Unsafe deserialization
Grep: pickle\.loads|yaml\.load\(|unserialize|JSON\.parse
Check: yaml.safe_load, validated schemas

# Missing integrity checks
Grep: download|fetch.*url|import.*from
Check: integrity/checksum verification for external resources
```

### A09: Logging Failures
```
# Missing audit logging
Grep: login|logout|delete|admin|permission|role
Check: security events are logged

# Sensitive data in logs
Grep: console\.log.*password|logger.*token|log.*secret|print.*key
Fix: Sanitize sensitive data before logging
```

### A10: SSRF
```
# Server-Side Request Forgery
Grep: fetch\(|axios\(|http\.get\(|urllib|requests\.get
Check: URL validation, allowlist, no internal network access
```

---

## Secrets Patterns (Regex)

```
# AWS
AKIA[0-9A-Z]{16}
[0-9a-zA-Z/+]{40}  (AWS Secret Key, near "aws" context)

# GCP
AIza[0-9A-Za-z\-_]{35}
[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com

# Azure
[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}  (near "azure" context)

# GitHub
ghp_[0-9a-zA-Z]{36}
gho_[0-9a-zA-Z]{36}
github_pat_[0-9a-zA-Z_]{82}

# Stripe
sk_live_[0-9a-zA-Z]{24,}
pk_live_[0-9a-zA-Z]{24,}
rk_live_[0-9a-zA-Z]{24,}

# Slack
xoxb-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}
xoxp-[0-9]{11}-[0-9]{11}-[0-9a-zA-Z]{24}

# Twilio
SK[0-9a-fA-F]{32}

# SendGrid
SG\.[0-9A-Za-z\-_]{22}\.[0-9A-Za-z\-_]{43}

# OpenAI
sk-[0-9a-zA-Z]{48}

# Generic patterns
(?i)(api[_-]?key|apikey|secret[_-]?key|access[_-]?token|auth[_-]?token|credentials|private[_-]?key)\s*[:=]\s*['"][^'"]{8,}['"]

# Private keys
-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----
-----BEGIN PGP PRIVATE KEY BLOCK-----

# Connection strings
(?i)(mongodb|postgres|mysql|redis|amqp):\/\/[^:]+:[^@]+@
```

---

## Enterprise Readiness Checklist

### Data Handling
- [ ] Data classification scheme documented
- [ ] Encryption at rest (AES-256)
- [ ] Encryption in transit (TLS 1.2+)
- [ ] Data residency options (EU, US, etc.)
- [ ] Data retention policy
- [ ] Automated data deletion / right to erasure
- [ ] PII inventory and DPA
- [ ] Backup encryption
- [ ] Cross-border transfer mechanisms (SCCs, adequacy decisions)

### Access Control
- [ ] SSO via SAML 2.0 / OIDC
- [ ] SCIM provisioning/deprovisioning
- [ ] MFA (TOTP, WebAuthn, push)
- [ ] RBAC with granular permissions
- [ ] API key management (create, rotate, revoke)
- [ ] Session timeout and management
- [ ] Audit logging (immutable, exportable)
- [ ] IP allowlisting
- [ ] Just-in-time access / least privilege

### Compliance & Trust
- [ ] SOC 2 Type II report
- [ ] ISO 27001 certification
- [ ] GDPR compliance documentation
- [ ] HIPAA BAA (if applicable)
- [ ] PCI-DSS SAQ (if applicable)
- [ ] Privacy policy (CCPA, GDPR compliant)
- [ ] Terms of service
- [ ] DPA (Data Processing Agreement)
- [ ] Subprocessor list
- [ ] Trust/security page (public)
- [ ] security.txt / .well-known/security.txt
- [ ] Responsible disclosure / bug bounty policy
- [ ] Penetration test report (annual)

### Operations & Resilience
- [ ] Incident response plan (IRP)
- [ ] Business continuity plan (BCP)
- [ ] Disaster recovery plan with RPO/RTO
- [ ] 24/7 monitoring and alerting
- [ ] Status page (public)
- [ ] SLA documentation (uptime guarantee)
- [ ] Vulnerability management process
- [ ] Patch management SLA (<24h critical, <7d high)
- [ ] Security awareness training
- [ ] Vendor risk management
- [ ] Change management process

---

## Framework-Specific Patterns

### Node.js / Express
```
# Helmet missing (security headers)
Grep: helmet|app\.use\(helmet
Missing = MEDIUM

# Express rate limit
Grep: express-rate-limit|rateLimit|rate-limit
Missing = HIGH (on auth endpoints)

# NoSQL injection (MongoDB)
Grep: \$where|\$regex|\.find\(.*req\.|\.findOne\(.*req\.
Fix: Validate/sanitize input

# Prototype pollution
Grep: Object\.assign|\.merge\(|\.extend\(|lodash\.merge
Check: deep merge with untrusted data
```

### Python / Django / Flask
```
# Django DEBUG
Grep: DEBUG\s*=\s*True
Check: not in production settings

# SQL injection
Grep: \.raw\(|\.extra\(|cursor\.execute.*%|cursor\.execute.*\.format
Fix: Use ORM, parameterized queries

# Pickle deserialization
Grep: pickle\.loads|pickle\.load|cPickle
Fix: Never deserialize untrusted data

# YAML unsafe load
Grep: yaml\.load\(
Fix: yaml.safe_load()

# Shell injection
Grep: os\.system|subprocess.*shell=True|os\.popen
Fix: subprocess with list args, no shell=True
```

### React / Next.js
```
# XSS via dangerouslySetInnerHTML
Grep: dangerouslySetInnerHTML
Check: input is sanitized (DOMPurify)

# Exposed API keys in client
Grep: NEXT_PUBLIC_|REACT_APP_
Check: no secrets in NEXT_PUBLIC_ / REACT_APP_ vars

# Missing CSP
Grep: Content-Security-Policy|contentSecurityPolicy
Missing = MEDIUM

# Open redirect
Grep: redirect|router\.push|window\.location
Check: URL validated against allowlist
```

### MongoDB
```
# No auth
Grep: mongodb://localhost|mongodb://127\.0\.0\.1
Check: auth enabled, not default port exposed

# Injection via operators
Grep: req\.body.*\$|req\.query.*\$
Fix: Sanitize $ operators from user input
```

---

## Trust Page Components Checklist

Для enterprise assessment — что должно быть на trust/security page:

- [ ] Security overview (approach description)
- [ ] Certifications & compliance badges
- [ ] Data encryption (at rest + in transit)
- [ ] Infrastructure provider info
- [ ] Access control description
- [ ] Incident response process
- [ ] Penetration testing (when, by whom)
- [ ] Bug bounty / vulnerability disclosure
- [ ] Privacy policy link
- [ ] DPA download link
- [ ] SOC 2 report request form
- [ ] Subprocessor list link
- [ ] Status page link
- [ ] Contact: security@company.com
- [ ] security.txt at /.well-known/security.txt
