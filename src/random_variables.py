from math import log
from random import random

class RandomVariables:

    @staticmethod
    def GetExponential(c):
        u = random()
        return -c * log(u)

    @staticmethod
    def GetUniform(a=0, b=1):
        return (b - a) * random() + a
