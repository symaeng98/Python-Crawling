##함수 선언 부분##

##변수 선언 부분##
height = 0
up = 0
down = 0
dn = 0
day = 0
##메인 함수 부분##
if __name__ == "__main__" :
    up, down, height = map(int,input().split())
    dn = up - down
    if (height -up) % dn == 0:
        day = 0
    else:
        day = 1
    day += (height - up)//dn + 1
    print(day)