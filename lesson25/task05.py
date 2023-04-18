students = {"Alex": 10, "Peter": 9, "Victor": 7,
            "Anna": 8, "Kate": 8, "Vladimir": 10, "Nikita": 8}
print("Before: ", students)
students.setdefault("Alice", 7)
print("After: ", students)
