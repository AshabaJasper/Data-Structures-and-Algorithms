#Arrays are containers which are able to store more than one item
#at the same time

#The difference between Arrays and Lists in python is arrays can only store one data type
#How to use arrays

#using the array module

#method one:
import array
#can be used as #import array as arr
#from array import *

#create and array with
a = array.array('i', [1, 2, 3,4])

print(a)

# printing original array
print("The new created array is : ")
for i in range(0, len(a)):
    print(a[i], end=" ")
print() #for the purposes of skipping a line

#array indexing
import array as arr

my_array=arr.array("i",[12,13,24,25,56])

print(my_array)
print(my_array[0]) #accesses the first element
print(my_array[-1]) #accesses the last element





