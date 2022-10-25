from abc import ABC, abstractmethod


class FootballPlayer(ABC):

    def __init__(self, name, salary, performance):
        self.name = name
        self.salary = salary
        self.performance = performance

    @abstractmethod
    def play(self):
        pass

    def __repr__(self):
        return f"Name: {self.name}\nSalary: {self.salary}M $\nPerformance: {self.performance}"


class OffencePlayer(FootballPlayer):
    def __init__(self, name, salary, performance):
        super().__init__(name, salary, performance)
        self.total_yards = 0

    def play(self, yards):
        self.total_yards += yards

    def __repr__(self):
        res = FootballPlayer.__repr__(self)
        # res = super().__repr__()
        return res + '\n' + f'Total Yards: {self.total_yards}'


class DefencePlayer(FootballPlayer):

    def __init__(self, name, salary, performance):
        super().__init__(name, salary, performance)
        self.total_tackles = 0

    def play(self):
        self.total_tackles += 1

    def __repr__(self):
        res = FootballPlayer.__repr__(self)
        # res = super().__repr__() # Same
        return res + '\n' + f'Total Tackles: {self.total_tackles}'


# player = FootballPlayer('a', 1, 1) # Error - because cant create an object of abstract class
off_player = OffencePlayer('Player1', 3, 9.7)
def_player = DefencePlayer('Player2', 2, 6.3)

off_player.play(5)
off_player.play(10)

def_player.play()
def_player.play()

print(off_player)
print(20 * "=")
print(def_player)
