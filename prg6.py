#6.	Write a program to count occurrence of a given characters in string.
word=input("enter a word: ")
n=input("enter a character to find: ")
if (word.find(n)!=-1):
    print(n, "yes")
else:
    print(n," No")    
