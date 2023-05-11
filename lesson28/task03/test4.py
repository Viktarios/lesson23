class Super:
    def walk(self):
        print("I can walk.")


class Subclass(Super):
    pass


base = Super()
sub = Subclass()

print(f"Is Subclass Super? - {issubclass(Subclass, Super)}")
print(f"Is Super Subclass? - {issubclass(Super, Subclass)}")
print(f"Is Super object? - {issubclass(Super, object)}")
print(f"Is Subclass object? - {issubclass(Super,object)}")