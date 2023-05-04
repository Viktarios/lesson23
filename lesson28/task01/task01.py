from human import Human
from human_creator import HumanCreator
from manager import  Manager
ls = HumanCreator.create()

for human in ls:
    print(human)

adult = Manager.count_adult(ls)
underage = Manager.count_underage(ls)

print(f"Adult - {adult}")
print(F"Underage - {underage}")