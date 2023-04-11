class Student:

    def __init__(self):
        # print("calling default-constructor")
        self.name = "no name"
        self.age = 16
        self.mark = 4

    def init(st, name, age, mark):
        st.name = name
        st.age = age
        st.mark = mark


def init(st, name, age, mark):
    st.name = name
    st.age = age
    st.mark = mark
