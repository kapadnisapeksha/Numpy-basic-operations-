'''Array Slicing and Indexing
Write a menu driven Python program to perform the following operations on a numpy array.
Template code is provided. Use the 2-D array initialised in the template code to perform the following operations.

1)Get a subarray from the given array
2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)
3)Swap 2 rows from the given 2-D array(swap rows 2 and3)
4)Reverse the rows of the given 2-D array
5)Reverse the columns of the given 2-D array
Refer Sample Input and Output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output 1:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
Menu:
1)Get a subarray from the given array
2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)
3)Swap 2 rows from the given 2-D array(swap rows 2 and3)
4)Reverse the rows of the given 2-D array
5)Reverse the columns of the given 2-D array
Enter your choice
1
Enter low row range
2
Enter high row range
4
Enter low column range
2
Enter high column range
4
[[10 11]
 [14 15]]
Sample Input and Output 2:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
Menu:
1)Get a subarray from the given array
2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)
3)Swap 2 rows from the given 2-D array(swap rows 2 and3)
4)Reverse the rows of the given 2-D array
5)Reverse the columns of the given 2-D array
Enter your choice
2
[[ 1  0  2  3]
 [ 5  4  6  7]
 [ 9  8 10 11]
 [13 12 14 15]]

Sample Input and Output 3:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
Menu:
1)Get a subarray from the given array
2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)
3)Swap 2 rows from the given 2-D array(swap rows 2 and3)
4)Reverse the rows of the given 2-D array
5)Reverse the columns of the given 2-D array
Enter your choice
3
[[ 0  1  2  3]
 [ 8  9 10 11]
 [ 4  5  6  7]
 [12 13 14 15]]

Sample Input and Output 4:

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
Menu:
1)Get a subarray from the given array
2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)
3)Swap 2 rows from the given 2-D array(swap rows 2 and3)
4)Reverse the rows of the given 2-D array
5)Reverse the columns of the given 2-D array
Enter your choice
4
[[12 13 14 15]
 [ 8  9 10 11]
 [ 4  5  6  7]
 [ 0  1  2  3]]

Sample Input and Output 5:

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]]
Menu:
1)Get a subarray from the given array
2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)
3)Swap 2 rows from the given 2-D array(swap rows 2 and3)
4)Reverse the rows of the given 2-D array
5)Reverse the columns of the given 2-D array
Enter your choice
5
[[ 3  2  1  0]
 [ 7  6  5  4]
 [11 10  9  8]
 [15 14 13 12]]'''
import numpy as np 
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Menu:")
print("1)Get a subarray from the given array"
"\n2)Swap 2 columns from the given 2-D array (swap columns 1 and 2)"
"\n3)Swap 2 rows from the given 2-D array(swap rows 2 and3)"
"\n4)Reverse the rows of the given 2-D array"
"\n5)Reverse the columns of the given 2-D array")
ch=int(input("Enter your choice"))
if (ch==1):
    l_row=int(input("Enter low row range"))
    h_row=int(input("\nEnter high row range"))
    l_col=int(input("\nEnter low column range"))
    h_col=int(input("\nEnter high column range"))
    subarray=arr[l_row:h_row,l_col:h_col]
    print(subarray)
