import pandas as pd
import re

"""
注意:資料已丟到 origin_data 資料夾
如果要使用這些 excel 檔，需要改 path 至 origin_data/data1.xlsx
"""

"""
# 將爬到的資料做初步的整理，將一些特殊字元、英文字清除
# 部分 data 直接使用 Excel 處理完成，因此不在這裡出現
"""

"""data1"""
df1 = pd.read_excel('data1.xlsx')
del df1['Unnamed: 0']

df1['咖啡豆'] = df1[0]
del df1[0]
# 清除雜訊
df1['咖啡豆'] = df1['咖啡豆'].replace(r'[,]', '', regex=True)
df1['半磅'] = df1['咖啡豆'].str.extract(r'半磅\s(\$\d+)')
df1['咖啡豆'] = df1['咖啡豆'].replace(r'\n.*', '', regex=True)
df1['半磅'] = df1['半磅'].replace(r'\$', '', regex=True)
print(df1)
# df1.to_excel('data1.xlsx')

"""data2"""
df2 = pd.read_excel('data2.xlsx')
df2 = df2.dropna()
del df2['Unnamed: 0']
df2['咖啡豆'] = df2[0]
del df2[0]
# 清除雜訊
df2['咖啡豆'] = df2['咖啡豆'].replace(r'[👆✓]', '', regex=True)
df2['咖啡豆'] = df2['咖啡豆'].replace(r'優惠活動.*', '', regex=True)
df2['咖啡豆'] = df2['咖啡豆'].replace(r'風\s*味.*', '', regex=True)
df2['咖啡豆'] = df2['咖啡豆'].replace(r'/半磅', '/半磅|', regex=True)
df2['咖啡豆'] = df2['咖啡豆'].replace(r'\n{1}', '', regex=True)
# 一個 row 有好多個商品，轉成 string 比較好清
df2 = pd.DataFrame.to_string(df2, header=False, index=False)
df2 = re.sub(r'[\n\s]', '', df2)
df2 = re.sub(r'烘焙度：', '@', df2)
df2 = re.sub(r'咖啡豆：', '@', df2)
df2 = re.sub(r'，[0-9]{1,5}元/半磅\|', '', df2)
df2 = re.sub(r'，[0-9]{1,5}元', "", df2)
df2 = re.sub(r'半磅咖啡', "", df2)
df2 = re.sub(r'1/4磅咖啡', '', df2)
df2 = re.sub(r'掛耳包','', df2)
df2 = re.sub(r'元/半磅', '', df2)

df2 = df2.split('|')

for i in range(len(df2)):
    df2[i] = df2[i].split('@')

"""
# 發現有一個row 與另一項合併到了，因為前一項沒有價錢，導致該row有四項無法合成DF
# 解法:移除這兩筆資料
"""

df2.remove(df2[9])
df2 = pd.DataFrame(df2, columns=['咖啡豆', '烘焙度', '半磅'])
df2 = df2.dropna()
print(df2)
# df2.to_excel('data2.xlsx')

"""data3"""
"""
# 困難點: 價格以區間顯示，因為他們把一磅、半磅、嘗鮮價放在第二頁，要點進去才看得到
# 除了上千元的咖啡豆以外，其他的買一磅約打9折左右。為求方便，以最高價除以2作為半磅價格
"""
df3 = pd.read_excel('data3.xlsx')
del df3['Unnamed: 0']
df3['咖啡豆'] = df3[0]
del df3[0]
df3['咖啡豆'] = df3['咖啡豆'].replace(r',', '', regex=True)
df3['半磅'] = df3['咖啡豆'].str.extract(r'~ NT\$(\d+)')   # 將價錢跟品名區隔開

# print(df3['半磅'].isnull())
# print(df3['咖啡豆'][11])
df3['半磅'][11] = 3850*2  # 因為只有一個 null 所以手動補值就好
df3['咖啡豆'] = df3['咖啡豆'].replace(r'\nNT.*', '', regex=True)

# 將一磅的價格全部除以2，就是半磅了
for i in range(len(df3)):
    df3['半磅'][i] = int(df3['半磅'][i]) / 2
print(df3)

# to_excel
# df3.to_excel('data3.xlsx')

"""data4"""
df4 = pd.read_excel('data4_1.xlsx')
for i in range(2,13):
    i = pd.read_excel('data4_%d.xlsx' %i)
    df4.append(i, ignore_index=True)
del df4['Unnamed: 0']
# print(df4[~df4[0].str.contains('半磅')])

