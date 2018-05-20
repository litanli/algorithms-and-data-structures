# Product of Other Numbers
# Given a list, return a list where each element is the product of all the
# elements at the other indices in the list. E.g. given [1,2,6,5,9] return
# [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5], which is
# [540, 270, 90, 108, 60]
list = [1,2,6,5,9]

# brute method
def products(list):
    results = [None]*len(list)
    for i in range(len(list)):
        indices = []
        product = 1
        for j in range(len(list)):
            if j != i:
                indices.append(j)
        for index in indices:
            product *= list[index]

        results[i] = product
    return results

results = products(list)

# the brute method's runtime is O(n^2). Can we do better? Notice there's a lot
# of products that are repeated in the solution list. We can solve them, keep
# track of them, and reuse them. Like this:

# products_before_index = [1, 1, 1*2, 1*2*6, 1*2*6*5]
# products_after_index = [2*6*5*9, 6*5*9, 5*9, 9, 1]
# note we use 1 at the end and beginning of products_before_index and
# products_after_index respectively.
# Then, results[i] = products_before_index[i]*products_after_index[i]
# We can implemment this in O(n) time.

products_before_index = [None]*len(list)
products_so_far = 1
for i in range(len(list)):
    products_before_index[i] = products_so_far
    products_so_far *= list[i]

products_after_index = [None]*len(list)
products_so_far = 1
for i in range(len(list)-1,-1,-1):
    products_after_index[i] = products_so_far
    products_so_far *= list[i]

# O(n) time function
def products(list):
    products = [None]*len(list)
    for i in range(len(list)):
        products[i] = products_before_index[i]*products_after_index[i]
    return products

res = products(list) # working!

# we can further save some space by just creating one list
def products(list):

    # check to make sure list has at least two elements
    if len(list) < 2:
        raise IndexError('List must have at least 2 elements.')

    products = [None]*len(list)
    products_so_far = 1
    for i in range(len(list)):
        products[i] = products_so_far
        products_so_far *= list[i]

    products_so_far = 1
    for i in range(len(list)-1,-1,-1):
        products[i] *= products_so_far
        products_so_far *= list[i]

    return products

# test case list too small
list = []
list2 = [1]
res = products(list)
res2 = products(list2)

# test edge cases
list3 = [0, 0, 0] # zeroes
list4 = [-1, -1, -1] # negatives
res3 = products(list3)
res4 = products(list4)
