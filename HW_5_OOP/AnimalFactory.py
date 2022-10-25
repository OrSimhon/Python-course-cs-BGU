class AnimalFactory(object):

    @staticmethod
    def create(type_animal, nick_name, price, power):
        if type_animal == "Dog":
            from Dog import Dog
            print("Dog created")
            return Dog(nick_name, price, power)
        elif type_animal == "Cat":
            from Cat import Cat
            print("Cat created")
            return Cat(nick_name, price, power)
        elif type_animal == "Parrot":
            from Parrot import Parrot
            print("Parrot created")
            return Parrot(nick_name, price, power)
        elif type_animal == "Snake":
            from Snake import Snake
            print("Snake created")
            return Snake(nick_name, price, power)
        elif type_animal == "Turtle":
            from Turtle import Turtle
            print("Turtle created")
            return Turtle(nick_name, price, power)
        return None
