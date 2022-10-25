from Animal import Animal
from AnimalFactory import AnimalFactory


class Shop:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.__animal_list = dict()

    def get_name(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Animal):
            return self.add_animal(other)
        else:
            return self.add_multiple_items(other)

    def add_animal(self, animal):
        if self.balance > animal.price:
            self.__animal_list[animal.nick_name] = animal
            self.balance -= animal.price
            return 1
        return 0

    def add_multiple_items(self, animals):
        animals.sort(key=lambda x: x.price)
        number_add = 0
        for animal in animals:
            if self.add_animal(animal):
                number_add += 1
            else:
                break
        return number_add

    def get__animals(self):
        dic_return = dict()
        for key in self.__animal_list.keys():
            animal = AnimalFactory.create(self.__animal_list[key].get_type(), self.__animal_list[key].nick_name,
                                          self.__animal_list[key].price, self.__animal_list[key]._get__power())
            dic_return[key] = animal
        return dic_return

    def sell(self, nickname):
        if nickname in self.__animal_list:
            self.balance += self.__animal_list[nickname].price
            return self.__animal_list.pop(nickname)
        return None

    def num_of_animals(self):
        return len(self.__animal_list)

    def play(self, animal1, animal2):
        if animal1 in self.__animal_list and animal2 in self.__animal_list:
            if self.__animal_list[animal1].__ge__(self.__animal_list[animal2]):
                return self.__animal_list[animal1].win() + '\n' + self.__animal_list[animal2].loss()
            else:
                return self.__animal_list[animal2].win() + '\n' + self.__animal_list[animal1].loss()
        else:
            return False
