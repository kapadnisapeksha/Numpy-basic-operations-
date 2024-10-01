'''Set Operations

Write a Python program to perform the following Set Operations on Numpy Arrays.
1) Union of A and B
2) Intersection on A and B
3) A difference B

Get the array size and elements as input from the user. Consider 1-D float array.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of 1st array
2
Enter the elements of first array
1
2
Enter the size of 2nd array
2
Enter the elements of second array
2
3
Union Array
[1. 2. 3.]
Intersection Array
[2.]
Difference Array
[1.]'''
import numpy as np
size1=int(input("Enter the size of 1st array"))
lst=[ ]
print("\nEnter the elements of first array")
for i in range (size1):
    ele=float(input())
    lst.append(ele)

size2=int(input("\nEnter the size of 2nd array"))
lst1=[ ]
print("\nEnter the elements of second array")
for i in range (size2):
    ele2=float(input())
    lst1.append(ele2)

arr1=np.array(lst)
arr2=np.array(lst1)
add=np.union1d(arr1,arr2)
print("\nUnion Array")
print(add)
inter=np.intersect1d(arr1,arr2)
print("Intersection Array")
print(inter)
diff=np.setdiff1d(arr1,arr2)
print("Difference Array")
print(diff)