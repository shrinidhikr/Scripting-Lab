#!/usr/bin/env python
#Introduction to Python : Classes & Objects, Functions
#b)   Write a recursive python function that has a parameter representing a list of integers
#and returns the maximum stored in the list.
#Hint: The maximum is either the first value in the list or the maximum of the rest of
#the list whichever is larger. If the list only has 1 integer, then its maximum is this
#single value, naturally. Demonstrate with some examples.

# Note : Handle all other corner cases which are not handled here

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

'''def main():
	try:
		list = eval(input("Enter a list of numbers: "))
		print ("The largest number is: ", Max(list))
	except SyntaxError:
		print ("Please enter comma separated numbers")
	except:
		print ("Enter only numbers")

main()'''

arr = list(input("Enter the numbers: ").split())
arr1=[]
for x in arr:
  arr1.append(int(x))
print ("The largest number is: ", Max(arr1))
