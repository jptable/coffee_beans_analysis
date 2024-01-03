import pandas as pd

"""
# cleaner3: 將 beans 欄位未分類的字詞拆成以下幾個欄位
# "國家" "城市/產地" "處理廠/莊園" "處理法" "烘焙度" "其他"    
"""

# 匯入 excel
df = pd.read_excel('df.xlsx')
df = df.dropna()

"""
# 建立函式
# 1. 讀 dictionary 的字進 text
# 2. 讓 df 跟 dictionary 的字進行比對，
#    有比對到的留下

"""

# 讀 dictionary
def to_txt(path, filename):
    f = open(path, encoding='UTF-8')
    temp_text = f.read()
    f.close()
    filename = temp_text.split('\n')
    return filename

# 進行比對
def string_classification(filename, search_from, put_into):
    """
    filename 是要使用的那個 dictionary 的名稱
    search_from 是要執行 str.contains 的 DataFrame column
    put_into 是從 search from 找到目標之後，修改完要存取的位置。也是指定一個 DataFrame column
    """
    for i in range(0, len(filename)):
        put_into.loc[search_from.str.contains(filename[i])] = filename[i]
    return 0


"""執行 to_txt 函式"""
country = to_txt('D:/Users/jimmy/Desktop/dictionary/country.txt', filename='country')  # country.txt
towns = to_txt('D:/Users/jimmy/Desktop/dictionary/towns.txt', filename='towns')  # towns.txt
beneficio = to_txt('D:/Users/jimmy/Desktop/dictionary/beneficio.txt', filename='beneficio')  # beneficio.txt
process = to_txt('D:/Users/jimmy/Desktop/dictionary/process.txt', filename='process')  # process.txt
roast = to_txt('D:/Users/jimmy/Desktop/dictionary/roast.txt', filename='roast')  # roast.txt
others = to_txt('D:/Users/jimmy/Desktop/dictionary/others.txt', filename='others')  # others.txt

"""建立額外 6 個 columns"""
df['country'] = ''
df['towns'] = ''
df['beneficio'] = ''
df['process'] = ''
df['roast'] = ''
df['others'] = ''

"""執行比對函式"""
string_classification(country, df['beans'], df['country'])  # country
string_classification(towns, df['beans'], df['towns'])  # towns
string_classification(beneficio, df['beans'], df['beneficio'])  # beneficio
string_classification(process, df['beans'], df['process'])  # process
string_classification(roast, df['beans'], df['roast'])  # roast
string_classification(others, df['beans'], df['others'])  # others
# print(df[['beans', 'country']].sample(5))

del df['beans']  # beans 的資料都成功切割到其他 columns 了，故移除

# 將 price_half_pound 移到最後面
column_to_move = df.pop('price_half_pound')
df.insert(6, 'price_half_pound', column_to_move)

# to excel
# df.to_excel('clean_data.xlsx')

# country
df['country'] = ''
country = to_txt('dictionary/country.txt', filename='country')
string_classification(country, df['beans'], df['country'])