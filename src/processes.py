import simpy

from utils import *
from random_variables import RandomVariables

def get_older(env, pop, stats):
    for p in pop:
        p.get_older()

def death(env, pop, stats):
    death_people = 0
    for p in pop:
        u = RandomVariables.GetUniform()
        if u < Probabilities.DeathProbability(p.get_years(), p.get_sex()):
            if p.get_civil_state() == CivilState.INLOVE:
                p.partner.start_widow(Probabilities.GetTimeRecoverProbability(p.partner.get_years()))
            p.die()
            death_people += 1
                
    stats[PersonStates.DPM].append((env.now, death_people))

def pregnat(env, pop, stats):
    total = 0
    for p in pop:
        if p.get_sex() != Gender.FEMALE:
            continue
        if p.is_pregnat():
            continue
        if p.get_civil_state() != CivilState.INLOVE:
            continue
        if p.get_sons() >= p.get_max_sons():
            continue
        u = RandomVariables.GetUniform()
        if u < Probabilities.PregnatProbability(p.get_years()):
            total += 1
            p.start_pregnat(env.now)
    stats[PersonStates.PPM].append((env.now, total))

def match(env, pop, stats):
    man = [ p for p in pop 
                if p.get_sex() == Gender.MALE and 
                    p.get_civil_state() == CivilState.SINGLE ]
    woman = [ p for p in pop if p.get_sex() == Gender.FEMALE and 
                p.get_civil_state() == CivilState.SINGLE and 
                    RandomVariables.GetUniform() < Probabilities.WantPartnerProbability(p.get_years()) ]
    for m in man:
        u = RandomVariables.GetUniform()
        if u > Probabilities.WantPartnerProbability(m.get_years()):
            continue
        for w in woman:
            if w.get_civil_state() != CivilState.SINGLE:
                continue
            u = RandomVariables.GetUniform()
            if u < Probabilities.CoupleProbability(m.get_years(), w.get_years()):
                m.add_partner(w)
                w.add_partner(m)
                break
    
def break_couple(env, pop, stats):
    for p in pop:
        if p.get_sex() != Gender.MALE:
            continue
        if p.get_civil_state() != CivilState.INLOVE:
            continue
        u = RandomVariables.GetUniform()
        if u < Probabilities.BREAK_PROB:
            p.partner.start_recover(Probabilities.GetTimeRecoverProbability(p.partner.get_years()))
            p.break_with_partner()
            p.start_recover(Probabilities.GetTimeRecoverProbability(p.get_years()))

def born(env, pop, stats):
    total = 0
    for p in pop:
        if p.get_sex() != Gender.FEMALE:
            continue
        if not p.is_pregnat():
            continue
        if not p.born_time(env.now):
            continue
        p.end_pregnat()
        u = RandomVariables.GetUniform()
        
        for i in range(number_of_childs(u)):
            total +=1
            p.add_son()
            p.actual_father.add_son()
            pop.add_person()
    stats[PersonStates.BCPM].append((env.now, total))

def number_of_childs(p):
    if p < 0.02:
        return 5
    if p < 0.06:
        return 4
    if p < 0.14:
        return 3
    if p < 0.32:
        return 2
    return 1
