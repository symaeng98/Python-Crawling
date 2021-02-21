##함수 선언 부분##

##변수 선언 부분##
X = 0
List = []
num = 0
cnt = 0
##메인 함수 부분##
if __name__ == "__main__" :
    X = int(input())

    while cnt < X :
        num += 1
        cnt += num

    cnt -= num

    if num % 2 == 0:
        i = X - cnt
        j = num - i + 1
    else :
        j = X - cnt
        i = num - j + 1

    print(f"{i}/{j}")