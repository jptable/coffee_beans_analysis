import pandas as pd

"""
# 注意:資料已丟到 origin_data 資料夾
# 如果要使用這些 excel 檔，需要改 path 至 origin_data/data1.xlsx
"""


"""
# 將所以初步清理完成的檔案合併，並繼續清理
"""
# 整理完後將所有df整併
df = pd.read_excel('origin_data/data1.xlsx')
for i in range(2,14):
    temp = pd.read_excel('origin_data/data%d.xlsx' %i)
    df = df.append(temp)

"""
# 因為有些檔案在進行 excel 處理時把 index 刪掉了，而 python 處理的有保留 index
# 所以 append 的時後有 index 的 dataframe 多了一欄未命名欄位(Column1)
"""

# print(df[df['Column1'].notna()])
del df['Unnamed: 0']

"""
# 之前在清理資料時使用中文作為 columns，在寫code的時候不太方便
# 這邊把它改成英文
"""
new_columns = ['beans', 'price_half_pound']
df.columns = new_columns

# 發現還有一些遺漏雜訊
df['beans'] = df['beans'].str.replace('\n', '', regex=True)
df['beans'] = df['beans'].str.replace(' ', '', regex=True)
df['beans'] = df['beans'].str.replace("[a-zA-z0-9()]", '', regex=True)
df['beans'] = df['beans'].str.replace("[（）%&]", '', regex=True)
df['beans'] = df['beans'].str.replace("[\-\.\'/。#]", '', regex=True)
df['beans'] = df['beans'].str.replace("系列", '', regex=True)
df['beans'] = df['beans'].str.replace("處理場", '', regex=True)
df['beans'] = df['beans'].str.replace("處理廠", '', regex=True)
df['beans'] = df['beans'].str.replace("精品", '', regex=True)
df['beans'] = df['beans'].str.replace("配方", '', regex=True)
df['beans'] = df['beans'].str.replace("風味", '', regex=True)
df['beans'] = df['beans'].str.replace("頂級", '', regex=True)
df['beans'] = df['beans'].str.replace("雙重", '', regex=True)
df['beans'] = df['beans'].str.replace("藝妓", '藝伎', regex=True)
df['beans'] = df['beans'].str.replace("瑰夏", '藝伎', regex=True)
df['beans'] = df['beans'].str.replace("耶加雪夫", '耶加雪菲', regex=True)
df['beans'] = df['beans'].str.replace("耶加雪非", '耶加雪菲', regex=True)
df['beans'] = df['beans'].str.replace("波利維亞", '玻利維亞', regex=True)
df['beans'] = df['beans'].str.replace("卡杜依", '卡杜艾', regex=True)
df['beans'] = df['beans'].str.replace("卡度依", '卡杜艾', regex=True)
df['beans'] = df['beans'].str.replace("卡度艾", '卡杜艾', regex=True)
df['beans'] = df['beans'].str.replace("卡度拉", '卡杜拉', regex=True)
df['price_half_pound'] = df['price_half_pound'].astype(str)
df['price_half_pound'] = df['price_half_pound'].str.replace(",", '', regex=True)
# print(df)
# df.to_excel('df.xlsx', index=None)
