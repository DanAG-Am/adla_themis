class BusinessRules:
    '''
    This class contains static methods for various business rules. These are very simple, 
    for a real use case you should consider the usage of certain time periods, more
    sophisticated validation, and other business logic considerations.
    '''
    @staticmethod
    def is_missing_distribution(sales_value):
        return sales_value <= 0

    @staticmethod
    def calculate_opportunity(brand_sales, opportunity_rate):
        return brand_sales * opportunity_rate

    @staticmethod
    def rank_opportunities(df):
        return df.orderBy(
            df.opportunity_value.desc()
        )