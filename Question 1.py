# Question 1
# Write a for loop to iterate through the list A = [1, 2, 3, 4, 5, 6]. 
# Square each element of the list in one by one fashion and print them. After the end of the iteration, print - "The sequence has ended".

#Input : List of Integers
#Output : Squares of Integers

input_list= list(map(int,input().split()))
for element in input_list:
    print(element*element)
    print()
print("The Sequence has ended")

