from src.data.generate_data import create_spark
from src.data.generate_data import create_sales

from src.data.queries import FMCGQueries

from src.skills.registry import SkillRegistry

from src.agent.router import SkillRouter
from src.agent.agent import FMCGAgent


def main():

    spark = create_spark()

    sales = create_sales(spark)

    queries = FMCGQueries(sales)

    registry = SkillRegistry(
        queries
    )

    router = SkillRouter(
        registry.skills
    )

    agent = FMCGAgent(
        router
    )

    print("\nFMCG AI Agent")
    print("=" * 40)

    question = input(
        "\nAsk an FMCG business question:\n> "
    )

    response = agent.answer(
        question
    )

    intent = response["intent"]

    print("\nAgent intent")
    print("=" * 40)

    print(
        f"Skill: {intent.skill}"
    )

    print(
        f"Brand: {intent.brand}"
    )

    print(
        f"Dimensions: {intent.dimensions}"
    )

    print("\nResult")
    print("=" * 40)

    response["result"].show(
        truncate=False
    )

    spark.stop()


if __name__ == "__main__":
    main()