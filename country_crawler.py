import re

from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
# 爬國家資料

driver = webdriver.Chrome('D:/selenium/chromedriver.exe')
driver.get('https://multilingual.mofa.gov.tw/web/web_UTF-8/almanac/almanac2007/html/12-14.htm')

country = []
EmptyList = []
try:
    for i in range(1,7):
        for j in range(0, 55):
            country.append(driver.find_elements(by=By.XPATH, value='/html/body/div/table[%d]/tbody/tr[%d]/td[1]/p/span[1]/span' %(i,j)))
except:
    print('warning')

for i in range(0, len(country)):
    if country[i] != EmptyList:
        country[i][0] = country[i][0].text

df = pd.DataFrame(country)
df.to_excel('country.xlsx', index=False)
driver.close()

# 找跟之前重複到的國家，去掉重複值
f = open('D:/Users/jimmy/Desktop/dictionary/country.txt', encoding='UTF=8')
text = f.read()
f.close()

text = re.sub('ns', '', text)
text = re.sub(' ', '', text)
text = text.split('\n')
text = pd.DataFrame(text)
text = text.drop_duplicates()
text = text.values.tolist()
text = '\n'.join(map(str, text))
text = re.sub('[\[\]\']', '', text)
f = open('D:/Users/jimmy/Desktop/dictionary/country.txt', encoding='UTF=8', mode='w')
f.write(text)
f.close()

