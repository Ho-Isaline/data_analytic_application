import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.manhuagui.com/rank/total.html"
res = requests.get(url)
data = BeautifulSoup(res.text, 'lxml')

title = data.select(".rank-title a")
status = data.select(".rank-title span")
update = data.select(".rank-time")
score = data.select(".rank-score")
info_list = list(zip(title, status, update, score))
print(info_list)

with open("request.csv",'w', newline='',encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["title", "status", "update", "score"])
    for title, status, update, score in info_list:
        writer.writerow([title.text, status.text, update.text, score.text])