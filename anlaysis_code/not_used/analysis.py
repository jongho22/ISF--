import pandas as pd
import nltk
#nltk.download("popular")
import re
from collections import Counter
from konlpy.tag import Twitter
from nltk.corpus import stopwords
from konlpy.tag import Okt

# 선배가 만든거

file = pd.read_excel('.\ISF_news.xlsx')
dic = {}
re_title = []   # symbol remove [title1, title2, ... , title10]
pt_title = []
result_list = []    # find NN
text_all =""
for line in file['content']:
    text_all += line

okt = Okt()
noun = okt.nouns(text_all)

for i,v in enumerate(noun) :
    if len(v)<2:
        noun.pop(i)

counts = Counter(noun)
kor = counts.most_common()

#print(tags)

NN_words = []
nlpy = Twitter()

change = re.sub('[^,.?!\w\s]','', text_all)
token = nltk.word_tokenize(change.lower())
pt = nltk.pos_tag(token)

for w, p in pt:
    if 'NN' in p and w.encode().isalpha() :
        NN_words.append(w)

wlem = nltk.WordNetLemmatizer()  
lemmatized_words = []

for word in NN_words :
    new_word = wlem.lemmatize(word)
    lemmatized_words.append(new_word)

stopwords_list = stopwords.words('english')
unique_NN_words = set(lemmatized_words)
final_NN_words = lemmatized_words

for word in unique_NN_words:
    if word in stopwords_list:
        while word in final_NN_words: final_NN_words.remove(word)

counts = Counter(final_NN_words)
eng = counts.most_common()

#print(tags)

value = kor + eng

value.sort(key=lambda x:-x[1])

df = pd.DataFrame(value,columns=['word', 'count'])
df.to_excel(f'./ISF_word_count.xlsx', sheet_name='data_01')

#print(value)
