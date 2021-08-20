import requests
res = requests.get("https://google.com")
# res = requests.get("https://aodtns.tistory.com") #200이 아니면 접근할 수 없는 페이지
print("응답코드 :",res.status_code) #200이면 정상

##if문을 이용해서 접근 유무 확인
# if res.status_code == requests.codes.ok:
#     print("정상임다")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")

##접근할 수 없으면 에러
res.raise_for_status()

print(len(res.text))
print(res.text)

#정보를 받아와서 파일로 만들기
with open("mygoogle.html","w", encoding="utf8") as f:
    f.write(res.text)
