class AgentContext:

    def __init__(self, semantic_model, skill_registry):
        self.semantic_model = semantic_model
        self.skill_registry = skill_registry

    def build(self):

        return {
            "dimensions": self.semantic_model.config["dimensions"],
            "measures": self.semantic_model.config["measures"],
            "business_rules": self.semantic_model.config["business_rules"],
            "hierarchies": self.semantic_model.config["hierarchies"],
            "skills": self.skill_registry.list()
        }