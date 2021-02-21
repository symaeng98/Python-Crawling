##함수 선언 부분##

##변수 선언 부분##
N = 0
cnt = 1
num = 0
six = 6
##메인 함수 부분##
if __name__ == "__main__" :
    N = int(input())
    while True :
        if N == 1:
            print(1)
            break

        elif N >= six * num + 2 :
            num += cnt
            cnt += 1
            if N <= six * num + 1 :
                print(cnt)
                break


