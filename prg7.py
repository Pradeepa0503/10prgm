#7.	Write a program to check a String is palindrome or not.
s =input("please enter a word: ")
def isPalindrome(s):
    return s == s[::-1]
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
