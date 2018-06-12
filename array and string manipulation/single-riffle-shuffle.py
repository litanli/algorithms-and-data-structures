import random

# Single Riffle Shuffle
# Write a function to tell us if a full deck of cards, shuffled_deck, is a 
# singe riffle shuffle of two other halves half1 and half2.

# e.g. input: half1 = [3, 5, 8, 52, 2, ..., 43]
#             half2 = [4, 16, 23, 42, ..., 39]
#             shuffled_deck = [3, 5, 4, 8, 52, 16, 23, 42, 2, ..., 43, 39]
#      output: is_single_riffle(shuffled_deck) returns True
#      where each card of the standard deck is represented by an integer 
#      between 1 to 52 inclusive. 


# use recursion! Remember base case (stop criterion)
def is_single_riffle(half1, half2, shuffled_deck):
    
    # base case
    if len(shuffled_deck) == 0:
        
        return True
    
    # recursion
    if len(half1) and shuffled_deck[0] == half1[0]:
        
        # remove that top card from half1 and shuffled_deck, it being 
        # accounted for
        return is_single_riffle(half1[1:], half2, shuffled_deck[1:])
    
    elif len(half2) and shuffled_deck[0] == half2[0]:
        
        # similarly
        return is_single_riffle(half1, half2[1:], shuffled_deck[1:])
    
    else:
        return False

deck = [i for i in range(1, 53)]        
random.shuffle(deck) # shuffles in-place
half1 = deck[0:26] 
half2 = deck[26:52]

is_single_riffle(half1, half2, deck) # True

deck[0], deck[51] = deck[51], deck[0] # mess up the deck
is_single_riffle(half1, half2, deck) # False

# What we Learned:
# We broke down the problem to a sub-problem, and saw that the top card of a
# single-riffle-shuffled deck must be either the top card from half1 or half2.
# From there, we "account for" the checked card by removing it and then used
# a recursive approach with an appropriate base case - if the whole deck has 
# checked without problem, return True.

# list slicing list[1:] for a length 1 list returns empty list.
half1 = [2]
half1[1:] # returns []
# Using the recursion like we did, we eventually get to the point when either 
# half1 or half2 has only 1 card left. Then, the half[1:] slice we give to the 
# next function call is an empty list.