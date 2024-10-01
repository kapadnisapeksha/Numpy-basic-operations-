'''Numpy Filtering Operations
Write a  Python program to perform the following operations on a numpy array –
Extract all odd numbers from an array
Get the indexes of all array elements between 5 and 10 ( both 5 and 10 inclusive) from an array.
Replace all odd numbers in an array with -1
Get the array size and elements as input from the user. Consider 1-D float array.
Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output :
Enter the size of the array
4
Enter the elements in the array
1
8
7
3
Input Array
[1. 8. 7. 3.]
All odd numbers array
[1. 7. 3.]
Index of elements between 5 and 10
(array([1, 2]),)
Array with all odd numbers replaced with -1
[-1.  8. -1. -1.]'''
import numpy as np 
size=int(input("Enter the size of the array"))
lst=[ ]
for i in range(size):
    ele=float(input())
    lst.append(ele)
arr=np.array(lst)
print("\nEnter the elements in the array")
print("\nInput Array")
print(arr)
odd_num=arr[arr %2 != 0]
print("All odd numbers array")
print(odd_num)
index_ele=np.where((arr>=5) & (arr<=10))
print("Index of elements between 5 and 10")
print(index_ele)
replace_arr=np.where(arr%2 != 0 ,-1,arr)
print("Array with all odd numbers replaced with -1")
print(replace_arr)
