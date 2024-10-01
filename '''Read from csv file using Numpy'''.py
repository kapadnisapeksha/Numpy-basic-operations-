'''Read from csv file

Write a python program to read from a csv file into a numpy array. Print the array.
The name of the input csv file is sample_data.csv. It is provided as part of the template code.

Refer sample input and output for formatting specifications.

Sample Input:
#crete
File Input. (sample_data.csv)
Username,Identifier,First name,Last name
booker12,9012,Rachel,Booker
grey07,2070,Laura,Grey
johnson81,4081,Craig,Johnson
jenkins46,9346,Mary,Jenkins
smith79,5079,Jamie,Smith

Sample Output:

[['Username' 'Identifier' 'First name' 'Last name']
 ['booker12' '9012' 'Rachel' 'Booker']
 ['grey07' '2070' 'Laura' 'Grey']
 ['johnson81' '4081' 'Craig' 'Johnson']
 ['jenkins46' '9346' 'Mary' 'Jenkins']
 ['smith79' '5079' 'Jamie' 'Smith']]'''
import numpy as np 
import pandas as pd 
array=np.genfromtxt("sample_data.csv",delimiter=',',dtype=str)
print(array)