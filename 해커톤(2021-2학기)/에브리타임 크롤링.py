from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

#CSV파일을 읽고 배열로 변환하기
readList = []
professorList = [[''] for _ in range(9)]
with open('C:\PythonPractice\Python\해커톤(2021-2학기)\professorList.csv','r') as f:
    file_read = csv.reader(f)
    for line in f:
        readList.append(line)
    #과를 포함한 교수님 리스트 (2차원 배열)
    for i in range(9):
        professorList[i] = readList[i].split(',')
    professors = [] #교수님 전체를 담은 리스트 (1차원 배열)
    for i in range(9):
        for j in range(1,len(professorList[i])):
            if len(professorList[i][j])<2:
                continue
            professors.append(professorList[i][j])

yongDriver = '/Users/yongcho/Downloads/chromedriver'
maengDriver  = 'C:\PythonPractice\Python\Web Page Scraping\chromedriver.exe'
yongHeader = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
maengHeader = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'

headers = {'User-Agent' : maengHeader}
browser = webdriver.Chrome(maengDriver) #'./chromedriver'
url = 'https://everytime.kr/'
browser.get(url)

#지정한 위치로 스크롤 하기
# browser.execute_script("window.scrollTo(0,300)") #300크기만큼 스크롤 내림
#화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#파일 오픈
# filename = ""
# file = open(filename, "w", encoding="utf-8-sig",  newline="")
# csvfile = csv.writer(file) #writer로 파일 쓰기

# feature = []
# csvfile.writerow(feature)

#로그인
browser.find_element_by_link_text("로그인").click()
id = 'dragon706'
psw = 'yj028020'
browser.find_element_by_xpath('//*[@id="container"]/form/p[1]/input').send_keys(id)
browser.find_element_by_xpath('//*[@id="container"]/form/p[2]/input').send_keys(psw)
browser.find_element_by_xpath('//*[@id="container"]/form/p[3]/input').click()

#강의 평가 페이지
browser.find_element_by_xpath('//*[@id="menu"]/li[3]/a').click()
for pro in professors:
    # 과목명 입력
    professorName = pro
    browser.find_element_by_class_name('keyword').send_keys(professorName)
    browser.find_element_by_class_name('submit').click()
    # 해당 과목 교수별 강의평가 클릭


    res = requests.get(url+'lecture/search/'+professorName, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(browser.page_source, 'lxml')
    star = browser.find_element_by_class_name('lecture')

    #star = soup.find_all('span',attrs={"class":"on"})
    # starCnt = 0 #별점이 있는 것의 개수
    # for st in star:
    #     if(len(st['style'])==10): #평점이 0점이면 넘긴다.
    #         continue
    #     starCnt += 1

    className = []  # 과목 이름
    classScore = []  # 과목 평점
    classAssign = []  # 과목 과제
    classTeamPl = []  # 과목 팀플
    classGradeRate = []  # 과목 학점비율
    classEval = []  # 강평

    class_feature = {}

    for k in range(1, len(star) + 1):  # 별점이 있는 것들만 반복
        browser.find_element_by_xpath(f'//*[@id="container"]/div/a[{k}]').click()

        soup2 = BeautifulSoup(browser.page_source, 'lxml')

        # 먼저 페이지의 평점을 보고 0점이면 멈춰서 해당 교수님 수업 그만 체크하기.
        classScore.append(browser.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[1]/span/span[1]').text)

        if classScore[-1] == '0':
            browser.back()
            break

        className.append(browser.find_element_by_xpath('//*[@id="container"]/div[2]/h2').text)
        classAssign.append(browser.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[1]/span').text)
        classTeamPl.append(browser.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[2]/span').text)
        classGradeRate.append(browser.find_element_by_xpath('//*[@id="container"]/div[4]/div[1]/div[2]/p[3]/span').text)

        # 강평
        classEval.append([e.text for e in browser.find_elements_by_class_name('text')])

        print(className, classScore, classAssign, classTeamPl, classGradeRate, classEval)

        browser.back()
