# Product archetype routing

Classify from observed behavior, not marketing labels. Choose one primary archetype and optionally up to two secondary archetypes.

## AIGC creation product

Signals: users provide prompts, scripts, references, style or generation parameters; the product creates or edits text, images, audio, video, 3D, or other media.

Prioritize:

- input sufficiency and prompt / parameter capture;
- staged generation and user confirmation gates;
- model choice, capabilities, limits, latency, cost, and safety;
- reference asset reuse and consistency across outputs;
- asset lineage, versions, retries, partial success, and final composition;
- quality validation beyond a tool's success flag;
- quota estimation, reservation, settlement, and failure refunds.

Core failures: prompt drift, inconsistent characters/style, missing assets, partial generation presented as complete, duplicate generation / billing, stale downstream assets after an upstream edit.

## General execution Agent

Signals: a user delegates an outcome; the system plans, chooses tools, changes external or local state, waits, retries, and reports completion.

Prioritize:

- task interpretation, planning boundaries, and authorization;
- tool selection and observable tool results;
- state machine, checkpoints, long-running execution, and resumability;
- confirmation gates for external or destructive actions;
- idempotency, retry, cancellation, rollback, and compensation;
- Agent / sub-Agent handoff contracts;
- proof of completion, audit trail, and status consistency.

Core failures: claimed completion without effects, action beyond authorization, repeated side effects, cancellation not propagated, lost handoff context, tool success but state write failure.

## Conversational companion product

Signals: the product's primary value is ongoing conversation, emotional support, role / persona continuity, relationship progression, or personalized companionship.

Prioritize:

- conversation goals, tone, persona boundaries, and user control;
- short-term context versus long-term memory;
- consent, memory visibility, edit / forget controls, and privacy;
- emotional state inference and uncertainty;
- crisis / safety escalation and dependency safeguards;
- persona consistency, recall errors, and relationship-state transitions;
- retention mechanics that may conflict with user wellbeing.

Core failures: fabricated memory, sensitive-memory leakage, manipulative dependency, overconfident emotion diagnosis, unsafe crisis handling, persona drift.

## Workflow / vertical SaaS

Signals: forms, records, approvals, queues, role permissions, dashboards, reports, and business workflows dominate.

Prioritize: roles and permissions, record lifecycle, validation, approval gates, bulk operations, integrations, auditability, exceptions, data export, and regulatory requirements.

## Transaction / marketplace product

Signals: catalog, pricing, cart, booking, order, payment, fulfillment, refund, or dispute.

Prioritize: inventory truth, quote and price changes, payment state, idempotent orders, fraud / risk, fulfillment, cancellation / refund, and customer support evidence.

## Content / community product

Signals: publishing, feed, recommendation, moderation, comments, follows, or creator monetization.

Prioritize: creation and distribution loop, ranking inputs, moderation, audience controls, attribution, abuse, notifications, and creator / consumer incentives.

## Developer / infrastructure product

Signals: APIs, SDKs, repositories, deployments, logs, observability, or automation pipelines.

Prioritize: setup path, interface contracts, environment boundaries, error semantics, backwards compatibility, security, performance, telemetry, and operational recovery.

## Hybrid rule

1. Pick the archetype that owns the user's main outcome as primary.
2. Add secondary archetypes only for materially different control, model, or data risks.
3. State which checklist item came from which lens.
4. Do not manufacture nonexistent components because a secondary archetype commonly has them.
