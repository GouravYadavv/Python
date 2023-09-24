"""
    Armstrong numbers are the numbers which are like- 153 becuase 1^3+5^3+3^3=153
"""
num = int(input("Enter a three digit number you want to check for armstrong:"))

temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp = temp // 10
if num == sum:
    print("Yes")
else:
    print("No")
