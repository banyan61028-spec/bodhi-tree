# Evidence method and sufficiency gate

## Evidence hierarchy

Prefer sources in this order for the claim being made:

1. Observable product state or reproducible behavior.
2. Source code reachable from the relevant entry point.
3. Product-generated artifacts, task records, logs, API traces, or schemas.
4. Official documentation describing the same version / feature.
5. User explanation as scope context.

Promotional claims may explain intent but do not prove implementation.

## Evidence labels

- `【页面/代码事实】`: directly visible, reproducible, or explicitly present in relevant code / official runtime output.
- `【合理推断】`: multiple facts support the conclusion, but the underlying implementation is not visible.
- `【建议设计】`: a proposed mechanism that improves correctness, safety, consistency, or maintainability.
- `【未知】`: available evidence does not support a reliable conclusion.

Never rewrite a suggestion as current product behavior.

## Evidence inventory

Assign stable IDs such as `E01`, `E02` or preserve user-provided screenshot IDs. Record:

| Field | Meaning |
|---|---|
| ID | Stable evidence identifier |
| Source | Screenshot, URL/page, code file/line, log, export, asset |
| Timestamp/order | Actual time or relative sequence |
| Visible fact | Exact text, component, state, object, error, or code behavior |
| Scope | Which stage / feature / Agent it covers |
| Limit | Cropped area, missing history, inaccessible state, ambiguity |

Use exact page strings, button names, Agent names, error text, asset counts, state labels, and file links where possible.

## Sufficiency gate

Evidence is sufficient only for the requested scope.

### Interaction / screenshot route

- entry state and earliest available input;
- chronological messages or actions;
- relevant buttons, forms, selections, and confirmation gates;
- result assets or records, not only chat claims;
- task / status surfaces;
- failure, interruption, empty, and partial-success states where present;
- final preview, export, or completion state where relevant.

### Website route

- exact URL and accessible session;
- permission to inspect the relevant surfaces;
- current version / environment;
- safe read-only navigation path;
- authentication handoff if needed.

### Source-code route

- entry point for the feature;
- reachable services / workflows;
- model or tool invocation boundary;
- state and asset persistence;
- error / retry / cancellation path;
- tests or runtime evidence where available.

Source presence alone is not proof that a path runs in production.

## Coverage decision

- `PASS`: enough evidence for the requested scope; continue.
- `LIMITED`: enough for a bounded subset; state excluded areas and continue only within scope.
- `BLOCKED`: no primary evidence or a missing critical stage makes the requested conclusion unsafe; stop and request evidence.

## Conflict handling

When sources disagree:

1. Describe both facts separately.
2. Identify source and time / version.
3. Do not collapse them into one “most likely” truth unless a stronger authoritative state exists.
4. Explain product impact.
5. Add a verification question or test.

Common conflicts include chat versus asset state, frontend versus backend task state, tool result versus persistence, code versus deployed UI, and local cache versus server state.

## Evidence collection safety

- Read only unless the user clearly authorizes mutations.
- Do not submit forms, send messages, generate, regenerate, publish, delete, buy, recharge, or overwrite during evidence collection.
- Do not inspect or output credentials, cookies, tokens, browser storage, secrets, or private identity data.
- If login, OTP, CAPTCHA, or takeover is required, hand control to the user and wait.
- Do not use a public marketing page to fill gaps in a private product workflow.
