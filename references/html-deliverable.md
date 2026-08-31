# HTML deliverable contract

Produce one standalone `.html` file in the user's requested language.

## Recommended order

Adapt depth to scope, but keep this order unless the user specifies another:

1. Executive summary and product archetype classification
2. Scope, operational boundaries, evidence inventory, and coverage result
3. Evidence gaps and contradictions
4. 用户层
5. 技术层
6. 模型层
7. 数据层
8. End-to-end cross-layer flow
9. As-Is versus To-Be
10. Prioritized risks and product opportunities
11. Rule/component/conclusion to evidence traceability
12. Unknowns and next verification questions

For a narrow request, keep the evidence gate and four-layer thinking but include only sections that materially apply.

## Presentation requirements

- Responsive layout, readable typography, accessible contrast, and sticky contents for long reports.
- Visible legend for `【页面/代码事实】`, `【合理推断】`, `【建议设计】`, and `【未知】`.
- Tables in scroll containers on small screens.
- Mermaid for flows, states, sequences, and ER diagrams only when useful.
- Evidence IDs on nodes or in an adjacent mapping table.
- Real screenshot thumbnails only when supplied and materially helpful; otherwise link local evidence.
- No secrets or sensitive identifiers.
- Functional tool names and semantic schema names marked non-official.

## Minimum evidence presentation

Every material conclusion needs evidence level, evidence ID/file/URL/code line, observable fact, limitation/confidence, and product impact.

## Diagram selection

- user journey: three swimlanes—用户 / 产品界面 / 系统结果;
- temporal handoffs: `sequenceDiagram`;
- lifecycle: `stateDiagram-v2`;
- entity relations: `erDiagram`;
- full architecture: layered `flowchart` with subgraphs.

For architecture diagrams, use solid lines for confirmed behavior, dashed lines for inference, and distinct color/thick lines for suggested design. Include a legend.

## Validation

Run `scripts/validate_report.py` with the final file. Structural validation does not prove visual rendering. Visually inspect when possible and report limitations honestly.
