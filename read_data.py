# MARK:- libs
import pandas as pd 
import re
from pandas import ExcelWriter
from pandas import ExcelFile
from case import Case

pd.options.mode.chained_assignment = None 

# MARK:- get discrete data

df = pd.read_excel('source.xlsx')

ids = df['id']
dates = df['date']
legal_relas = df['legal_rela']
plaintiff_ages = df['plaintiff_age']
defendant_ages = df['defendant_age']
decisions = df['decision']

length = len(legal_relas) - 1

for i in range(0, length):
    relation = legal_relas[i]
    decision = decisions[i]
    
    corr_legal = re.search(r'\d', relation)
    corr_decis = re.search(r'\d', decision)

    legal_relas[i] = corr_legal.group()
    decisions[i] = corr_decis.group()


# MARK:- create list objects

cases = []

for i in range(0, length):
    case = Case(ids[i], legal_relas[i], plaintiff_ages[i],defendant_ages[i], decisions[i])
    cases.append(case)

# MARK:- write to file
file = open("cases.arff", "w")

for case in cases:
    file.write(case.toString())

file.close()