df4['咖啡豆'] = df4[0]
del df4[0]
df4['咖啡豆'] = df4['咖啡豆'].replace(',', '', regex=True)
df4['半磅'] = df4['咖啡豆'].str.extract(r'NT\$(\d+)')
df4 = df4[-df4['咖啡豆'].str.contains('掛耳包', regex =True)]
temp1 = df4[df4['咖啡豆'].str.contains('114g', regex=True)].reset_index()
temp2 = df4[df4['咖啡豆'].str.contains('一磅', regex=True)].reset_index()
del temp1['index']
del temp2['index']
for i in range(len(temp1)):
    temp1['半磅'][i] = int(temp1['半磅'][i]) * 2
for i in range(len(temp2)):
    temp2['半磅'][i] = int(temp2['半磅'][i]) / 2
df4 = df4[-df4['咖啡豆'].str.contains('114g', regex =True)]
df4 = df4[-df4['咖啡豆'].str.contains('一磅', regex =True)]
df4.append(temp1)
df4.append(temp2)

df4['咖啡豆'] = df4['咖啡豆'].replace(r'\nNT\$\d+', '', regex=True)
df4['咖啡豆'] = df4['咖啡豆'].replace(r'\(半磅\)', '', regex=True)
df4['咖啡豆'] = df4['咖啡豆'].replace(r'\(114g/鐵罐裝\)', '', regex=True)
df4['咖啡豆'] = df4['咖啡豆'].replace(r'\(一磅\)', '', regex=True)
df4['咖啡豆'] = df4['咖啡豆'].replace(r'●', '', regex=True)
print(df4)
# to excel
# df4.to_excel('data4.xlsx')


"""data6"""
df6_1 = pd.read_excel('origin_data/data6_1.xlsx')
df6_2 = pd.read_excel('origin_data/data6_2.xlsx')
df6_3 = pd.read_excel('origin_data/data6_3.xlsx')

del df6_1['Unnamed: 0']
del df6_2['Unnamed: 0']
del df6_3['Unnamed: 0']

df6 = df6_1.append(df6_2).append(df6_3)
df6 = df6.dropna()
df6['咖啡豆'] = df6[0]
del df6[0]
df6['咖啡豆'] = df6['咖啡豆'].replace(r'\n加入購物車', "", regex=True)
df6['咖啡豆'] = df6['咖啡豆'].replace(r'｜', "", regex=True)
df6['咖啡豆'] = df6['咖啡豆'].replace(r'[\n/]', "", regex=True)
df6['咖啡豆'] = df6['咖啡豆'].replace(r'[ ”]', "", regex=True)
df6['咖啡豆'] = df6['咖啡豆'].replace(r'^.*系列|$', "", regex=True)
df6['咖啡豆'] = df6['咖啡豆'].replace(r'活動專區|', "", regex=True)
df6['咖啡豆'] = df6['咖啡豆'].replace(r',', "", regex=True)
# df6.to_excel('temp.xlsx')

# 中間有用 excel 進行清理
df6 = pd.read_excel('temp.xlsx')
df6['C3'] = df6['C3'].replace(r'[^0-9]', "", regex=True)
df6['C1'] = df6['C1'].replace(r'[0-9a-zA-z]', "", regex=True)
df6['C1'] = df6['C1'].replace(r'[+-“.]', "", regex=True)
new_col = ['咖啡豆', '半磅', 'g']
df6.columns = new_col

# to excel
# df6.to_excel('data6.xlsx')
print(df6)


"""data12"""
for i in range(1,3):
    df12 = pd.read_excel('data12_%d.xlsx'%i)
    df12.append(df12)
del df12['Unnamed: 0']
df12 = df12.dropna()
df12[0] = df12[0].replace(r"【.*】", "", regex=True)
df12[0] = df12[0].replace(r"缺貨中\n", "", regex=True)
df12[0] = df12[0].replace(r"–\n選擇規格", "", regex=True)
df12[0] = df12[0].replace(r"[「」® –/”]", "", regex=True)
df12[0] = df12[0].replace(r"\n加入購物車", "", regex=True)
df12[0] = df12[0].replace(r"咖啡豆", "", regex=True)

# 將不是半磅的豆子個別處理，並另存
# temp = df12[df12[0].str.contains("g")]
# temp.to_excel('temp.xlsx')

df12 = df12.drop(df12.index[0])
df12[['咖啡豆', '半磅']] = df12[0].str.split('\n', expand=True)
df12 = df12.drop(0, axis=1)
df12['半磅'] = df12['半磅'].replace(r'NT\$', '', regex=True)
print(df12)
# to excel
# df12.to_excel('data12.xlsx')
