import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np

url = 'https://www.manhuagui.com/rank/total.html'
res = requests.get(url)
soup = BeautifulSoup(res.text ,'html.parser')
name_link = soup.select('.rank-detail h5 a')

manhua_link ={}
for manhua in name_link:
    name = manhua.text
    link = manhua.get('href')
    manhua_link[name]=link


#最後要建立df得元素
manhua_dic ={}
name_list=[]
url_list=[]
first_publish_list=[]
status_list=[]
comment_amount_list=[]
score_amount_list =[]
catagory_list=[]
latest_chapterNumber_list=[]
browser = webdriver.Chrome()
for manhua_name, manhua_url in manhua_link.items():
    manhua_url = 'https://www.manhuagui.com'+manhua_url
    browser.execute_script("window.open('new window')")
    browser.implicitly_wait(5)
    windows=browser.window_handles  #get all windows in your browser
    browser.switch_to.window(windows[-1])
    browser.get(manhua_url)
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    manhua_first_publish = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[2]/ul/li[1]/span[1]/a').text
    manhua_status = browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[2]/ul/li[4]/span/span[1]').text
    manhua_score_ammount = browser.find_element(By.XPATH, '//*[@id="scoreRes"]/div[1]/p[2]/span').text

    #把漫畫類別做成一個ｌｉｓｔ
    manhua_catagory_temp = browser.find_elements(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div[2]/ul/li[2]/span[1]/a')
    manhua_catagory=[]
    for a in manhua_catagory_temp:
        manhua_catagory.append(a.text)
    manhua_latest_upgrade_ul = browser.find_elements(By.XPATH, '//*[@id="chapter-page-1"]/ul')
    for ul in manhua_latest_upgrade_ul:
        li_list= ul.find_elements(By.TAG_NAME, 'li')
        li=li_list[-1]
        manhua_latest_chapter = li.find_elements(By.TAG_NAME,'a')[-1].text.split('-')[-1]


    name_list.append(manhua_name)
    url_list.append(manhua_url)
    first_publish_list.append(manhua_first_publish)
    status_list.append(manhua_status)
    score_amount_list.append(manhua_score_ammount)
    catagory_list.append(manhua_catagory)
    latest_chapterNumber_list.append(manhua_latest_chapter)
    time.sleep(3)
    manhua_comment_amount = browser.find_element(By.XPATH, '//*[@id="Comment"]/div/h2/span[1]/em').text
    comment_amount_list.append(manhua_comment_amount)



    
browser.quit()
manhua_dic['name'] = name_list
manhua_dic['url'] = url_list
manhua_dic['first_publish'] = first_publish_list
manhua_dic['status'] = status_list
manhua_dic['comment_ammount'] = comment_amount_list
manhua_dic['score_amount'] = score_amount_list
manhua_dic['catagory'] = catagory_list
manhua_dic['latest_chapterNumber'] = latest_chapterNumber_list
print(manhua_dic)

df = pd.DataFrame(manhua_dic, index=np.arange(1,51))

df.to_csv('manhua_rank.csv',encoding='utf-8')