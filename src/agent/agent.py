class FMCGAgent:

    def __init__(self, router):

        self.router = router

    def answer(self, question):

        intent = self.router.route(question)

        skill = self.router.skills[intent.skill]

        result = skill.run(
            brand=intent.brand
        )

        return {
            "intent": intent,
            "result": result
        }