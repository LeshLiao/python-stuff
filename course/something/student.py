class Student:
  name = ''
  birthday = ''
  # Has_Ink = True
  def __init__ (self, name, birthday='idk'):
    self.name = name
    self.birthday = birthday

  def register(self, name, birthday):
    self.name = name
    self.birthday = birthday
    # print("You drew a " + self.color + " art piece")

  def introduction(self):
    if self.name == "" or self.birthday == "":
      print(f"Hi everyone!")
    else:
      print(f"Hi I am {self.name} and I was born on {self.birthday}")

studentA = Student('Thomas', "Oct 1st")
# studentA.register('Thomas', "Oct 1st")
# studentA.introduction()

studentB = Student('Elon musk')
# studentB.introduction()

all_stu = [studentA, studentB]

for student in all_stu:
  student.introduction()