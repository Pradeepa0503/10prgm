#1.	Write a program to reverse an integer
Number = int(input("please enter a number: "))
Rev = 0
while(Number > 0):
   Remin = Number %10
   Rev = (Rev*10) + Remin
   Number = Number //10.
print("\n Reverse of entered number is = %d" %Rev)