from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def power_on(self):
        pass
    def power_off(self):
        pass

class Acer(Command):
    def power_on(self):
        print("Acer on \r\n")
    def power_off(self):
        print("Acer off\r\n")

class MSI(Command):
    def power_on(self):
        print('MSI on')
    def power_off(self):
        print('MSI off')


value = 1
myCmd = Acer()

if value == 1:
    myCmd = MSI()

myCmd.power_on()
myCmd.power_off()