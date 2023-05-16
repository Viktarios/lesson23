class Human:
    def __init__(self, name="no name"):
        self.name = name

    def __str__(self):
        return self.name

    def hello(self):
        print(f"Hello! I'm {self.name}", end='')
