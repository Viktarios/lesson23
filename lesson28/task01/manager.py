from human import Human


class Manager:
    @staticmethod
    def count_adult(humans):
        count = 0
        if isinstance(humans, (list, tuple)):
            for human in humans:
                if isinstance(human, Human) and human.age >= 18:
                    count += 1

            return count

    @staticmethod
    def count_underage(humans):
        total = len(humans)
        total -= Manager.count_adult(humans)
        return total
