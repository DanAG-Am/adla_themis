---
name: sales-analysis
description: Analyze FMCG sales performance by brand, SKU, store, or customer. Use for sales questions, brand comparisons, SKU performance, or sales contribution.
---

# Sales Analysis

Use this skill for questions about FMCG sales performance.

## Process

1. Read config/semantic_model.yaml when metric definitions are required.
2. Identify the requested brand, SKU, store, or customer.
3. Use the repository query layer.
4. Calculate the requested sales metric.
5. Compare entities when requested.
6. Explain the business implication.

## Implementation

Use:

src/skills/sales.py

For local synthetic analysis:

python -m src.skills.cli --skill sales --brand "Brand A"

Do not manually redefine the sales metric when the semantic model already contains its definition.

## Output

Return the requested sales metrics followed by a concise business interpretation.