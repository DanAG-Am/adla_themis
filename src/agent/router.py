from agent.intent import AgentIntent


class SkillRouter:

    def __init__(self, skills):
        self.skills = skills

    def route(self, question):

        question_lower = question.lower()

        if any(
            word in question_lower
            for word in [
                "opportunity",
                "opportunities",
                "untapped",
                "potential"
            ]
        ):
            skill = "opportunity"

        elif any(
            word in question_lower
            for word in [
                "distribution",
                "coverage",
                "stores"
            ]
        ):
            skill = "distribution"

        elif any(
            word in question_lower
            for word in [
                "sales",
                "revenue",
                "sell out"
            ]
        ):
            skill = "sales"

        else:
            raise ValueError(
                "Unable to determine analytical skill."
            )

        brand = self._extract_brand(question)

        dimensions = self._extract_dimensions(
            question
        )

        return AgentIntent(
            skill=skill,
            brand=brand,
            dimensions=dimensions
        )

    def _extract_brand(self, question):

        words = question.split()

        for index, word in enumerate(words):

            if word.lower() == "brand" and index + 1 < len(words):

                return f"Brand {words[index + 1].strip(',.?!')}"

        return "Brand A"

    def _extract_dimensions(self, question):

        question = question.lower()

        dimensions = []

        if "customer" in question:
            dimensions.append("customer")

        if "store" in question:
            dimensions.append("store")

        if "sku" in question:
            dimensions.append("sku")

        if "brand" in question:
            dimensions.append("brand")

        return dimensions