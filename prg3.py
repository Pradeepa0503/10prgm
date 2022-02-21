#3.	Write a program to check given number is prime or not
n= int(input("Enter a number to check prime no or not: "))
flag = False
if n > 1:
   for i in range(2, n):
        if (n % i) == 0:
            flag = True            
if flag:
    print("No")
else:
    print("yes")
