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

distances = []

for i in range(0, length):
    relation = legal_relas[i]
    decision = decisions[i]
    
    corr_legal = re.search(r'\d', relation)
    corr_decis = re.search(r'\d', decision)

    legal_relas[i] = corr_legal.group()
    decisions[i] = corr_decis.group()

    distances.append(abs(plaintiff_ages[i] - defendant_ages[i])) 

max_plaintiff = max(plaintiff_ages)
max_defendant = max(defendant_ages)
max_dist = max(distances)

str_plaintiff = []
str_defendant = []
str_dist = []

for i in range(18, max_plaintiff):
    str_plaintiff.append(str(i))

for j in range(18, max_defendant):
    str_defendant.append(str(j))

for k in range(1, max_dist):
    str_dist.append(str(k))

str_plaintiff = ','.join(str_plaintiff)
str_defendant = ','.join(str_defendant)
str_dist = ','.join(str_dist)

print(str_plaintiff)
print(str_defendant)
print(str_dist)

# MARK:- create list objects

cases = []

for i in range(0, length):
    case = Case(ids[i], legal_relas[i], plaintiff_ages[i], defendant_ages[i], decisions[i])
    cases.append(case)

# MARK:- write to file
file = open("cases.arff", "w")

for case in cases:
    file.write(case.toString())

file.close()