from Animal import Animal


class Reptiles(Animal):
    def __init__(self, nick_name, price, power, type):
        super().__init__(nick_name, price, power, type)

    def move(self):
        self._set__power(self._get__power() / 2)

    def __ge__(self, other):
        if isinstance(other, Reptiles):
            self.move()
            other.move()
        return Animal.__ge__(self, other)
