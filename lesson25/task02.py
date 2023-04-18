# students = ["Alex", "Peter", "Victor",
#             "Anna", "Kate", "Vladimir", "Nikita"]
#
# marks = [10, 9, 7, 8, 8, 10, 8]

# index = students.index("Victor")
# print(marks[index])

dictionary = {"Alex": 10, "Peter": 9, "Victor": 7,
              "Anna": 8, "Kate": 8, "Vladimir": 10, "Nikita": 8}

print(dictionary["Anna"])
# print(dictionary["Alice"])
print(dictionary.get("Alice"))