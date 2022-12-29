# Question 3. Create a tuple t_1 = (1, 4, 9, 16, 25, 36). 
# Square each element of the tuple using tuple comprehension and store the result in a variable known as t_modified. 
# Find element at index position 4 of the tuple t_modified. Now slice the modified tuple in such a way that the sliced 
#  tuple includes only elements from index position 1 to 3 and store this sliced tuple in a variable known as t_sliced. 

# Final output should be:

# t_1: (1, 4, 9, 16, 25, 36)
# t_modified: (1, 16, 81, 256, 625, 1296)
# Element at index postiion 4 of t_modified: 625
# t_sliced: (16, 81, 256)

#Input: Tuple
#output: Modified Tuple
import math
tup=tuple(map(int,input().split(",")))
# #Tuple comprehension
t_modified = tuple(int(math.pow(val, 2)) for val in tup)
#Indexing of Tuple
val_at_4th_index=t_modified[3]
#slicing of tuple
t_sliced=t_modified[1:4]
#printing the values
print(t_modified)
print(val_at_4th_index)
print(t_sliced)

