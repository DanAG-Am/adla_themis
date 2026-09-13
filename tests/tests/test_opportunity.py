from semantic.business_rules import BusinessRules


def test_opportunity_calculation():

    brand_sales = 100000
    opportunity_rate = 0.20

    result = BusinessRules.calculate_opportunity(
        brand_sales,
        opportunity_rate
    )

    assert result == 20000