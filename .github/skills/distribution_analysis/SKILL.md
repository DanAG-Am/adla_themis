---
name: distribution-analysis
description: Analyze FMCG distribution and store coverage across brands and SKUs. Use for questions about stores selling a product, distribution gaps, store coverage, or SKU presence.
---

# Distribution Analysis

Use this skill for questions involving distribution or store coverage.

## Process

1. Read config/semantic_model.yaml when definitions are required.
2. Identify the requested brand, SKU, store, or customer.
3. Use the repository query layer to calculate distribution.
4. Distinguish between stores selling a SKU and stores where the SKU is absent.
5. Return the result using the repository's defined business logic.

## Implementation

Use:

src/skills/distribution.py

Use the existing query layer rather than recreating the calculations.

For local synthetic analysis:

python -m src.skills.cli --skill distribution --brand "Brand A"

## Output

Return the relevant distribution metrics and explain the result in business terms.

Do not infer distribution definitions that conflict with config/semantic_model.yaml.