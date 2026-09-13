# AGENTS.md — SwarmForgeAI Repo Guidance

## Purpose
This repo is the **SwarmForgeAI** product under SimpliCoreAI.

See `~/AgenticHub/SIMPLICOREAI_PLATFORM.md` for umbrella platform framing.

SwarmForgeAI is a multi-agent platform for small businesses, starting with hospitality. Its goal is to help operators coordinate AI agents across workflows like marketing, revenue, operations, approvals, and business insights—without losing trust, control, or visibility.

## Current Repo Shape
Right now this repo is lightweight and early-stage. The current visible artifact is a hospitality-oriented demo experience.

Treat the repo as an early product prototype, not yet a finished platform.

## Product Direction
SwarmForgeAI should evolve toward:
- multi-agent business workflow orchestration
- clear operator dashboards
- approval-aware task execution
- verticalized experiences starting with hospitality
- strong visibility into what each agent did and why

## Working Style
- Preserve forward momentum; do not over-engineer the first version.
- Favor concrete business workflows over abstract agent theater.
- Optimize for operator trust, not flashy complexity.
- Keep the hospitality starting point explicit unless expanded intentionally.
- Separate public marketing surfaces from protected operator surfaces.

## Business-Safe Rules
- Never assume permission to trigger external business actions without explicit approval.
- Drafts, recommendations, and analyses are safer defaults than automatic execution.
- High-impact actions should be reviewable.
- Anything customer-facing, financial, or reputation-sensitive should be treated as approval-worthy unless the product explicitly defines otherwise.

## UX and Product Guardrails
SwarmForgeAI should feel like:
- an AI operating layer for the business
- a system with accountable sub-agents
- a practical decision and execution tool

It should not feel like:
- a toy multi-agent demo with no business value
- an opaque autopilot
- a dashboard that hides risk behind pretty metrics

## Architecture Direction
As the repo grows, keep these separations clean where possible:
- public landing / marketing pages
- authentication / login entry points
- protected product application surfaces
- reusable agent/workflow logic
- business-specific data and configuration

## Validation Expectations
For meaningful changes, verify with the lightest credible checks available:
- route/path sanity for web flows
- login or gating behavior if auth-related changes are made
- smoke checks for demo interactions when UI files change
- asset loading sanity for static pages

If there is no formal test suite yet, say that plainly.

## Change Discipline
- Make reversible changes when shaping early product structure.
- Prefer additive scaffolding over destructive rewrites.
- Document new assumptions as the repo evolves.
- Keep naming, paths, and product framing consistent with the hospitality-first MVP.

## When Unsure
Choose the option that improves:
1. operator trust
2. clarity of agent behavior
3. business usefulness
4. separation between public and protected surfaces
5. future platform extensibility without premature complexity
