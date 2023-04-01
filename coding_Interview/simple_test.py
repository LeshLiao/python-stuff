from inheritance import Andy


class MyClass:
    def __init__(self, value):
        self.value = value


if __name__ == "__main__":
    my_class = MyClass(1)

    person = Andy(222)
    person.get_details()
