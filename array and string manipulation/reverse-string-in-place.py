# Reverse String in Place
# Take a string and reverse the order of its characters in-place. Since strings
# are immutable in Python, the input format will be a list of the characters
# of the string in the order as they appear in the string.

# e.g. input ['s', 't', 'r', 'i', 'n', 'g']
# output ['g', 'n', 'i', 'r', 't', 's']

def reverse(list_of_characters):
    
    left_index = 0
    right_index = len(list_of_characters) - 1
    
    while left_index < right_index:
        
        list_of_characters[left_index], list_of_characters[right_index] = list_of_characters[right_index], list_of_characters[left_index]
        
        left_index += 1
        right_index -= 1
    
characters = ['s', 't', 'r', 'i', 'n', 'g']
reverse(characters)
print(''.join(characters))
# O(n) time and O(1) space


# What we Learned:
# Python strings are immutable. Working in-place saves space; however since it
# destroys your input, be careful. Use it only if you're very space constrained
# or if you're certain the original input is not needed anymore, even for 
# debugging. E.g.

def square_list_in_place(int_list):
    for index, element in enumerate(int_list):
        
        int_list[index] *= element
    
    return int_list
        
def square_list_out_of_place(int_list):
    
    squared_list = [None]*len(int_list)
    
    for index, element in enumerate(int_list):
        squared_list[index] = element**2
    
    return squared_list

original_list = [1, 2, 3, 4]
squared_list = square_list_in_place(original_list)
print(squared_list) # [1, 4, 9, 16]
print(original_list) # [1, 4, 9, 16], confusingly!