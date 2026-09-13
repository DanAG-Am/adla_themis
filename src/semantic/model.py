import yaml


class SemanticModel:

    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as file:
            self.config = yaml.safe_load(file)

    def get_measure(self, name):
        return self.config["measures"].get(name)

    def get_business_rule(self, name):
        return self.config["business_rules"].get(name)

    def get_hierarchy(self, name):
        return self.config["hierarchies"].get(name)

    def get_dimensions(self):
        return self.config["dimensions"]

    def list_measures(self):
        return list(self.config["measures"].keys())