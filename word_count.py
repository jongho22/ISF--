# 국가 빈도수 분석

import pandas as pd
from collections import Counter

file = pd.read_excel('C:\pythonPractice\python_study\crawler\excel\isf.xlsx')
emp_list = []
for emp in file['employment']:
    emp_list.append(emp)

# print(emp_list)

counts = Counter(emp_list)
tags = counts.most_common()
# print(tags)

print("국가 빈도수 분석")
print("국가 빈도수 :", tags)