from doctor import Doctor
from president import President
from student import Student
from worker import Worker


def main():
    doc = Doctor("Watson", 55, True,  45)
    student = Student("Alex", 20, True,  10)
    president = President("Trueman", 60, True,  99)
    worker = Worker("Eve", 35, True,  2500)

    print(doc)
    doc.can_cure()
    print(president)
    president.can_run()
    print(worker)
    worker.can_work()
    print(student)
    student.can_study()


if __name__ == "__main__":
    main()
