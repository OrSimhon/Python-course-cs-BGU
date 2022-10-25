from Animal import Animal


class Bird(Animal):
    def __init__(self, nick_name, price, power, type):
        super().__init__(nick_name, price, power, type)
        self.fly = False

    def __ge__(self, other):
        if isinstance(other, Bird):
            if other.fly and self.fly:
                return Animal.__ge__(self, other)
            elif other.fly and not self.fly:
                return False
            elif self.fly and not other.fly:
                return True
            else:
                return Animal.__ge__(self, other)
        return Animal.__ge__(self, other)
