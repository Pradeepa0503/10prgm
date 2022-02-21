#2.	Write a program to find sum of digits of a number.
n=int(input("enter a number to find sum: "))
def getSum(n):
    sum=0
    while (n > 0):
     sum = sum + (n % 10)
     n = n//10
    return sum
print(getSum(n))
