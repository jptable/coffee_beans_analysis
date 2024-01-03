from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd


"""爬取資料"""
def crawler(url, low_length, high_length, value):
    driver = webdriver.Chrome('D:/selenium/chromedriver.exe')
    driver.get(url)
    try:
        data = []
        EmptyList = []
        for i in range(low_length, high_length):  # 執行爬蟲
            data.append(driver.find_elements(by=By.XPATH, value=value % i))
        for i in range(len(data)):
            if data[i] != EmptyList:  # if data[i] 裡面有值，則將值轉換成 text，反之 break
                data[i][0] = data[i][0].text
            else:
                break
    except ValueError:
        print('value error')
    else:
        print('No Problem')
    finally:
        print('End')
    driver.quit()

    return data


"""to_excel"""
def download(data, filename):
    data = pd.DataFrame(data)
    data.to_excel("D:/github_project/coffee bean analysis/%s.xlsx" % filename)
    return 0


"""Buon caffe"""
data1 = crawler('https://www.buoncaffe.com.tw/pages/product-list', 3, 164,
                value='//*[@id="product_list_container"]/div[%d]/a/div[2]/div[1]')
download(data1, filename='data1')
print('data1 end')

"""暖窩咖啡"""
data2 = crawler('https://shop.cozyhousecoffee.com/pages/%E5%92%96%E5%95%A1%E8%B1%86%E5%96%AE', 3, 26,
                value='//*[@id="Content"]/div[1]/div[%d]')
download(data2, filename='data2')
print('data2 end')

"""再之在"""
data3 = crawler('https://www.cafehereagain.com.tw/categories/%E8%8E%8A%E5%9C%92%E7%B2%BE%E5%93%81%E5%92%96%E5%95%A1'
                '%E8%B1%86', 1, 21,
                value='/html/body/div[9]/div[1]/div/div/div/div[2]/div[2]/ul/li[%d]/a/div[2]')
download(data3, filename='data3')
print('data3 end')

"""OKLAO"""
for j in range(1, 13):
    data4 = crawler('https://www.idou.com.tw/categories/coffeebean?page=%d&sort_by=&order_by=&limit=24'%j, 1, 25,
                    value='//*[@id="Content"]/div/div[2]/div/div[2]/div[2]/div[1]/div[%d]/product-item/a/div[2]/div')
    download(data4, filename='data4_%d'%j)
print('data4 end')

"""kakalove"""
data5 = crawler('https://www.kakalovecafe.com.tw/products?page=1&sort_by=&order_by=&limit=72', 1, 73,
                value='//*[@id="Content"]/div/div/div[2]/div[2]/div[2]/div[1]/div[%d]/product-item/a/div[2]/div')
download(data5, filename='data5')
print('data5 end')

# 湛盧咖啡
for j in range(1, 4):
    data6 = crawler('https://www.zhanlu.com.tw/product-category/baked-beans/page/%d/'%j, 1, 13,
                    value='//*[@id="main"]/div/div[2]/div/div[3]/div[%d]/div/div[2]/div[2]')
    download(data6, filename='data6_%d'%j)
print('data6 end')

"""Bargain cafe"""
data7 = crawler('https://www.bargain-cafe.com/categories/%E5%95%86%E5%93%81%E5%88%86%E9%A1%9E?limit=72',
                1, 30, value='//*[@id="Content"]/div/div/div[2]/div[2]/div[2]/div/div[%d]/product-item/a/div[2]')
download(data7, filename='data7')
print('data7 end')

"""dear john"""
data8 = crawler('https://www.dearjohncoffee.com.tw/categories/%E7%B2%BE%E9%81%B8%E5%92%96%E5%95%A1%E8%B1%86?limit=72', 1, 17, value='/html/body/div[9]/div[1]/div/div/div/div[2]/div[2]/ul/li[%d]/product-item/a/div[2]/div')
download(data8, 'data8')
print('data8 end')

"""新篇章咖啡"""
data9 = crawler('https://www.nextchapter.com.tw/pages/%E6%96%B0%E7%9A%84%E5%88%86%E9%A0%81-1', 1, 11,
                value='//*[@id="page-item-60687f503437a20020a32a90"]/div/div[1]/div[%d]/product-item/a/div[2]/div')
download(data9, 'data9')
print('data9 end')

"""廣吉食品"""
data10 = crawler('https://www.kugifoods.com.tw/product_list.php?bc=3&pc=4', 1, 6,
                 '/html/body/main/div[2]/div/ul/li[%d]/div')
download(data10, 'data10')
print('data10 end')

"""Riverbird"""
data11 = crawler('https://www.riverbird.com.tw/categories/category-2', 1, 25,
                 '//*[@id="Content"]/div/div[2]/div/div[2]/div[2]/div/a[%d]/div[2]')
download(data11, 'data11')
print('data11 end')

"""hayya's"""
for j in range(1, 3):
    data12 = crawler('https://www.haaya.com.tw/product-category/%E6%A5%B5%E4%B8%8A%E7%8F%88%E5%95%A1%E7%B3%BB%E5%88%97-%E5%92%96%E5%95%A1%E8%B1%86/page/{0}/'.format(j),
                     1, 32, '/html/body/div[4]/div[3]/div[2]/div/div/div[4]/div[%d]')
    download(data12, 'data12_%d'%j)
print('data12 end')
