# Permutation Palindrome
# Write a function that checks to see if any permutation of an input string is 
# a palindrome. You can assume all input strings are lower-case.

# e.g. "civic" should return True
#      "viicc" should return True
#      "civil" should return False
#      "viilc" should return False

# a brute force approach checks each of the n! permutations to see if it's a 
# palindrome. Each check takes n time, for a total run time of O(n!n). How can 
# we improve the run time? 

# Any permutation that is a palindrome must have an even number of each of its 
# letters except its middle letter (if permutation has odd number of letters) 
# which must appear an odd number of times. We could use a dictionary to track 
# the multiplicity of each letter. 

# Actually, we just need to check that no more than one letter appears an odd
# number of times. We create a set, which contains the letters with an odd
# multiplicity. O(n) time!

def is_any_permutation_palindrome(word):
    
    unpaired_letters = set()
    
    for letter in word:
        if letter not in unpaired_letters:
            unpaired_letters.add(letter)
        else:
            unpaired_letters.remove(letter) 
        
    return len(unpaired_letters) <= 1
    
is_any_permutation_palindrome("civic")
is_any_permutation_palindrome("viicc")
is_any_permutation_palindrome("civil")
is_any_permutation_palindrome("viilc")

# What we learned:
# Again, we saw that asking "can a dictionary or set make our solution faster"
# led to a faster answer compared to the brute force, which is almost always
# not optimized. Broke down the problem to a simple rule.