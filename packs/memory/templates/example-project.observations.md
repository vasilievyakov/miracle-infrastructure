# Observations - example-project

## Index
| # | Date | Type | Summary | Files |
|---|------|------|---------|-------|
| 1 | 2026-02-15 | decision | Chose Prisma over Drizzle for ORM | schema.prisma |
| 2 | 2026-02-18 | decision | Migrated REST to tRPC | api/*, lib/trpc.ts |
| 3 | 2026-02-18 | discovery | tRPC bundle size +40KB gzipped | package.json |
| 4 | 2026-02-20 | feature | User dashboard with task stats | app/dashboard/* |
| 5 | 2026-02-20 | problem | Slow date range filter query | lib/queries.ts |

## Details

### [1] 2026-02-15 | decision | Chose Prisma over Drizzle for ORM
**Before:** No ORM selected, raw SQL queries
**After:** Prisma with typed client, migrations, and seed scripts
**Files:** schema.prisma, lib/db.ts
**Why:** Team has prior Prisma experience. Drizzle is lighter, with better performance for complex queries. Chose familiarity over marginal performance gain since the app is not query-heavy.

### [2] 2026-02-18 | decision | Migrated REST to tRPC
**Before:** 12 REST endpoints in /api/* with manual type definitions
**After:** tRPC router with end-to-end type safety, automatic inference on client
**Files:** api/trpc/*, lib/trpc.ts, all frontend API calls
**Why:** Type mismatches between frontend and backend caused 3 bugs in one week. tRPC eliminates this class of errors entirely.

### [3] 2026-02-18 | discovery | tRPC adds ~40KB gzipped to client bundle
**Before:** Assumed tRPC was lightweight
**After:** Measured +40KB gzipped. Acceptable for this app, would reconsider for a public-facing landing page.
**Files:** package.json, next.config.js
**Why:** Noticed during bundle analysis after migration

### [4] 2026-02-20 | feature | User dashboard with task completion stats
**Before:** No overview. Users had to count tasks manually
**After:** Dashboard with completion rate chart (recharts), overdue counter, weekly trend
**Files:** app/dashboard/page.tsx, app/dashboard/components/*
**Why:** Users requested a way to see progress at a glance

### [5] 2026-02-20 | problem | Date range filter query takes >2s for 10k+ tasks
**Symptoms:** GET /api/tasks?from=...&to=... takes 2-4 seconds when the user has many tasks
**Impact:** Dashboard feels sluggish for power users
**Status:** Open
**Files:** lib/queries.ts, schema.prisma
**Why:** No composite index on (userId, createdAt). Prisma generates a sequential scan.
