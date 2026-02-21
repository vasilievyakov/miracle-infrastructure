# Example Project

## Status
Active

## Description
A sample web application for task management. Built with Next.js and PostgreSQL. Used by a small team of 3.

## Architecture
- Frontend: Next.js 14, React, Tailwind CSS
- Backend: Next.js API routes
- Database: PostgreSQL via Prisma ORM
- Deployment: Vercel
- Auth: NextAuth.js with GitHub OAuth

## Current State
- Last session: 2026-02-20
- Done: Added user dashboard with task statistics
- Uncommitted: no

## Unresolved Problems
- Slow query on tasks list when filtering by date range (>2s for 10k+ tasks)
- Email notifications sometimes delayed by 5-10 minutes

## Decisions Made
- [2026-02-15] Chose Prisma over Drizzle for ORM. Prisma has better docs and team familiarity
- [2026-02-18] Switched from REST to tRPC for type safety across frontend/backend boundary
- [2026-02-20] Dashboard uses server components for initial load, client components for interactivity

## Next Steps
1. Optimize the date range filter query (add composite index)
2. Investigate email delay (check queue processing interval)
3. Add export to CSV feature

## Session History
- [2026-02-20] Built user dashboard with charts (recharts), task completion rate, overdue counter
- [2026-02-18] Migrated API from REST to tRPC, updated all frontend calls
- [2026-02-15] Initial project setup, database schema, auth flow
