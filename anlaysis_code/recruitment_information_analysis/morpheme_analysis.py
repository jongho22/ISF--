# 형태소 분석(NN count)

import pandas as pd
import nltk
import re
from collections import Counter

# 데이터 불러오기
file = pd.read_excel(
    "/Users/shinjongho/Desktop/2023_ISF_분석/ISF-Analysis/completed_data/주제 1) 2023_국제스포츠_채용정보_분석/(채용정보) ISF-국제스포츠 일자리 데이터.xlsx"
)

dic = {}
re_title = []  # 특수기호를 제거한 제목
pt_title = []  # 토큰화 작업을 한 제목
result_list = []

# 특수 기호 제거
for title in file["Title"]:
    for i in range(0, 1):
        change = re.sub("[-=+,#/\?:^.@*\"※~ㆍ!』‘|\[\]`'…》\”\“\’·%–]", "", title)
        re_title.append(change)

# 토큰화
for t in range(len(re_title)):
    token = nltk.word_tokenize(re_title[t])
    pt = nltk.pos_tag(token)
    pt_title.append(pt)

# 형태소 분석 (명사 찾기)
for i in range(len(pt_title)):
    for a in range(len(pt_title[i])):  # 각 제목 길이
        # 명사일 때(NN)
        if pt_title[i][a][1] == ("NN") or pt_title[i][a][1] == ("NNP"):
            result_list.append(pt_title[i][a][0])


# 결과 확인
counts = Counter(result_list)
tags = counts.most_common()
print("형태소 분석 결과")
print("명사별 빈도수 :", tags)

list_number = list(range(1, len(tags) + 1))
rows = len(tags)  # Total number of cards
cols = 2  # Number of columns

initialization = [[0 for c in range(cols)] for r in range(rows)]

for i in range(len(tags)):
    initialization[i] = tags[i]

# 저장
df = pd.DataFrame(initialization, list_number, columns=["명사", "빈도수"])
with pd.ExcelWriter(
    "/Users/shinjongho/Desktop/2023_ISF_분석/ISF-Analysis/completed_data/주제 1) 2023_국제스포츠_채용정보_분석/(채용정보) 제목의 명사 빈도수.xlsx"
) as writer:
    df.to_excel(writer, sheet_name="sheet1")

print("작업이 완료되었습니다.")
