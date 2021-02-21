##함수 선언 부분##

##변수 선언 부분##
default = 0
vc = 0
price = 0
sub = 0
##메인 함수 부분##
if __name__ == "__main__" :
    default, vc, price = map(int, input().split())
    sub = price - vc
    if(sub <= 0 ):
        print(-1)
    else:
        print((default//sub)+1)