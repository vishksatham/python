"""
Learn about lists, tuples, and dictionaries.
Understand how to manipulate these data structures (e.g., appending to a list, updating dictionary values).
"""

nums = [] 

while True:

    userIn = input("Enter an integer (input 'done' to finish): ")
    
    if(userIn != 'done'):

        num = int(userIn) 
        
        nums.append(num)

    elif userIn == 'done':
        break
   
nums.sort(reverse = True)
nums_tuple = tuple(nums)

print("Numbers in descending order: " + str(nums_tuple))