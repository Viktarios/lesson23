from student import Student
from student import init


def main():

    st1 = Student()
    st2 = Student()

    # init(st1, "Alex", 20, 10)
    # init(st2, "Kate", 18, 8)

    # print(st1.name)
    # print(getattr(st1, "name"))

    # print(vars(st1))
    # print (st1.__dict__)
    # print(help(st1))
    # print(dir(st1))
    # print(st1.__getattribute__("name"))

    # del st1.name
    # delattr(st1,"mark")
    # st1.__delattr__("age")

    # st1.name = "Alex"
    # setattr(st1, "name ", "Peter")
    # st1.__setattr__("name", "Olya")
    #
    print(vars(st1))
    print(vars(st2))


if __name__ == "__main__":
    main()
