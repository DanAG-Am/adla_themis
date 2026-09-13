from skills.opportunity import OpportunitySkill
from skills.distribution import DistributionSkill
from skills.sales import SalesSkill


class SkillRegistry:

    def __init__(self, queries):
        self.skills = {
            "opportunity": OpportunitySkill(queries),
            "distribution": DistributionSkill(queries),
            "sales": SalesSkill(queries)
        }

    def get(self, name):
        return self.skills.get(name)

    def list(self):
        return {
            name: {
                "name": skill.name,
                "description": skill.description
            }
            for name, skill in self.skills.items()
        }