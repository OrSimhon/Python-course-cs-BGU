from Reptiles import Reptiles


class Snake(Reptiles):
    def __init__(self, nick_name, price, power, type="Snake"):
        super().__init__(nick_name, price, power, type)

    def move(self):
        self._set__power(self._get__power() * 2.5)
