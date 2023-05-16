from human import Human

class Doctor(Human):
    def hello(self):
        super().hello()
        print(" I'm a good doctor!")
