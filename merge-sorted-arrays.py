# Merge Sorted Arrays
# Given two sorted lists, merge them into one sorted list. 
# E.g. my_list = [3, 4, 6, 10, 11, 15], your_list = [1, 5, 8, 12, 14, 19]
# merged_list = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]

my_list = [3, 4, 6, 10, 11, 15]
your_list = [1, 5, 8, 12, 14, 19]

# O(nlogn) time
def merge(my_list, your_list):
    return sorted(my_list+your_list)

merged_list = merge(my_list, your_list)

# The above function works, but runs in nlogn time. How can we make it 
# faster? Well, the lists are sorted... we can take advantage of that.
# Let's compare the left most element that has not been merged at every
# comparison. This should be O(n) time complexity, and should work. But 
# remember, we've got to deal with the cases when either your list of my
# list gets exhausted.

def merge(my_list, your_list):
    my_index = 0
    your_index = 0
    merged_list = [None]*(len(my_list)+len(your_list))
    merge_index = 0  

    while merge_index < len(merged_list):
        
        # case: my list exhausted
        if my_index >= len(my_list):
            merged_list[merge_index] = your_list[your_index]
            your_index += 1
        
        # case: your list exhausted
        elif your_index >= len(your_list):
            merged_list[merge_index] = my_list[my_index]
            my_index += 1
            
        # case: merge mine
        elif my_list[my_index] < your_list[your_index]:
            merged_list[merge_index] = my_list[my_index]
            my_index += 1
        
        # case: merge yours
        else:
            merged_list[merge_index] = your_list[your_index]
            your_index += 1

        merge_index += 1
    
    return merged_list

merged_list = merge(my_list, your_list) # works! no index errors 

# We can make the code a bit more concise, then we're done.
def merge(my_list, your_list):
    my_index = 0
    your_index = 0
    merged_list = [None]*(len(my_list)+len(your_list))
    merge_index = 0  

    while merge_index < len(merged_list):
        
        # case: merge from yours
        # since Python uses short-circuit evaluation, if the LHS of the and
        # statement evaluates false, the RHS won't be evaluated since Python
        # knows the and statement will be false. This avoids an index error
        # when your list is exhausted
        
        my_list_exhausted = my_index >= len(my_list)
        your_list_exhausted = your_index >= len(your_list)
        
        # case: merge from yours
        if not your_list_exhausted and (my_list_exhausted or your_list[your_index] < my_list[my_index]):
            merged_list[merge_index] = your_list[your_index]
            your_index += 1
        
        # case: merge from mine
        else:
            merged_list[merge_index] = my_list[my_index]
            my_index += 1
        
        merge_index += 1
    
    return merged_list

merged_list = merge(my_list, your_list)

# Test edge cases
my_list = [-3, 4, 6, 10, 11, 15]
your_list = [-5, -1, 8, 12, 14, 19]
merge(my_list, your_list)

my_list = [0, 0, 0, 0, 0, 0]
your_list = [0, 0, 0, 0, 0, 0]
merge(my_list, your_list)

my_list = [3, 4, 6]
your_list = [1, 5, 8, 12, 14, 19]
merge(my_list, your_list)

my_list = [3, 4, 6, 10, 11, 15]
your_list = [1, 5]
merge(my_list, your_list)

my_list = []
your_list = [1, 5, 8, 12, 14, 19]
merge(my_list, your_list)

my_list = [3, 4, 6, 10, 11, 15]
your_list = []
merge(my_list, your_list)

# What we Learned
# Since the lists we're given is already sorted, we can take advantage of this
# fact and speed up our algorithm from O(nlogn) to O(n), where n is the length
# of the merged list. We can use a POINTER for your list and my list to compare
# between the smallest unmerged numbers. Finally, since Python uses 
# short-circuit evaluation, we were able to combine the statements to make the
# code a bit more concise.