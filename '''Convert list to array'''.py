'''Convert list to array

Write a python program to get a list as input from the user and convert it to a numpy array. Print the type of the array and the array.

Consider an integer array.

Refer sample input and output for formatting specifications.
(All text in bold corresponds to input and the rest corresponds to output)

Sample Input and Output:
Enter the size of the list
5
Enter the elements in the list
23
45
12
67
90
class 'numpy.ndarray'
[23 45 12 67 90]'''
import numpy as np 
size=int(input("Enter the size of the list"))
lst=[]
print("\nEnter the elements in the list")
for i in range (size):
    ele=int(input())
    lst.append(ele)

arr=np.array(lst)
print("class 'numpy.ndarray'")
print(arr)