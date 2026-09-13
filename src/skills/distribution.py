class DistributionSkill:

    name = "distribution"

    description = """
    Analyzes FMCG distribution and identifies products
    with high or low store coverage.
    """

    def __init__(self, queries):
        self.queries = queries

    def run(self, brand):

        return self.queries.get_distribution(
            brand
        )