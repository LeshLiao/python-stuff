from datetime import date
'''
Reference: https://www.youtube.com/watch?v=PIKiHq1O9HQ&ab_channel=Indently
'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self) -> str:
        return f'{self.name} is {self.age} years old.'

    @classmethod
    def age_from_year(cls, name, birth_year):
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

    @staticmethod
    def get_bmp(weight, height):
        return weight / ((height/100)*(height/100))


if __name__ == '__main__':
    john = Person('John', 20)
    print(john.description())

    federico = Person.age_from_year('Federico', 1997)
    print(federico.description())

    print('BMI:' + str(round(Person.get_bmp(75, 179), 2)))
