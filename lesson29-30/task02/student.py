from human import Human


class Student(Human):
    def hello(self):
        super().hello()
        print(" I'm a student.")

    def work(self):
        print("I can study")


def main():
    h = Human("Trueman")
    st = Student("Alex")
    st.hello()
    h.hello()


if __name__ == "__main__":
    main()
