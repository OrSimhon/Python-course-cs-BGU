from functools import reduce


class Plant:
    def __init__(self, name, aesthetics=1, water_consumption_month=1, average_month_yield=1, seasonal=False):
        self.name = name
        self.aesthetics = aesthetics
        self.water_consumption_month = water_consumption_month
        self.average_month_yield = average_month_yield
        self.seasonal = seasonal

    def get_maintenance_cost(self, func1):
        return func1(self)

    def purchase_decision(self, func1, func2):
        return func1(self, func2(self))

    def __repr__(self):
        return "name={}".format(self.name)
        # return "water consumption = {0}".format(self.water_consumption_month)


class GardenManager:
    def __init__(self, plants_in_garden):
        self.plants_in_garden = plants_in_garden

    def action(self, func1):
        return func1(self)


"""
PART A - Lambda functions
"""

# Q1
get_cost_lmbd = lambda plant: plant.water_consumption_month

# Q2
get_yearly_cost_lmbd = lambda plant: plant.water_consumption_month * 6 if plant.seasonal else 12

# Q3
worth_investing_lmbd = lambda plant: plant.average_month_yield > plant.water_consumption_month

# Q4
declare_purchase_lmbda = lambda plant, worth: f"{plant.name}:{'yes' if worth else 'no'}"

# Q5
get_plants_names_lmbd = lambda gardenManager: sorted([plant.name for plant in gardenManager.plants_in_garden])

"""
PART B - High order functions
map, filter, reduce
"""


# Q1 - filter
def retrospect(garden_manager):
    return list(map(lambda x: x.name, filter(lambda x: x.average_month_yield > x.water_consumption_month, garden_manager.plants_in_garden)))


# Q2 - reduce
def get_total_yearly_cost(garden_manager):
    return reduce(lambda x, y: x + y.water_consumption_month * 6 if y.seasonal else 12, garden_manager.plants_in_garden, 0)


# Q3 - map
def get_aesthetics(garden_manager):
    return list(map(lambda plant: plant.aesthetics, garden_manager.plants_in_garden))


"""
PART C - Queue
"""


class GateLine:
    def __init__(self, max_capacity):
        self.maximum_allowed_capacity = max_capacity
        self.priority_line = []
        self.regular_line = []

    def new_in_line(self, student_id, priority_id_holder):
        if priority_id_holder:
            while len(self.priority_line) + len(self.regular_line) >= self.maximum_allowed_capacity:
                if len(self.regular_line) == 0:
                    break
                self.regular_line = self.regular_line[:-1]
            self.priority_line.append(student_id)
        elif len(self.priority_line) + len(self.regular_line) < self.maximum_allowed_capacity:
            self.regular_line.append(student_id)

    def open_gate(self):
        entered_students_id = ""
        if len(self.priority_line) > 0:
            temp = self.priority_line[0]
            self.priority_line.remove(temp)
            entered_students_id += temp
        elif len(self.regular_line) > 0:
            temp = self.regular_line[0]
            self.regular_line.remove(temp)
            entered_students_id = temp
        return entered_students_id if entered_students_id != "" else None

    def is_empty(self):
        return len(self.regular_line) + len(self.priority_line) == 0

    def show_who_is_in_line(self):
        current_line_to_gate = list()
        regular_line_copy = self.regular_line.copy()
        priority_line_copy = self.priority_line.copy()
        for prioritized_stud in priority_line_copy:
            current_line_to_gate.append(prioritized_stud)
        for reg_stud in regular_line_copy:
            current_line_to_gate.append(reg_stud)
        return current_line_to_gate
