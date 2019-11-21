# MARK:- libs
import pandas as pd
import re
from pandas import ExcelWriter
from pandas import ExcelFile
from random import seed
from random import randint
from random import choice
from case import Case


# MARK:- support functions
def new_case_one():
    """
        output.append(str(self.legal_rela))
        output.append(str(self.has_child))
        output.append(str(self.plaintiff_age))
        output.append(str(self.defendant_age))
        output.append(str(self.age_dist))
        output.append(str(self.decision))
    """

    legal_rela = choice([4, 5, 7])
    age_dist = 1
    decision = 2
    plaintiff_age = randint(23, 53)
    defendant_age = plaintiff_age + randint(1, 5)

    case = Case(1000, legal_rela, plaintiff_age, defendant_age, decision)
    case.has_child = randint(0,1)
    return case


def new_case_two():
    legal_rela = choice([1, 8])
    age_dist = 2
    decision = 2
    plaintiff_age = randint(25, 53)
    defendant_age = plaintiff_age + randint(6, 10)

    case = Case(1000, legal_rela, plaintiff_age, defendant_age, decision)
    return case

def new_case_three():
    legal_rela = choice([2,3])
    age_dist = 2
    decision = 2
    plaintiff_age = randint(25, 53)
    defendant_age = plaintiff_age + randint(6, 10)

    case = Case(1000, legal_rela, plaintiff_age, defendant_age, decision)
    return case


# MARK:- write to file
file = open("cases.arff", "a")
seed(1)
# generate some random numbers
for _ in range(10):
    case = new_case_one()
    file.write(case.toString())

for _ in range(30):
    case = new_case_two()
    file.write(case.toString())

for _ in range(30):
    case = new_case_one()
    file.write(case.toString())

for _ in range(10):
    case = new_case_two()
    file.write(case.toString())

for _ in range(50):
    case = new_case_three()
    file.write(case.toString())

file.close()

