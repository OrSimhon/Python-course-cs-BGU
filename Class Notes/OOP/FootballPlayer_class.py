import copy


class FootballPlayer:
    def __init__(self, name, salary, performance):
        self.name = name
        self.salary = salary
        self.performance = performance

    def __repr__(self):
        return f"Name: {self.name}\nSalary: {self.salary}M $\nPerformance: {self.performance}"


class OffencePlayer(FootballPlayer):
    def __init__(self, name, salary, performance):
        FootballPlayer.__init__(self, name, salary, performance)
        self.total_yards = 0

    def __repr__(self):
        res = FootballPlayer.__repr__(self)
        return res + '\n' + f'Total Yards: {self.total_yards}'

    def run_yards(self, yards):
        self.total_yards += yards


class DefencePlayer(FootballPlayer):

    def __init__(self, name, salary, performance):
        FootballPlayer.__init__(self, name, salary, performance)
        self.total_tackles = 0

    def __repr__(self):
        res = FootballPlayer.__repr__(self)
        return res + '\n' + f'Total Tackles: {self.total_tackles}'

    def tackle(self):
        self.total_tackles += 1


class FootballTeam:
    """
    This class represents a Football Team
    """

    def __init__(self, players):
        """
        Constructor
        :param players: list - list of Football players objects
        """
        self.__players = players  # __ makes the players list field to private to the class. Namely, not accessible outside the class

    def get_team(self):
        # return self.__players # makes this var mutable from outside the class
        return copy.deepcopy(self.__players)


p = FootballPlayer('Tom Brady', 20, 7)
pp = OffencePlayer('Tom Brady', 20, 7)
ppp = DefencePlayer('Tom Brady', 20, 7)
ppp.tackle()

print(p, end='\n\n')
print(pp, end='\n\n')
print(ppp, end='\n\n')

team = FootballTeam([DefencePlayer('Janis Griffin', 15, 6.2), OffencePlayer('John Smith', 22, 7)])
team.get_team().append(OffencePlayer('hacker', 1000, 999))
for player in team.get_team():
    print(player.name)
