from Mammal import Mammal


class Cat(Mammal):
    def __init__(self, nick_name, price, power, type='Cat'):
        super().__init__(nick_name, price, power, type)

    def speak(self):
        return f"{self.nick_name} says meow"
