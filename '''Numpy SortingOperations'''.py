'''Numpy SortingOperations
Write a  Python program to perform the following sorting perations on a numpy array –
Sort the array in ascending order
Sort the array in descending order

Get the array size and elements as input from the user. Consider 1-D float array.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :
Enter the size of the array
5
Enter the elements in the array
2
4
76
43
24
Input Array
[ 2.  4. 76. 43. 24.]
Sorted Array Ascending
[ 2.  4. 24. 43. 76.]
Sorted Array Descending
[76. 43. 24.  4.  2.]'''
import numpy as np 
size=int(input("Enter the size of the array"))
lst=[ ]
print("Enter the elements in the array")
for i in range (size):
    ele=float(input())
    lst.append(ele)
print("Input Array")
arr=np.array(lst)
print(arr)

s_lst=np.sort(arr)
print("Sorted Array Ascending")
print(s_lst)
print("Sorted Array Descending")
r_lst=np.sort(arr)[::-1]
print(r_lst)