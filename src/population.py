from person import Men, Women
from random_variables import RandomVariables

class Population:

    def __init__(self):
        self.id = 1
        self.death = []
        self.persons = []
        self.new_death = []

    def count(self):
        count_person_alive = 0
        for person in self.persons:
            if person.is_alive():
                count_person_alive += 1
        return count_person_alive

    def generate_population(self, n):
        for _ in range(n):
            age = RandomVariables.GetUniform(1, 100 * 12) // 1
            sex = RandomVariables.GetUniform()
            if sex < 0.5:
                self.persons.append(Men(self.id, age=age))
                self.id += 1
            else:
                self.persons.append(Women(self.id, age=age))
                self.id += 1

    def generate_population_sex_defined(self, men, women):
        for _ in range(men):
            age = RandomVariables.GetUniform(1, 100 * 12) // 1
            self.persons.append(Men(self.id, age=age))
            self.id += 1
        for _ in range(women):
            age = RandomVariables.GetUniform(1, 100 * 12) // 1
            self.persons.append(Women(self.id, age=age))
            self.id += 1

    def add_person(self):
        uniform = RandomVariables.GetUniform()
        if uniform < 0.5:
            self.persons.append(Men(self.id))
            self.id += 1
        else:
            self.persons.append(Women(self.id))
            self.id += 1

    def __iter__(self):
        self.index = 0
        self.new_death = []
        return self
    
    def __next__(self):
        while True:
            if self.index == len(self.persons):
                for dp in self.new_death[::-1]:
                    self.death.append(self.persons.pop(dp))
                raise StopIteration
            person = self.persons[self.index]
            if not person.is_alive():
                self.new_death.append(self.index)
            self.index += 1
            if person.is_alive():
                return person

