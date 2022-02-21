#10.	Write a program to remove duplicate elements from an array
elem = eval(input("Enter List of values : "))
list1=[]
for x in elem:
    if x not in list1:
        list1.append(x)
print("After Removing duplicate elements ",list1)