class SalesSkill:

    name = "sales"

    description = """
    Analyzes FMCG sales at brand and SKU levels.
    """

    def __init__(self, queries):
        self.queries = queries

    def run(self, brand):

        return self.queries.get_brand_sales(
            brand
        )