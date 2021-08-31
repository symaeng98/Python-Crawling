from selenium import webdriver
import csv
import requests
from bs4 import BeautifulSoup

##selenium으로 일정 클릭
browser = webdriver.Chrome()
url = "https://www.spojoy.com/sportsinfo/infomation/league/?country=eng&category=soccer&game_gubun=D"
browser.get(url)
elem = browser.find_element_by_id("img2")
elem.click()

##title 스크래핑
filename = "EPL경기 결과.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)
title = "시간	대회 홈팀	vs	원정팀 결과".split()
writer.writerow(title)

##내용 스크래핑
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
data_rows = soup.find_all("table", attrs={"id":"stbl"}).find("tbody").find_all("tr")
for row in data_rows:
    columns = row.find_all("td")
    data = [column.get_text() for column in columns]
    print(data)