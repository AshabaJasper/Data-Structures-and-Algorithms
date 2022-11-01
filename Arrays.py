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
for i in range(len(a)):
    print(a[i], end=" ")
print() #for the purposes of skipping a line
print("--------------------")
#array indexing
import array as arr

#syntax of array module:
# {variable=array.array("unicode_character",[array elements]")
my_array=arr.array("i",[12,13,24,25,56])

print(my_array)
print(my_array[0]) #accesses the first element
print(my_array[-1]) #accesses the last element
print("*************")
#searching through an array

from array import *

my_second_array=arr.array('i',[9,23,45,6,5])

#returns the index of the element
#syntax, array_name.index(element)
print(my_second_array.index(23))
print("************")

#looping through an array
import array as arr

b=arr.array("q",[1,2,3,4,5,6])

for i in b:
    print(i)
# for i in range(0,len(my_second_array)):
#     print(my_second_array[i])


