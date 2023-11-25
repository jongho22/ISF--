# 국가 도시 빈도수
import pandas as pd
from collections import Counter

file = pd.read_excel('C:\pythonPractice\python_study\crawler\excel\isf.xlsx')
emp_list = []
sample__count = 0

# employment have value
for emp in file['employment']:
    emp_list.append(emp)
    
counts = Counter(emp_list)
tags = counts.most_common()
print(tags[0])
print(len(tags))
l_tags = len(tags)
##### Save data to Excel
list_number = list(range(1, l_tags + 1))
rows = l_tags  # Total number of cards
cols = 3        # Number of columns

initialization = [[0 for c in range(cols)] for r in range(rows)]
for i in range(0, len(tags)):      # 0~40까지
    print("i :", i)
    initialization[i] = tags[i]

df = pd.DataFrame(initialization,
                  list_number, columns=['국가', '도시'])

with pd.ExcelWriter('C:/pythonPractice/python_study/crawler/excel/국가_도시_빈도수3.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1')

print("The file has been saved.")