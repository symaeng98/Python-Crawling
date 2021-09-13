from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome("C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe") #'./chromedriver'
browser2 = webdriver.Chrome("C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe") #'./chromedriver'
# browser.maximize_window() #창 최대화
url = 'https://www.flashscore.co.kr/soccer/england/premier-league/archive/'
browser.get(url)

#지정한 위치로 스크롤 하기
browser.execute_script("window.scrollTo(0,300)") #300크기만큼 스크롤 내림

#화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#아카이브 페이지에서 시즌 태그 중에 첫번쨰 불러오기
browser.find_element_by_link_text("프리미어리그 2021/2022").click()

#시즌 페이지에서 결과창 불러오기
browser.execute_script("window.scrollTo(0,300)") #300크기만큼 스크롤 내림
browser.find_element_by_link_text("결과").click()


#결과 창에서 id찾기
browser.execute_script("window.scrollTo(0,300)") #300크기만큼 스크롤 내림
soup = BeautifulSoup(browser.page_source,'lxml')
id_arr = soup.find_all('div', attrs={'class':'event__match event__match--static event__match--twoLine'})

for id in id_arr:
    id['id'] = id['id'][4:]
    print(id['id'])

#새로운 창에 대해 url 얻기
url_for_statistic = f"https://www.flashscore.co.kr/match/{id_arr[0]['id']}/#match-summary/match-summary"
browser2.get(url_for_statistic)
browser2.find_element_by_link_text("통계").click()
