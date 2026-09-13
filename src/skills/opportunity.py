from pyspark.sql import functions as F


class OpportunitySkill:

    name = "opportunity"

    description = """
    Identifies FMCG distribution opportunities by finding
    products that are not currently selling in stores and
    estimating their potential value.
    """

    def __init__(self, queries):
        self.queries = queries

    def run(self, brand, top_n=10):

        brand_sales_df = self.queries.get_brand_sales(
            brand
        )

        distribution_df = self.queries.get_distribution(
            brand
        )

        missing_df = self.queries.get_missing_distribution(
            brand
        )

        brand_sales = (
            brand_sales_df
            .collect()[0]["brand_sales"]
        )

        opportunities = (
            missing_df
            .join(
                distribution_df,
                on="sku",
                how="left"
            )
            .withColumn(
                "opportunity_rate",
                1 - F.col("distribution")
            )
            .withColumn(
                "opportunity_value",
                F.lit(brand_sales)
                * F.col("opportunity_rate")
            )
        )

        return (
            opportunities
            .select(
                "brand",
                "sku",
                "customer",
                "store",
                "distribution",
                "opportunity_rate",
                "opportunity_value"
            )
            .orderBy(
                F.col("opportunity_value").desc()
            )
            .limit(top_n)
        )