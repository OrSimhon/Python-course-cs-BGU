from Bird import Bird


class Parrot(Bird):
    def __init__(self, nick_name, price, power, type="Parrot"):
        super().__init__(nick_name, price, power, type)
        self.fly = True

