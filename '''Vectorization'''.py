'''Vectorization
Numpy Arrays are important because they enable you to express batch operations on data without writing any for loops. This is usually called vectorization.

Write a Python program to illustrate vectorization by squaring all elements in the numpy array.

Get the array size and elements as input from the user. Consider 1-D float array.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of the array
5
Enter the elements in the array
2
4
6
8
10
Input Array
[ 2.  4.  6.  8. 10.]
Squared Array
[  4.  16.  36.  64. 100.]'''
import numpy as np 
size=int(input("Enter the size of the array"))
lst=[ ]
print("Enter the elements in the array")
for i in range (size):
    ele=float(input())
    lst.append(ele)
arr=np.array(lst)
print("Input Array")
print(arr)
sqr_arr=arr**2
print("Squared Array")
print(sqr_arr)