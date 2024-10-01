'''Flattening Arrays

Write a Python program to convert an array of arrays into a flat 1-D Array.

The flatten() function is used to get a copy of a given array collapsed into one dimension.

Steps:
Create the 1-D array using the range function by passing 1 parameter that corresponds to the max value.
Convert it to a 2-D array with m rows and n columns.
Flatten the array.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of 1-D array
10
1-D Array
[0 1 2 3 4 5 6 7 8 9]
Enter m value
5
Enter n value
2
2-D Array
[[0 1]
 [2 3]
 [4 5]
 [6 7]
 [8 9]]
Flattenned Array
[0 1 2 3 4 5 6 7 8 9]'''
import numpy as np 
size=int(input("Enter the size of 1-D array"))
print("\n1-D Array")
ran=np.arange(0,size)
print(ran)
m=int(input("\nEnter m value"))
n=int(input("\nEnter n value"))
rs=np.reshape(ran,(m,n))
print("\n2-D Array")
print(rs)
rf=ran.flatten()
print("Flattenned Array")
print(rf)