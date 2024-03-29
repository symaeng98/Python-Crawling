from selenium import webdriver
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import time
import csv

# <죵재>
# /Users/yongcho/Downloads/chromedriver
# <aodtns>
# C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe
yong_path = "/Users/yongcho/Desktop/Tool/chromedriver"
maeng_path = "C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~driver 수정~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
browser = webdriver.Chrome(maeng_path)  # './chromedriver'
# browser.maximize_window() #창 최대화
url = 'https://www.flashscore.co.kr/soccer/england/premier-league/archive/'
browser.get(url)

# 지정한 위치로 스크롤 하기
browser.execute_script("window.scrollTo(0,300)")  # 300크기만큼 스크롤 내림

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 파일 오픈
filename = "Dataset.csv"
file = open(filename, "w", encoding="utf-8-sig", newline="")
csvfile = csv.writer(file)  # writer로 파일 쓰기

feature = ['HT', 'AT', 'HG', 'AG', 'HP', 'AP', 'HS', 'AS', 'HOT', 'AOT', 'HMS', 'AMS', 'HBS', 'ABS', 'HF', 'AF', 'HCNR',
           'ACNR', 'HOFF', 'AOFF', 'HTHR', 'ATHR', 'HSV', 'ASV', 'HFL', 'AFL', 'HYC', 'AYC', 'HPSS', 'APSS', 'HTCK',
           'ATCK', 'HATTK', 'AATTK', 'HTA', 'ATA']
csvfile.writerow(feature)

# 팝업.
browser.find_element_by_xpath('''//*[@id="onetrust-accept-btn-handler"]''').click()
browser.maximize_window()
# 아카이브 페이지에서 시즌 태그 중에 첫번쨰 불러오기
year1 = 2021
year2 = 2022
game_cnt = 0
season_data = [['' for x in range(36)] for _ in range(1520)]  # 모든 데이터를 1차원 배열로 담을거임
for i in range(1, 4):
    year1 -= i
    year2 -= i
    browser.find_element_by_link_text(f"프리미어리그 {year1}/{year2}").click()
    browser.implicitly_wait(5)
    # 시즌 페이지에서 결과창 불러오기
    browser.execute_script("window.scrollTo(0,300)")  # 300크기만큼 스크롤 내림
    browser.find_element_by_link_text("결과").click()
    browser.implicitly_wait(10)

    # 결과 창에서 id 찾기 + 더 많은 경기 보기
    soup = BeautifulSoup(browser.page_source, 'lxml')
    for j in range(3):

        browser.implicitly_wait(10)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        more_match = soup.find("a", attrs={"class": "event__more event__more--static"}).get_text()
        if len(more_match) == 0:
            break
        browser.implicitly_wait(10)

        browser.find_element_by_link_text("더 많은 경기 보기").click()

    soup = BeautifulSoup(browser.page_source, 'lxml')
    arr = soup.find_all('div', attrs={'title': "경기세부사항을 보려면 클릭"})

    # id 수정 및 id 배열 만들기
    id_arr = []
    for ar in arr:
        ar['id'] = ar['id'][4:]
        id_arr.append(ar['id'])

    for j in range(len(id_arr)):
        # 새로운 창에 대해 url 얻기
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~driver 수정~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        browser2 = webdriver.Chrome(maeng_path)  # './chromedriver'
        url_for_statistic = f"https://www.flashscore.co.kr/match/{id_arr[j]}/#match-summary/match-statistics/0"
        browser2.get(url_for_statistic)
        soup2 = BeautifulSoup(browser2.page_source, 'lxml')

        # 팀 이름 가져오기
        match = soup2.find_all("a", attrs={"class": "participant__participantName participant__overflow"})
        name_list = []
        for m in match:
            m_strip = str(m['href']).split('/')
            name_list.append(m_strip[2])
        home_name = name_list[0]
        away_name = name_list[1]

        # 점수로 승, 무, 패 결정하기
        score = soup2.find("div", attrs={"class": "detailScore__wrapper"}).get_text()
        home_score = score[0]
        away_score = score[2]
        if home_score > away_score:
            Win_Draw_Lose_HomeTeam = 2
        elif home_score == away_score:
            Win_Draw_Lose_HomeTeam = 1
        else:
            Win_Draw_Lose_HomeTeam = 0

        # 통계 데이터 가져오기

        category = soup2.find_all("div", attrs={"class": "statCategoryName"})
        home_data = soup2.find_all("div", attrs={"class": "statHomeValue"})
        away_data = soup2.find_all("div", attrs={"class": "statAwayValue"})
        home_data_score = []
        away_data_score = []
        category_name = []
        for h in home_data:
            home_data_score.append(h.get_text())
        for a in away_data:
            away_data_score.append(a.get_text())
        for c in category:
            category_name.append(c.get_text())
        # for k in range(len(category_name)):
        #     print(f"홈팀 {category_name[k]} : {home_data_score[k]}")
        #     print(f"어웨이팀 {category_name[k]} : {away_data_score[k]}")
        # print(home_name, away_name, home_score, away_score, home_data_score[:], away_data_score[:])
        # exit(0)

        season_data[game_cnt][0] = home_name
        season_data[game_cnt][1] = away_name
        season_data[game_cnt][2] = home_score
        season_data[game_cnt][3] = away_score

        if '스로우인' not in category_name:
            home_data_score.insert(8, 0)
            away_data_score.insert(8, 0)

        if '경고' not in category_name:
            home_data_score.insert(11, 0)
            away_data_score.insert(11, 0)

        if '퇴장' in category_name:
            home_data_score.pop(category_name.index('퇴장'))
            away_data_score.pop(category_name.index('퇴장'))

        while len(home_data_score) != 16:
            home_data_score.insert(len(home_data_score) - 1, 0)

        while len(away_data_score) != 16:
            away_data_score.insert(len(home_data_score) - 1, 0)

        for k in range(4, 36):
            if k % 2 == 0:
                season_data[game_cnt][k] = home_data_score[(k // 2) - 2]
            else:
                season_data[game_cnt][k] = away_data_score[(k // 2) - 2]

        csvfile.writerow(season_data[game_cnt])

        game_cnt += 1

        browser2.close()
    browser.back()
    browser.back()