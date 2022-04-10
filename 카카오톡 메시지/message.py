#REST_API = 5931ac3ae1a7daf08eb7253bda790f28
# 라이브러리 호출
import requests
import json
# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"

data = {

}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

#친구 목록 가져오기
url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

result = json.loads(requests.get(url, headers=header).text)
friends_list = result.get("elements")

print(friends_list)

friend_id = friends_list[0].get("uuid")
print(friend_id)

friend_id2 = friends_list[1].get("uuid")
print(friend_id2)

# 카카오톡 메시지
url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

data={
    'receiver_uuids': '["{}","{}"]'.format(friend_id,friend_id2),
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "오늘 저욾칼? 빠큐요",
                                     "link" : {
                                                 "web_url" : "https://op.gg/summoners/kr/%EB%A7%B9%EC%93%B0%EC%98%A4",
                                                 "mobile_web_url" : "https://op.gg/summoners/kr/%EB%A7%B9%EC%93%B0%EC%98%A4"
                                              }
    })
}

response = requests.post(url, headers=header, data=data)
response.status_code