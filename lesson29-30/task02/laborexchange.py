from human import Human

class LaborExchange:
    @staticmethod
    def execute(humans):
        if isinstance(humans,(list,tuple)):
            for human in humans:
                if isinstance(human,Human):
                    human.hello()
                    human.work()