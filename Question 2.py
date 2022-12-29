# Question 2. If choice of user = 2, print the pattern - > 

# * * * * *
#  * * * *
#   * * *
#    * *
#     *                       
#    _ _
#   _ _ _
#  _ _ _ _
# _ _ _ _ _

# If choice of user = 1, print the pattern - > 

# * * * * *
#  * * * *
#   * * *
#    * *
#     * 

# If choice of the user = any_other_choice_other_than_1_and_2, print the message - >

# 'Invalid Input'

#Program:

#If the user choice is 1

def user_choice_1(n):
    for i in range(n,0,-1):
        for j in range(0,n-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()

#If the user choice is 2
def user_choice_2(row):
    #upper half
    for i in range(row,0,-1):
        for j in range(0,row-i):
            print(end=" ")
        for j in range(0,i):
            print("*",end=" ")
        print()

# Lower-half
    for i in range(2, row+1):
        for j in range(row-i):
            print(end=" ")
        for j in range(0,i):
            print("-", end=" ")
        print()

user_input=int(input())
if user_input==1:
    user_choice_1(5)
elif user_input==2:
    user_choice_2(5)
else:
    print("Invalid Input")