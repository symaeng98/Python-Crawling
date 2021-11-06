##main##
print("Input N: ",end="")
n = int(input())
print("Input increasing elements: ",end="")
arr = [int(i) for i in input().split()] ##input elements
print("Find an element: ",end="")
find_element = int(input())
find_element_location = -1 #initialize

i = 0
j = n-1
while i < j-1:
    l = i+(j-i)//3 ##modified
    u = i+2*(j-i)//3
    if find_element > arr[u]:
        i = u + 1
    elif find_element > arr[l]:
        i = l + 1
        j = u
    else:
        j = l
if find_element == arr[i]:
    find_element_location = i
elif find_element == arr[j]:
    find_element_location = j
else:
    find_element_location = -1
if(find_element_location==-1): ##if not found
    print("The element is not found:", find_element_location+1)
else:
    print("Element's location:", find_element_location+1)
