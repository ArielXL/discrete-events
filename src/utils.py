import enum
import argparse
import matplotlib.pyplot as plt

from random_variables import *

class CivilState(enum.Enum):
    '''
    Representa los posibles estados civiles de las personas.
    '''
    SINGLE = 'single',
    INLOVE = 'in love',
    WIDOW = 'widow',
    RECOVER = 'recover',

class PersonStates(enum.Enum):
    '''
    Representa los posibles estados de una persona.
    '''
    DPM = 'death_per_month',
    BCPM = 'born_child_per_month',
    CP = 'couples',
    AP = 'alive_people',
    PPM = 'pregnant_per_month',

class Gender(enum.Enum):
    '''
    Representa los posibles sexos de las personas.
    '''
    MALE = 'male',
    FEMALE = 'female'

class Utils:

    @staticmethod
    def GetArguments():

        parser = argparse.ArgumentParser(description='Run a COOL Compiler.')

        parser.add_argument('-w', '--women', type=int, default=10, 
                        required=False, help='count of women in a population.')
        parser.add_argument('-m', '--men', type=int, default=10, 
                        required=False, help='count of men in a polution.')
        parser.add_argument('-y', '--years', type=int, default=100, 
                        required=False, help='count of years in a simulation.')

        return parser.parse_args()

    @staticmethod
    def GetArraysForDiagram(population_evolution):
        x1 = [ x[0] for x in population_evolution.stats[PersonStates.DPM] ]
        y1 = [ x[1] for x in population_evolution.stats[PersonStates.DPM] ]
        x2 = [ x[0] for x in population_evolution.stats[PersonStates.AP] ]
        y2 = [ x[1] for x in population_evolution.stats[PersonStates.AP] ]
        
        acum,y3 = 0,[]
        for w in y1:
            acum += w
            y3.append(acum)
        
        x4 = [ x[0] for x in population_evolution.stats[PersonStates.CP] ]
        y4 = [ x[1] for x in population_evolution.stats[PersonStates.CP] ]
        x5 = [ x[0] for x in population_evolution.stats[PersonStates.BCPM] ]
        y5 = [ x[1] for x in population_evolution.stats[PersonStates.BCPM] ]
        x6 = [ x[0] for x in population_evolution.stats[PersonStates.PPM] ]
        y6 = [ x[1] for x in population_evolution.stats[PersonStates.PPM] ]
        
        acum,y7 = 0,[]
        for w in y5:
            acum += w
            y7.append(acum)
        
        return x1, y1, x2, y2, y3, x4, y4, x5, y5, x6, y6, y7

    @staticmethod
    def BuildDiagram(population_evolution):
        x1, y1, x2, y2, y3, x4, y4, x5, y5, x6, y6, y7 = Utils.GetArraysForDiagram(population_evolution)

        plt.plot(x1, y1, x2, y2, x1, y3, x4, y4, x5, y5, x5, y7)
        plt.legend(['muertes por mes', 'personas vivas', 'total de muertos', 'parejas por mes', 'nacidos por mes', 'total de nacimientos'])
        print(f'Duración: {population_evolution.duration} segundos.')
        plt.show()

class Probabilities:

    BREAK_PROB = 0.2

    @staticmethod
    def SonNumberProbability(n):
        '''
        Probabilidad que cada persona desea tener 
        segun el numero de hijos.
        '''
        if n == 1:
            return 0.6
        elif n == 2:
            return 0.75
        elif n == 3:
            return 0.35
        elif n == 4:
            return 0.2
        elif n == 5:
            return 0.1
        else:
            return 0.05

    @staticmethod
    def DeathProbability(age, sex):
        '''
        Probabilidad que una persona fallezca 
        segun la edad y el sexo.
        '''
        if age < 0 or not sex in [ Gender.MALE, Gender.FEMALE ]:
            return Exception("Invalid person")
        elif age <= 12:
            if sex == Gender.MALE:
                return 0.25 / (12 * 12)
            else:
                return 0.25 / (12 * 12)
        elif age <= 45:
            if sex == Gender.MALE:
                return 0.1 / (12 * 33)
            else:
                return 0.15 / (12 * 33)
        elif age <= 76:
            if sex == Gender.MALE:
                return 0.3 / (12 * 31)
            else:
                return 0.35 / (12 * 31)
        elif age <= 125: 
            if sex == Gender.MALE:
                return 0.7 / (12 * 49)
            else:
                return 0.75 / (12 * 49)
        else:
            return 1

    @staticmethod
    def PregnatProbability(age):
        '''
        Probabilidad de que una mujer quede 
        embarazada segun la edad.
        '''
        if age < 12:
            return 0
        elif age < 15:
            return 0.2 / 3
        elif age < 21:
            return 0.45 / 6
        elif age < 35:
            return 0.8 / 14
        elif age < 45:
            return 0.4 / 10
        elif age < 60:
            return 0.2 / 15
        elif age < 125:
            return 0.05 / 65
        else:
            return 0

    @staticmethod
    def WantPartnerProbability(age):
        '''
        Probabilidad de que una persona quiera 
        encontrar una pareja segun la edad.
        '''
        if  age < 12:
            return 0
        elif age < 15:
            return 0.6
        elif age < 21:
            return 0.65
        elif age < 35:
            return 0.8
        elif age < 45:
            return 0.6
        elif age < 60:
            return 0.5
        elif age < 125:
            return 0.2
        else:
            return 0

    @staticmethod
    def CoupleProbability(age1, age2):
        '''
        Probabilidad de que dos personas de diferentes 
        sexos quieran establecer una pareja segun la 
        diferencia de edad.
        '''
        diff = abs(age1 - age2)
        if diff < 5:
            return 0.45
        elif diff < 10:
            return 0.4
        elif diff < 15:
            return 0.35
        elif diff < 20:
            return 0.25
        else:
            return 0.15

    @staticmethod
    def GetTimeRecoverProbability(age):
        '''
        Probabilidad que una persona necesita estar 
        sola por un periodo de tiempo segun la edad.
        '''
        if age < 12:
            return 0
        elif age < 15:
            return RandomVariables.GetExponential(1 / 3)
        elif age < 35:
            return RandomVariables.GetExponential(1 / 6)
        elif age < 45:
            return RandomVariables.GetExponential(1 / 12)
        elif age < 60:
            return RandomVariables.GetExponential(1 / 24)
        else:
            return RandomVariables.GetExponential(1 / 48)
