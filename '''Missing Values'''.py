'''Missing Values

The np.nan is the IEEE 754 floating-point representation of Not a Number. The nan stands for “not a number“, and its primary constant is to act as a placeholder for any missing numerical values in the array.

Write a Python program to replace all missing values with a 0 in the numpy array.

Read data from a csv file. The input file is provided as part of the template code. File name is sample_nan.csv.
11,12,,14
21,,,24
31,32,33,34


Refer Sample Output for formatting Specifications.

Sample Output:

Actual Data
[[11. 12. nan 14.]
 [21. nan nan 24.]
 [31. 32. 33. 34.]]
Missing Values Replaced
[[11. 12.  0. 14.]
 [21.  0.  0. 24.]
 [31. 32. 33. 34.]]'''
import numpy as np 

data=np.genfromtxt("sample_nan.csv",delimiter=',')
print("Actual Data")
print(data)
data[np.isnan(data)]=0
print("Missing Values Replaced")
print(data)
