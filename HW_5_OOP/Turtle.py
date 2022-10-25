from Reptiles import Reptiles


class Turtle(Reptiles):
    def __init__(self, nick_name, price, power, type="Turtle"):
        super().__init__(nick_name, price, power, type)

    def loss(self):
        return Reptiles.loss(self) + " I always lose"
