import argparse

from src.data.generate_data import create_spark
from src.data.queries import FMCGQueries
from src.skills.opportunity import OpportunitySkill
from src.skills.distribution import DistributionSkill
from src.skills.sales import SalesSkill
from src.skills.registry import SkillRegistry


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--skill", choices=["opportunity", "distribution", "sales"], required=True)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--limit", type=int, default=10)

    args = parser.parse_args()

    spark = create_spark()
    queries = FMCGQueries(spark)

    registry = SkillRegistry()

    registry.register("opportunity", OpportunitySkill(queries))
    registry.register("distribution", DistributionSkill(queries))
    registry.register("sales", SalesSkill(queries))

    skill = registry.get(args.skill)

    if args.skill == "opportunity":
        result = skill.run(args.brand, args.limit)
    else:
        result = skill.run(args.brand)

    if hasattr(result, "show"):
        result.show(truncate=False)
    else:
        print(result)

    spark.stop()


if __name__ == "__main__":
    main()