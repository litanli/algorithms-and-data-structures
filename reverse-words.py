# Reverse Words
# Write a function reverse_words() that takes a message and reverses the order 
# of its strings in-place. The message is given as a list of characters, with 
# spaces separating the words. Note we use a list of characters because strings 
# are immutable in Python.

# e.g. message = ['l', 'a', 'u', 'n', 'd', 'r', 'y', ' ',
#              'y', 'o', 'u', 'r', ' ', 'd', 'o']
#      reverse_words(message) 
#      print(''.join(message)) # prints 'do your laundry' 

# The trick here is to first reverse all the characters. If you do that,
# you'll get ['o', 'd', ' ', 'r', 'u', 'o', 'y', ' ',
#              'y', 'r', 'd', 'n', 'u', 'a', 'l']
# That is, you get the words in order, but each word is reversed.
# We then just need to reverse each word.

def reverse_characters(list_of_characters, left_index, right_index):
    
    while left_index < right_index:
        
        list_of_characters[left_index], list_of_characters[right_index] = list_of_characters[right_index], list_of_characters[left_index]
        
        left_index += 1
        right_index -= 1


def reverse_words(message):
    
    reverse(message)
    current_word_start_index = 0
    
    for i in range(len(message)+1):
        
        # found end of current word. Note, we are lucky that Python uses short
        # circuiting. If the first condition is true, the second is not
        # evaluated. If it was, we would have an index error.
        if i == len(message) or message[i] == ' ':
    
            reverse_characters(message, current_word_start_index, i - 1)
            current_word_start_index = i + 1
        
message = ['l', 'a', 'u', 'n', 'd', 'r', 'y', ' ', 'y', 'o', 'u', 'r', ' ', 'd', 'o']
reverse_words(message)
print(''.join(message))    

# O(n) time, O(1) space
    

# What we Learned:
# We tried solving a simpler problem first, namely reversing the characters of
# the whole message, and we found that it did half the work towards solving the
# problem.
    

