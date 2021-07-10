##함수 선언 부분

##변수 선언 부분
square = []

##메인 함수 부분
if __name__ == "__main__":
    N = int(input())
    square = [[int(x) for x in input().split()]for y in range(N)]
