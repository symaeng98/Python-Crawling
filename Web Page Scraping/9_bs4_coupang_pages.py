import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}

for i in range(1,6):
    url = f"https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={i}&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    for item in items:

        #광고 제품 제외
        ad_badge = item.find("span",attrs={"class":"ad-badge-text"})
        if ad_badge:
            print("  <광고 상품 제외함다>")
            continue
        name = item.find("div", attrs={"class":"name"}).get_text()

        #애플 제품 제외
        if "Apple" in name:
            print("  <애플 상품 제외함다>")
            print(name)
            continue

        price = item.find("strong",attrs={"class":"price-value"}).get_text() #가격


        #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        rate = item.find("em", attrs={"class": "rating"}) #평점(rating)
        if rate:
            rate = rate.get_text()
        else:
            print("평점 없음\n")
            continue

        rate_cnt = item.find("span", attrs={"class": "rating-total-count"})# 평점 수(rating-total-count)
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
            rate_cnt = rate_cnt[1:-1]
        else:
            print("평점 수 없음\n")
            continue
        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            print(f"이름: {name}\n 가격: {price}\n 평점: {rate}\n 리뷰 수: {rate_cnt}\n")