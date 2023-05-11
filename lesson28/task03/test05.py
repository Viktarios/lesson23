class Super(object):
    def __init__(self, name = "Alex"):
        self._name = name

    def walk(self):
        print("I can walk.")

    @property
    def name(self):
        return self._name

    @staticmethod
    def smethod():
        print("static method from Super class")


    @classmethod
    def cmethod(cls):
        print("class method from Super class")

class Subclass(Super):
    pass


sub = Subclass("Peter Pan")
sub.walk()
print(sub._name)
print(sub.name)
Subclass.smethod()
sub.smethod()
Subclass.cmethod()