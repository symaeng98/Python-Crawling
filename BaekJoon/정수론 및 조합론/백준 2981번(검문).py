##함수 선언 부분##


##변수 선언 부분##
A = []
min = 0
min_i = 0
##메인 함수 부분##
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        A.append(int(input()))
    A.sort()
    min = A[1]-A[0]
    for i in range(1,N):
        if min > A[i]-A[i-1]:
            min = A[i] - A[i-1]
            min_i = i

    for i in range(2,min+1):
        if min % i == 0:
            print("%d"%i,end=" ")
    # i = 2
    # while i <= max(A):
    #     isRight = 1
    #     ans = A[0] % i
    #     for j in range(1, len(A)):
    #         if A[j] % i == ans:
    #             continue
    #         else:
    #             isRight = 0
    #     if isRight:
    #         print("%d" % (i), end=" ")
    #
    #     i += 1