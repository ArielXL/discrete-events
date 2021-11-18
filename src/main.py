import time
import simpy

from utils import *
from processes import *
from person import Person
from random import randint
from population import Population

class PopulationEvolution:
    def __init__(self, woman, man, years):
        self.woman = woman
        self.man = man
        self.years = years
        self.process = [ pregnat, death, born, break_couple, match ]
        self.enviroment = simpy.Environment()
        self.stats = { 
            PersonStates.DPM: [], 
            PersonStates.BCPM: [], 
            PersonStates.CP: [], 
            PersonStates.AP: [], 
            PersonStates.PPM: [] 
        }
        self.population = Population()
        self.population.generate_population_sex_defined(self.man, self.woman)
        self.enviroment.process(self.run_month())
        start = time.time()
        self.enviroment.run(until=self.years*12)
        end = time.time()
        self.duration = end - start
    
    def count_couples(self):
        count = 0
        for person in self.population:
            if person.get_civil_state() == CivilState.INLOVE:
                count += 1
        return count / 2

    def run_month(self):
        while True:
            self.stats[PersonStates.AP].append((self.enviroment.now, self.population.count()))
            get_older(self.enviroment, self.population, self.stats)
            process_clone = [ p for p in self.process ]
            while len(process_clone) > 0:
                index = randint(0, len(process_clone) - 1)
                process_clone.pop(index)(self.enviroment, self.population, self.stats)
            self.stats[PersonStates.CP].append((self.enviroment.now, self.count_couples()))
            yield self.enviroment.timeout(1)
            print(f'Hay {self.population.count()} habitantes en {self.enviroment.now} meses.')

def main():

    args = Utils.GetArguments()

    women = args.women
    men = args.men
    years = args.years

    population_evolution = PopulationEvolution(women, men, years)
    Utils.BuildDiagram(population_evolution)

if __name__ == '__main__':
    main()
