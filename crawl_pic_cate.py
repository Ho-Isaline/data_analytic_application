import requests
from bs4 import BeautifulSoup
import os
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import string

class comic_scrap():

    def send_categories():
        url = "https://tw.manhuagui.com/list/view.html"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')

        #此網頁有將漫畫做類別分類
        res = soup.select('.filter.genre a') #選取目標(漫畫類別所在位置)
        global categories
        global ca_hrefs
        categories = [] #類別名稱
        ca_hrefs = [] #類別網址

        for category in res:
            categories.append(category.get_text())
            ca_hrefs.append(category.get('href'))
        return categories


    def scrap(ca):
        #進入此類別網址
        url1 = "https://tw.manhuagui.com" + ca_hrefs[categories.index(ca)]
        res1 = requests.get(url1)
        soup1 = BeautifulSoup(res1.text, 'html.parser')

        res1 = soup1.select(".book-list a")#選取次類別最新的所有漫畫書

        books_href = []#同一類別中漫畫的網址

        for book_href in res1[0:36]:
            books_href.append(book_href.get('href'))

        #可選擇要看幾本漫畫
        # no = int(input("請輸入要觀看的漫畫數量(1 : 一篇): "))

        book = random.sample(books_href, 1)#在最新的35本中隨機挑選n本書的網址

        for times_url in book:
            #進入漫畫網址
            url2 = "https://tw.manhuagui.com" + times_url
            res2 = requests.get(url2)
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            
            res2 = soup2.select(".book-title h1")#取得書名 
            for bookname in res2:
                book_name = bookname.get_text()
                print(book_name)

            start_to_read_href = soup2.select(".book-btn a")#取得開始閱讀網址
            read_href = start_to_read_href[0].get('href')
            url3 = "https://tw.manhuagui.com" + read_href#得到閱讀網址
            
            #改用selenium方式抓取圖片 -> 圖片連載較慢 bs4不易取得
            driver = webdriver.Chrome()#已在同層有chromedriver.exe
            driver.get(url3)#進入閱讀網址
            time.sleep(2)#等待圖片載入
            
            position = driver.find_element(By.XPATH, value='//*[@id="mangaFile"]')#尋找圖片網址的地方
            page = driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/span')#尋找頁數的地方
            src = position.get_attribute('src')#取得乾淨網址
            print('src: ',src)
            #過濾頁數
            pages = ""
            for p in page.text[3:]:
                if p != ")":
                    pages = pages + p
            
            #建立圖片資料夾
            if not os.path.exists("comics"):
                os.mkdir("comics")
            
            #網站無法直接抓取圖片 須設定header
            header_Benson = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15'}
            header_Easy = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                    "Referer" : "https://tw.manhuagui.com/"}
            pic = requests.get(src, headers=header_Easy)#取得第一頁圖片

            comic_file_name = []
            file_name = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

            time.sleep(2)#等待圖片載入

            with open("static/" + file_name + "1.jpg", "wb") as file:#開啟資料夾及圖片
                file.write(pic.content)#載入圖片
            comic_file_name.append({'img':file_name+'1.jpg'})
            #下一頁
            i=2
            #int(page)
            while i < 3: 
                nextpage = driver.find_element(By.XPATH, value='//*[@id="next"]')#尋找下一頁按鈕
                nextpage.click()#按下 下一頁按鈕
                time.sleep(1)#等待圖片載入
                position2 = driver.find_element(By.XPATH, value='//*[@id="mangaFile"]')#尋找圖片網址 (由於此網站的圖片網址無頁數規律 需一個一個找)
                src2 = position2.get_attribute('src')#過濾圖片網址
            
                pic2 = requests.get(src2, headers=header_Easy)#取得圖片網址
                time.sleep(2)#等待圖片載入

                with open("static/" + file_name + str(i) + ".jpg", "wb") as file:#找到資料夾及圖片
                    file.write(pic2.content)#載入圖片

                comic_file_name.append({'img':file_name + str(i) + ".jpg"})

                i = i+1#頁數加一
        driver.quit()#結束
        return book_name, comic_file_name


# #可選擇要看哪種類別的漫畫
# ca = input("請輸入以下選項中的其中一項 : "+str(categories)+" : ")

# #進入此類別網址
# url1 = "https://tw.manhuagui.com" + ca_hrefs[categories.index(ca)]
# res1 = requests.get(url1)
# soup1 = BeautifulSoup(res1.text, 'lxml')

# res1 = soup1.select(".book-list a")#選取次類別最新的所有漫畫書

# books_href = []#同一類別中漫畫的網址

# for book_href in res1[0:36]:
#     books_href.append(book_href.get('href'))

# #可選擇要看幾本漫畫
# no = int(input("請輸入要觀看的漫畫數量(1 : 一篇): "))

# book = random.sample(books_href, no)#在最新的35本中隨機挑選n本書的網址

# for times_url in book:
#     #進入漫畫網址
#     url2 = "https://tw.manhuagui.com" + times_url
#     res2 = requests.get(url2)
#     soup2 = BeautifulSoup(res2.text, 'lxml')
    
#     res2 = soup2.select(".book-title h1")#取得書名 
#     for bookname in res2:
#         book = bookname.get_text()
#         print(book)
        
#     start_to_read_href = soup2.select(".book-btn a")#取得開始閱讀網址
#     read_href = start_to_read_href[0].get('href')
#     url3 = "https://tw.manhuagui.com" + read_href#得到閱讀網址
    
#     #改用selenium方式抓取圖片 -> 圖片連載較慢 bs4不易取得
#     driver = webdriver.Chrome()#已在同層有chromedriver.exe
#     driver.get(url3)#進入閱讀網址
#     time.sleep(2)#等待圖片載入
    
#     position = driver.find_element(By.XPATH, value='//*[@id="mangaFile"]')#尋找圖片網址的地方
#     page = driver.find_element(By.XPATH, value='/html/body/div[2]/div[2]/span')#尋找頁數的地方
#     src = position.get_attribute('src')#取得乾淨網址
    
#     #過濾頁數
#     pages = ""
#     for p in page.text[3:]:
#         if p != ")":
#             pages = pages + p
    
#     #建立圖片資料夾
#     if not os.path.exists("comics"):
#         os.mkdir("comics")
    
#     #網站無法直接抓取圖片 須設定header
#     header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
#               "Referer" : "https://tw.manhuagui.com/"}
#     pic = requests.get(src, headers=header)#取得第一頁圖片
   
#     with open("comics\\" + book + "1.jpg", "wb") as file:#開啟資料夾及圖片
#         file.write(pic.content)#載入圖片
    
#     #下一頁
#     i=2
#     while i < int(pages): 
#         nextpage = driver.find_element(By.XPATH, value='//*[@id="next"]')#尋找下一頁按鈕
#         nextpage.click()#按下 下一頁按鈕
#         time.sleep(2)#等待圖片載入
#         position2 = driver.find_element(By.XPATH, value='//*[@id="mangaFile"]')#尋找圖片網址 (由於此網站的圖片網址無頁數規律 需一個一個找)
#         src2 = position2.get_attribute('src')#過濾圖片網址
       
#         pic2 = requests.get(src2, headers=header)#取得圖片網址

#         with open("comics\\" + book + str(i) + ".jpg", "wb") as file:#找到資料夾及圖片
#             file.write(pic2.content)#載入圖片
#         i = i+1#頁數加一
# driver.quit()#結束