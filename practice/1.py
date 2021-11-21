def binary_search_iter(A, key, low, high):
    while(low <= high):
        middle = (low + high)//2
        if key == A[middle]:
            return middle
        elif key>A[middle]:
            low=middle+1
        else:
            high = middle - 1
    return None

A = [2,6,11,13,18,20,22,27,29,30,34,38,41,42,45,47] #16개 원소
key = 13 #찾으려는 값
print(binary_search_iter(A,13,0,15)) #인덱스 0부터 15까지중에 key값의 인덱스 찾으려고 함
#print를 해줘야 함수가 return한 값의 결과가 출력이 돼요