##함수 선언 부분
DIVIDE = 1000000007
def C(N, K):
    if N == K or K == 0:
        return 1
    else:
        return (C(N-1,K-1)%DIVIDE + C(N-1, K)%DIVIDE)%DIVIDE

##변수 선언 부분


##메인 함수 부분
if __name__ == "__main__":
    N, K = map(int,input().split())
    if N == K or K == 0:
        print(1)
    else:
        print(C(N, K))