from semantic.model import SemanticModel


def test_semantic_model():

    model = SemanticModel(
        "config/semantic_model.yaml"
    )

    metric = model.get_measure(
        "sales_value"
    )

    assert metric is not None

    assert (
        metric["expression"]
        == "SUM(sales_value)"
    )


def test_business_rule():

    model = SemanticModel(
        "config/semantic_model.yaml"
    )

    rule = model.get_business_rule(
        "opportunity"
    )

    assert rule is not None

    assert (
        rule["condition"]
        == "sales_value = 0"
    )