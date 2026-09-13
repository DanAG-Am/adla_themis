---
name: opportunity-analysis
description: Analyze FMCG distribution opportunities by identifying products that are not sold in relevant stores and estimating their potential sales opportunity. Use for opportunity, distribution gap, whitespace, prioritization, or opportunity sizing questions.
---

# Opportunity Analysis

Use this skill when the user asks which products, brands, or SKUs represent the largest distribution opportunities.

The analysis must use the repository semantic model and business rules.

## Process

1. Read config/semantic_model.yaml when metric or dimension definitions are required.
2. Identify the requested brand.
3. Identify the relevant store and product dimensions.
4. Determine which products are not currently sold in the relevant stores.
5. Calculate the opportunity using the repository's opportunity implementation.
6. Rank opportunities from highest to lowest.
7. Return the requested number of opportunities.

## Business logic

An opportunity exists when a relevant SKU has zero or missing sales in a store where the business rules indicate that the SKU should have distribution.

Opportunity value is based on the repository's defined sales and salience metrics.

Do not create alternative definitions of opportunity if the semantic model already defines one.

## Implementation

Use the Python implementation in:

src/skills/opportunity.py

Use the repository's existing data and query layer instead of creating a separate calculation.

For local synthetic analysis, use the repository's CLI when available.

Example:

python -m src.skills.cli --skill opportunity --brand "Brand A" --limit 10

## Output

Return:

- Brand
- SKU
- Store or customer
- Current distribution status
- Opportunity value
- Ranking

Explain the largest opportunities in business language.