class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    def is_worth_it(self):
        if ((self.draft - self.crew * 1.5) > 20):
          return True
        return False

# Titanic = Ship(15, 10)
# Titanic.is_worth_it()

# A = Ship(0, 0)
# print(A.is_worth_it())

# B = Ship(15, 20)
# print(B.is_worth_it())

# C = Ship(100,20)
# print(C.is_worth_it())

# D = Ship(35, 20)
# print(D.is_worth_it())


from solution import Ship
import codewars_test as test

@test.describe('sample tests')
def sample_tests():

    @test.it('empty ship (draft: 0, crew: 0)')
    def empty_ship():
        empty_ship = Ship(0, 0)
        test.assert_equals(empty_ship.is_worth_it(), False)

    @test.it('medium boat (draft: 15, crew: 20)')
    def boat():
        boat = Ship(15, 20)
        test.assert_equals(boat.is_worth_it(), False)

    @test.it("A worthy ship (draft: 100, crew: 20)")
    def worthy_ship():
        worthy_ship = Ship(100,20);
        test.assert_equals(worthy_ship.is_worth_it(), True)

    @test.it('big boat (draft: 35, crew: 20)')
    def big_boat():
        big_boat = Ship(35, 20)
        test.assert_equals(big_boat.is_worth_it(), False)
