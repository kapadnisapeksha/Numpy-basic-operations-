'''Numpy Array Mathematical Operations
Write a  Python program to perform the following operations on a numpy array – Finding the mean, Finding the maximum element, Finding the minimum element and to round all the array elements to 1 decimal place.

Get the array size and elements as input from the user. Consider 1-D float array.

Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.

Sample Input and Output :

Enter the size of the array
4
Enter the elements in the array
2.56
1.145
7.897
4.321
Mean of the array
3.98075
Maximum Element in the array
7.897
Minimum Element in the array
1.145
Rounded array
[2.6 1.1 7.9 4.3]'''
import numpy as np 
size=int(input("Enter the size of the array"))
print("\nEnter the elements in the array")
lst=[ ]
for i in range ( size):
    ele=float(input())
    lst.append(ele)
lst_mean=np.mean(lst)
print("Mean of the array")
print(round(lst_mean,2))

lst_max=np.max(lst)

print("Maximum Element in the array")
print(lst_max)
lst_min=np.min(lst)

print("Minimum Element in the array")
print(lst_min)
rnd_lst=np.round(lst,1)
print("Rounded array")
print(rnd_lst)
