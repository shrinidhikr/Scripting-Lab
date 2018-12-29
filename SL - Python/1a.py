#Write a python program to read in a list of elements.
#Create a new list that holds all the elements minus the duplicates (Use functions).
def remove_duplicates(numbers):
    newlist = []
    for number in numbers:
       if number not in newlist:
           newlist.append(number)
    return newlist 

arr = list(input("Enter the numbers: ").split())
arr1=[]
for x in arr:
  arr1.append(int(x))
  
no_duplicates = remove_duplicates(arr1)
print(no_duplicates)
list = [val for val in no_duplicates if(val%2==0)]
print(list)

rev = []
for i in range(len(no_duplicates)-1,-1,-1):
  rev.append(no_duplicates[i])
print(rev)
