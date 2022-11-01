#Arrays are containers which are able to store more than one item
#at the same time

#The difference between Arrays and Lists in python is arrays can only store one data type
#How to use arrays

#using the array module

#method one:
import array

#create and array with
a = array.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ")
for i in range(0, 3):
    print(a[i], end=",")
print()

