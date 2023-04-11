from student import Student
from manager import Manager


def main():
    manager = Manager()
    s1 = Student("Alex", 20, 10)
    s2 = Student("Kate", 18, 9)
    s3 = Student("Peter", 22, 5)

    ls = [s1, s2, "abs",  s3, 5]

    result = manager.calc_avg_mark(ls)

    print(f"Result is {result}.")


if __name__ == "__main__":
    main()
