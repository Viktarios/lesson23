class Counter:
    def __init__(self,count=0):
        self.count = count

    def increment(self):
        self.count += 1

    def decrement(self):
        if self.count != 0:
            self.count -= 1

    def resep(self):
        self.count = 0

    def __str__(self):
        return "Counter:" + str(self.count)
