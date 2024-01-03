import pandas as pd


"""cleaner4 目標: 將 towns 對應到目標 country，並填上"""

# 讀入檔案
df = pd.read_excel('clean_data.xlsx')
del df['Unnamed: 0']

# 移除 country 與 towns 都是 NaN 的商品
df = df[-(df['towns'].isnull() & df['country'].isnull())]

# 看一下各個 columns NaN 的比例有多少
print('columns with na:\n', df.isnull().sum(), '\n')
na_rate = round(df.isnull().sum() / df.shape[0] * 100)
print('na rate in columns (%):\n', na_rate, '\n')

# to excel
# df.to_excel('to_tableau.xlsx')

print('five number summary from price:\n', round(df['price_half_pound'].describe()))