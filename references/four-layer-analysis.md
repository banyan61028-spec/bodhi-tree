# Four-layer analysis framework

Analyze in order because each layer constrains the next. Do not list generic components without evidence or a clear design reason.

## 1. 用户层

Purpose: reconstruct what the user is trying to achieve and what they actually experience.

Inspect target user, job-to-be-done, entry point, original input, chronological journey, stage goals, actions, choices, confirmation gates, back/edit/cancel paths, page feedback, task states, errors, empty states, partial success, visible outputs, emotions, friction, cost anxiety, and gaps between claims and results.

Outputs: evidence table, user journey with normal/modification/failure/interruption paths, decision or state diagram when helpful, and top experience problems / opportunities.

## 2. 技术层

Purpose: explain the observable system needed to produce the user experience.

Inspect client surfaces, applications, orchestration, workflow, state machine, Agent/service boundaries, tool contracts, APIs, queues, workers, persistence, object storage, CDN, integrations, authentication, authorization, tenancy, safety, billing, observability, retry, idempotency, cancellation, compensation, and completion gates.

For every tool or service, capture trigger, input, precondition, result, verification, state write, retry rule, and downstream consumer. Use functional names when official names are not visible and label them non-official.

Outputs: component or Agent contracts, tool table, architecture diagram, sequence/state diagram, and failure/recovery matrix.

## 3. 模型层

Purpose: identify what intelligence or generative capability is required, how it is selected, and how results are verified.

Inspect model roles by modality/task, inputs, context, structured output, references, tool access, routing dimensions, model/prompt/policy versioning, knowledge retrieval, safety/copyright boundaries, evaluation, user feedback, quality gates, fallback, human confirmation, and evidence for actual model names/options.

Do not infer a multi-model router from one visible model option. Do not reconstruct hidden chain-of-thought. Public planning summaries may support functional rules, not official prompts.

Outputs: model capability/routing table, model-knowledge-tool boundary, quality/safety validation plan, and evidence-graded behaviors.

## 4. 数据层

Purpose: explain how user, project, runtime, asset, and feedback truth is represented and transferred.

Inspect user/tenant context, project configuration, business entities, conversation, Agent run, task, tool call, model invocation, confirmation, error, billing, generated assets, immutable versions, stable references, lineage, dependency graph, workflow state, public knowledge versus private assets, permissions, retention, deletion, export, privacy, feedback, evaluation data, and stale downstream data after upstream edits.

Use semantic placeholder field names when real schema is unavailable and label them as analysis design.

Outputs: entity table/ER diagram, global context partitions, producer-consumer and read/write tables, version/lineage/invalidation/access rules.

## Cross-layer synthesis

For each important user action, show:

`User intent → UI action → service/Agent decision → tool/model call → data/state write → asset/result → validation → next user choice`

Every arrow should be supported by evidence, clearly inferred, or explicitly recommended. Include evidence IDs near nodes or in a traceability table.

## As-Is and To-Be separation

As-Is contains only observed facts and bounded inferences. To-Be contains proposed mechanisms. A risk may justify a To-Be component, but does not prove that component currently exists.
