class Metrics:

    @staticmethod
    def brand_sales(df, brand):

        return (
            df
            .filter(df.brand == brand)
            .groupBy("brand")
            .sum("sales_value")
            .withColumnRenamed("sum(sales_value)", "brand_sales")
        )

    @staticmethod
    def distribution(df):

        return (
            df
            .groupBy("brand", "sku")
            .agg(
                {
                    "store_id": "countDistinct"
                }
            )
        )