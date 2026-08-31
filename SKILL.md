---
name: evidence-based-product-deconstruction
description: Evidence-gated reverse analysis of digital products from screenshots, accessible websites, recordings, exports, or source code. Use when the user asks to拆解、逆向分析、梳理用户旅程、Agent/工具/模型/数据架构，或沉淀产品方法论，并要求基于真实产品证据输出 HTML。 Do not use for ordinary design critique, market research based only on promotional claims, or implementation without product evidence.
---

# Evidence-Based Product Deconstruction

Turn first-party product evidence into a traceable product analysis. Classify the product before choosing the analysis emphasis, then work through four layers: 用户层 → 技术层 → 模型层 → 数据层. Deliver the final report as one self-contained HTML file.

## Non-negotiable invariants

- Do not perform a full deconstruction without primary product evidence. A user description, memory, competitor article, or promotional page alone is insufficient.
- Separate every conclusion into `【页面/代码事实】`, `【合理推断】`, `【建议设计】`, or `【未知】`.
- A product or Agent saying “完成” is not proof. Verify the corresponding state, asset, record, or code path.
- Record contradictions between chat, canvas, task state, asset library, preview, database, or code. Never silently choose one source as truth.
- Do not claim access to hidden chain-of-thought, private prompts, credentials, cookies, tokens, browser storage, or undocumented internal APIs.
- Preserve the user's operational boundaries. Default browser investigation to read-only unless the user explicitly authorizes changes.
- Keep the method generic. Do not bake a previously analyzed product name, story, Agent list, field name, model, or screenshot into this skill or its report template.
- The final deliverable is HTML. Supporting notes may be temporary, but do not substitute Markdown-only output for the requested report.

## Workflow

### 1. Establish the target and analysis question

Identify the current product, product surface, desired insight, requested depth, operational limits, output path, and whether the scope is the whole product, one journey, one Agent, one feature, or one architecture layer.

Do not ask for information that can be safely discovered from provided files or a permitted read-only product session.

### 2. Classify the product before decomposing it

Read [references/product-archetypes.md](references/product-archetypes.md). Select one primary archetype and zero to two secondary archetypes from evidence. State the classification, confidence, and evidence. If hybrid, keep one primary lens and explicitly add secondary lenses instead of applying every checklist equally.

### 3. Apply the evidence gate

Read [references/evidence-method.md](references/evidence-method.md). Build an evidence inventory and coverage matrix before analysis.

Acceptable primary evidence includes one or more of:

- complete or sufficiently scoped screenshots / screen recordings;
- an accessible product URL or authenticated session;
- original source code or a repository export;
- structured product exports, logs, API traces, database schemas, or generated assets supplied by the user.

If no primary evidence is available, stop after producing: what is missing, the minimum evidence package required, safe collection instructions, and the exact next question for the user. Do not output a speculative full decomposition.

If evidence exists but is incomplete, limit analysis to the covered scope, mark missing stages `【未知】`, and request only evidence that would materially change the result.

### 4. Inspect in chronological and state order

For interaction evidence, start at the earliest available user action and follow every visible transition. Check text, buttons, forms, status indicators, assets, history, errors, previews, and exits. Capture user intent/action, UI feedback, decision gates, system result, state/asset changes, failure/retry/interruption/rollback/handoff paths, and inconsistencies.

For source code, trace from entry point to business service, model/tool call, state write, asset persistence, and downstream consumer. Do not infer runtime behavior solely from unused or dead code.

### 5. Decompose four layers

Read [references/four-layer-analysis.md](references/four-layer-analysis.md). Analyze in this order:

1. 用户层
2. 技术层
3. 模型层
4. 数据层

For every layer, distinguish current observable architecture (As-Is) from recommended architecture (To-Be). Trace cross-layer claims back to evidence IDs.

### 6. Synthesize cross-layer flows

Build at least one end-to-end flow appropriate to the target. Show, where evidence supports it: user interaction, control / Agent / service flow, tool and model invocation, context and state, asset/data flow, confirmation, failure, interruption, and recovery.

Use a state machine when completion, retry, confirmation, or interruption is important. Use sequence diagrams for temporal handoffs and architecture diagrams for ownership and data flow. Diagrams must carry evidence IDs or nearby traceability notes.

### 7. Produce the HTML report

Read [references/html-deliverable.md](references/html-deliverable.md). Start from [assets/report-template.html](assets/report-template.html) when it fits; adapt sections to the user's scope rather than padding the report.

The HTML must be self-contained except for an optional Mermaid CDN script. Include a visible evidence legend and a source / gap section near the top. Use full, readable tables with horizontal scrolling on small screens.

### 8. Validate before delivery

Run:

```bash
python3 scripts/validate_report.py /absolute/path/to/report.html
```

Also inspect the report visually when a safe local rendering surface is available. If local rendering is unavailable, report that limitation and still perform structural validation. Do not claim Mermaid rendered successfully unless it was actually rendered or independently parsed.

Deliver a clickable absolute path to the HTML file and summarize only scope, evidence gaps, and validation status.

## Stop conditions

Stop and ask the user for evidence when:

- no primary product evidence is available;
- the target product / feature cannot be identified;
- login, CAPTCHA, OTP, or user takeover is required;
- the next action would create, regenerate, publish, delete, purchase, recharge, send, or overwrite content without explicit authorization;
- evidence sources contradict each other and the requested conclusion depends on resolving the conflict;
- a material choice would change the analysis target or product archetype.

When blocked, preserve gathered evidence and state exactly what is needed next.
