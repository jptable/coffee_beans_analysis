import pandas as pd
import jieba.analyse

"""
# 這邊的程式碼是拿來嘗試利用 jieba 與 tf-idf 進行分析
# 但後來發現不同種類的詞混在一起根本不能拿來分析
# 因此最後未採用
"""

# 讀入檔案
df = pd.read_excel('df.xlsx')

# 分詞
jieba.load_userdict('D:/Users/jimmy/Desktop/dictionary/country.txt')

data_list = []

for str in df['beans']:
    seg_list = jieba.cut(str)
    data_list.append('/'.join(list(seg_list)))

# list to string
data_string = '/'.join(data_list)

# tf-idf
tfidf = jieba.analyse.extract_tags(data_string, topK=20, withWeight=False, allowPOS=(), withFlag=True)
print(tfidf)

# 計算該每個詞在資料中佔多少
count_sum = df.value_counts()
count_rate = df.value_counts(normalize=True)

df_count = pd.DataFrame(count_sum, columns=['total_number'])
df_count_rate = pd.DataFrame(count_rate, columns=['rate'])
df_count['rate'] = df_count_rate['rate']
print(df_count)

