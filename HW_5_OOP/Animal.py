class Animal:
    def __init__(self, nick_name, price, power, type):
        """
        Animal constructor
        :param nick_name(str): The animal's name
        :param price(float): The price of one unit of this animal.
        :param power:
        :param type:
        """
        self.nick_name = nick_name
        if price < 1 or power < 1 or power > 100:
            raise ValueError("Error in parameter type")
        self.price = float(price)
        self.__power = float(power)
        self.type = type

    def __repr__(self):
        """
        Representation of this class
        :return:
        """
        return f"Name: {self.nick_name}, Price {self.price} NIS, Power: {self.__power}"

    def _get__power(self):
        return float(self.__power)

    def _set__power(self, new_power):
        if 0 < new_power <= 100:
            self.__power = float(new_power)

    def win(self):
        return f"{self.nick_name} winner"

    def loss(self):
        return f"{self.nick_name} loser"

    def __ge__(self, other):
        if isinstance(other, Animal):
            return self._get__power() >= other._get__power()
        raise ValueError("Wrong type")

    def __eq__(self, other):
        if not isinstance(other, Animal):
            return False
        return self.nick_name >= other.nick_name

    def get_type(self):
        return self.type
