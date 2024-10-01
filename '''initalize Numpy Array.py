'''initalize Numpy Array

Write a python program to initialize a numpy array with values [1,2,3,4,5,6,7,8,9,10] and print the array and its type.

Refer sample output for fomatting specifications.

Sample Output:

Array
[ 1  2  3  4  5  6  7  8  9 10]
Array Type
class 'numpy.ndarray'''

import numpy as np 
arr=[1,2,3,4,5,6,7,8,9,10]
arr1=np.array(arr)
print("Array")
print(arr1)
print("Array Type")
print("class 'numpy.ndarray'	")