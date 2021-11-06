#coins
quarter = 25
dime = 10
nickel = 5
penny = 1

print("Input N: ",end="")
N = int(input())

quarter_num = N//quarter
N -= quarter_num * quarter
dime_num = N // dime
N -= dime_num * dime
nickel_num = N // nickel
N -= nickel_num * nickel
penny_num = N // penny
N -= penny_num * penny


print("Quarter:",quarter_num)
print("Dime:",dime_num)
print("Nickel:",nickel_num)
print("Penny:",penny_num)
print("Minimum Number of Coins:",quarter_num+dime_num+nickel_num+penny_num)

