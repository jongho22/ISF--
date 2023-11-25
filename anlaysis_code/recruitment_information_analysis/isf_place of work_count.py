# 국가 도시 빈도수
import pandas as pd
from collections import Counter

file = pd.read_excel(
    "/Users/shinjongho/Desktop/2023_ISF_분석/ISF-Analysis/completed_data/주제 1) 2023_국제스포츠_채용정보_분석/(채용정보) ISF-국제스포츠 일자리 데이터.xlsx"
)
emp_list = []
sample__count = 0

# 근무지 정보
for emp in file["employment"]:
    emp_list.append(emp)

counts = Counter(emp_list)
tags = counts.most_common()  # ('스위스, Lausanne', 128)
l_tags = len(tags)  # 34개
list_number = list(range(1, l_tags + 1))
rows = l_tags  # Total number of cards
cols = 4

initialization = [[0 for c in range(cols)] for r in range(rows)]

for i in range(0, len(tags)):
    num = tags[i][1]
    tags[i] = tags[i][0].split(",", 1)
    tags[i].append(int(num))
    initialization[i] = tags[i]

    print(tags[i])


df = pd.DataFrame(initialization, list_number, columns=["국가", "도시(근무지)", "빈도수"])

# 엑셀 저장
with pd.ExcelWriter(
    "/Users/shinjongho/Desktop/2023_ISF_분석/ISF-Analysis/completed_data/주제 1) 2023_국제스포츠_채용정보_분석/(채용정보) 근무지 빈도수.xlsx"
) as writer:
    df.to_excel(writer, sheet_name="sheet1")

print("작업이 완료되었습니다.")
