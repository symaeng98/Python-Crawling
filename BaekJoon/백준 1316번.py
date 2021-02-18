##함수 선언 부분##

##변수 선언 부분##
N = 0
cnt = 0
Str = []
cont = 1
isGroup = 1
flag = 0
##메인 함수 부분##
if __name__ == "__main__" :
    N = int(input())
    for i in range(0, N):
        Str = input()
        isGroup = 1
        flag = 0
        cont = 1
        for j in range(0, len(Str)):
            flag = 0
            cont = 1
            for k in range(0, j):
                if (Str[j] == Str[k]):
                    flag = 1
                    break

            if(flag == 0):
                for k in range(j, len(Str)):
                    if(Str[j] == Str[k]):
                        if(cont == 0):
                            isGroup = 0
                            break
                    else:
                        cont = 0
            if isGroup == 0 :
                break


        if isGroup == 1 :
            cnt += 1

    print("%d"%cnt)