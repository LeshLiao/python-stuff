class Ship:
    """this is a Ship class"""
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if ((self.draft - self.crew * 1.5) > 20):
          return True
        return False

Titanic = Ship(15, 10)
Titanic.is_worth_it()

A = Ship(0, 0)
print(A.is_worth_it())

B = Ship(15, 20)
print(B.is_worth_it())

C = Ship(100,20)
print(C.is_worth_it())

D = Ship(35, 20)
print(D.is_worth_it())