# 형태소 분석(NN count)

import pandas as pd
import nltk
import re
from collections import Counter

file = pd.read_excel('C:\pythonPractice\python_study\crawler\excel\isf.xlsx')
dic = {}
re_title = []
pt_title = []
result_list = []
i = 0

for title in file['Title']:
    for i in range(0, 1):
        change = re.sub("[-=+,#/\?:^.@*\"※~ㆍ!』‘|\[\]`\'…》\”\“\’·]", "", title)
        re_title.append(change)
print("특수 기호 제거 :", re_title)

for t in range(len(re_title)):     # 2315
    token = nltk.word_tokenize(re_title[t])
    # print("token :", token)
    pt = nltk.pos_tag(token)
    pt_title.append(pt)
# print("pt_title :", pt_title)

for i in range(len(pt_title)):         # 0~2315
    for a in range(len(pt_title[i])):  # 각 제목 길이
        # 명사일 때(NN)
        if pt_title[i][a][1] == ('NN'):
            result_list.append(pt_title[i][a][0])
# print("result_list :", result_list)
counts = Counter(result_list)
tags = counts.most_common()
print("형태소 분석 결과")
print("명사 빈도수 :", tags)
# print()
# print("len(tags) :", len(tags))
# print("tags :", (tags[0][0]))

list_number = list(range(1, len(tags) + 1))
rows = len(tags)  # Total number of cards
cols = 2        # Number of columns

initialization = [[0 for c in range(cols)] for r in range(rows)]

for i in range(len(tags)):      # repeat 109 times
    initialization[i] = tags[i]

df = pd.DataFrame(initialization,
                   list_number, columns=['noun', 'freq'])
with pd.ExcelWriter('C:/pythonPractice/python_study/crawler/excel/Noun_Freq3.xlsx') as writer:
    df.to_excel(writer, sheet_name='sheet1')

print("The file has been saved.")