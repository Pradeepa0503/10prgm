#4.	Write a program to print first n numbers in the Fibonacci series
n1, n2 = 0, 1
n=int(input('enter a number of terms:'))
count = 0
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1