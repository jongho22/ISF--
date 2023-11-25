# 국가 빈도수 분석

import pandas as pd
from collections import Counter

file = pd.read_excel('/Users/shinjongho/Desktop/2023_ISF_분석/ISF-Analysis/completed_data/주제 1) 2023_국제스포츠_채용정보_분석/(채용정보) ISF-국제스포츠 일자리 데이터.xlsx')
emp_list = []
for emp in file['employment']:
    emp_list.append(emp)

# print(emp_list)

counts = Counter(emp_list)
tags = counts.most_common()
# print(tags)

print("국가 빈도수 분석")
print("국가 빈도수 :", tags)