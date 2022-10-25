from Animal import Animal


class Mammal(Animal):
    def __init__(self, nick_name, price, power, type):
        super().__init__(nick_name, price, power, type)

    def speak(self):
        return f"{self.nick_name} says"
