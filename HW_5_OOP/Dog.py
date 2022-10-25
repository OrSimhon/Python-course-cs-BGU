from Mammal import Mammal


class Dog(Mammal):
    def __init__(self, nick_name, price, power, type="Dog"):
        super().__init__(nick_name, price, power, type)

    def speak(self):
        return Mammal.speak(self) + " woof woof"

    def win(self):
        return self.speak() + " " + Mammal.win(self)
