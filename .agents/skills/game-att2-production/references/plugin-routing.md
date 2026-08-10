# Plugin routing

Use this reference only when a Game att2 task involves an external connector, add-on, remote system, participant data, telemetry, security review, or plugin recommendation. Keep local development and deterministic verification independent of plugins.

## Apply the decision gate

Before invoking an external tool, confirm all five conditions:

1. The explicit task needs information or an action unavailable in the local repository.
2. The connector is installed, authenticated, and limited to the required account or project.
3. The planned read or write is within the user's authority and request.
4. No secret, participant identity, raw session record, or unpublished owner material will leave the repository without explicit approval.
5. The result can be traced back into the repository when it affects requirements, decisions, evidence, or release status.

Prefer read-only discovery. Before any external write, state the exact target and intended mutation. Never copy credentials into project files, logs, prompts, issues, or reports.

## Route installed core plugins

### GitHub

Use GitHub for remote issues, pull requests, review comments, checks, releases, repository metadata, or provenance not available in the local clone. The local worktree remains the editing and test surface.

- Read remote state when the user asks about it or when merge/release status materially depends on it.
- Create or change issues, branches, pull requests, comments, labels, releases, or files only when the user requests that external mutation.
- Treat issue labels, milestones, and project fields as coordination metadata, not design authority.
- Reconcile an accepted remote decision into the appropriate authoritative repository document.

### Codex Security

Use Codex Security when a change introduces or materially alters untrusted input, dependency loading, file parsing, network access, credential handling, packaging, CI/CD, distribution, or release-facing attack surface.

- Do not require a scan for routine rules, deterministic simulator logic, fixtures, tests, or documentation with no new trust boundary.
- Scope scans to the changed surface and retain actionable findings with file-level evidence.
- Treat P0/P1 findings as acceptance blockers. Record lower-severity findings, their disposition, and the owner of any accepted risk.
- Do not represent a completed scan as proof that the product is secure.

## Defer conditional workflow plugins

Do not install or connect these until the named gate is open:

| Plugin family | Gate | Allowed role | Required repository trace |
|---|---|---|---|
| Airtable | Owner approves the P01-P08 study schema, privacy fields, retention, and export | Participant/session operations without unnecessary PII | Lossless, versioned research export plus evidence-class labels |
| Google Drive or Notion | The owner identifies an external source that must be consulted | Read owner-authored source material | Reconcile accepted decisions into authoritative Markdown; keep the source link and date |
| Linear, Asana, or Monday.com | The team already uses the tracker and requests synchronization | Mirror approved tasks, gates, owners, and status | Repository requirements and gate documents remain authoritative |
| Figma or Canva | A presentation, UI review, or asset gate opens | Review or produce presentation-layer artifacts | Keep approved source/export artifacts and decision notes in the repository |
| PostHog or Sentry | A playable build exists and telemetry/privacy plans are approved | Product telemetry or runtime fault evidence | Version event schemas, consent basis, build identity, and exported evidence |

Never move playtest PII or raw observations into a plugin by default. Use participant codes, minimum necessary fields, documented retention, and an approved deletion/export path.

## Reject currently irrelevant infrastructure

Do not recommend or connect hosting, database, billing, CRM, marketing, video, or website plugins merely because they are available. Cloudflare, Vercel, Supabase, Neon, Stripe, HubSpot, Apollo, Semrush, Wix, Base44, Lovable, Replit, Remotion, HeyGen, and similar services need a separately approved requirement and trust-boundary review.

## Report connector use

In the final result, name each connector used, distinguish reads from writes, link or identify the external artifact when possible, disclose any data transfer, and state what repository file now records the authoritative outcome. If no plugin was necessary, say that local evidence was sufficient.
