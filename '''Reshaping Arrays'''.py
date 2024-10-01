'''Reshaping Arrays


Write a Python program to convert a 1-D array to a 2-D array with m rows and n columns.

Create the 1-D array using the range function by passing 1 parameter that corresponds to the max value.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of 1-D array
6
1-D Array
[0 1 2 3 4 5]
Enter m value
3
Enter n value
2
2-D Array
[[0 1]
 [2 3]
 [4 5]]'''
import numpy as np 
size=int(input("Enter the size of 1-D array"))
print("\n1-D Array")
arr=np.arange(0,size)
#print("1-D Array")
print(arr)
print("Enter m value")
m=int(input())
print("Enter n value")
n=int(input())
print("2-D Array")
two_d=np.reshape(arr,(m,n))
print(two_d)