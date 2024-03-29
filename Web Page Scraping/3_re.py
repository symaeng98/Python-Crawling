import re

#ca?e -> ?에 뭐가 들어갈까
#care, cafe, cake ... 등등

p = re.compile("ca.e")
# '.' (ca.e)은 하나의 문자를 의미 -> care, cafe, cake (O) | caffe (X)
# '^' (^de)은 문자열의 시작을 의미 -> desk, destination (O) | fade (X)
# '$' (se$)은 문자열의 끝을 의미 -> case, base (O) | face (X)

def print_match(m):
    # m = p.match("case") #case가 p와 매칭이 되는가
    # # print(m.group()) #매치되지 않으면 에러가 발생
    #
    if m:
        print("m.group():", m.group()) #일치하는 문자열 반환
        print("m.string:",m.string) #입력받은 문자열
        print("m.start():",m.start()) #일치하는 문자열의 시작 index
        print("m.end():", m.end()) #일치하는 문자열의 끝 index
        print("m.span():", m.span()) #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")
# m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인 - > careless (O)
# print_match(m)

# m = p.search("good care") # search : 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

# lst = p.findall("good care cafe") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)

# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환

# 원하는 형태 : 정규식
# '.' (ca.e)은 하나의 문자를 의미 -> care, cafe, cake (O) | caffe (X)
# '^' (^de)은 문자열의 시작을 의미 -> desk, destination (O) | fade (X)
# '$' (se$)은 문자열의 끝을 의미 -> case, base (O) | face (X)