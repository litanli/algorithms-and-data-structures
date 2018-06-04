# Inflight Entertainment
# Some passengers on longer flights like to watch a second movie after their
# first one ends, but don't get to see the ending of the second before the
# plane lands. Write a simple recommendation system that checks to see if
# there are two movies whose total runtime equals exactly the flight time.

# Assume users will watch exactly two movies
# Don't make users watch any same movie twice
# Optimize for runtime over memory

# e.g. flight_length = 180 # minutes
#      movie_lengths = [122, 100, 110, ..., 80] # list of movies' lengths in minutes
#      recommend(flight_length, movie_lengths) # returns True

# An O(n^2) runtime solution is simply
def can_two_movies_fill_flight(flight_length, movie_lengths):
    
    for i in range(len(movie_lengths)):
        for j in range(len(i+1, movie_lengths)):
            if movie_lengths[i] + movie_lengths[j] == flight_length:
                return True
    
    return False

# How can we make this faster? We can sort the movies by length in nlogn time,
# then look for movie times that match our criterion using binary search (logn
# time). The runtime of our function would be O(nlogn).

# Can we do better and go down to linear time? Let's try to do away with the 
# inner for loop. The exact length of the second movie can be determined by 
# subtracting the length of the first movie from the flight time. We can turn
# our movie lengths into a set, then look up the set for the length we want in
# constant time. The total runtime would be O(n); O(n) space.
def can_two_movies_fill_flight(flight_length, movie_lengths):
    
    movie_lengths_seen = set() # start with empty set
    
    for first_movie_length in movie_lengths:
        
        matching_second_movie_length = flight_length - first_movie_length
        
        if matching_second_movie_length in movie_lengths_seen: # O(1) lookup
            return True
        
        movie_lengths_seen.add(first_movie_length)
        
    return False


# What we learned:
# Adding an element to and looking up an element in a set take constant time.
# Since we knew exactly what number we were looking for in the set, we could
# loop through the movie lengths only once, taking constant time in each 
# iteration. Because of their constant lookup time, using hash-based data 
# structures, like dictionary or sets, is so common in coding challenge 
# solutions that you should always ask yourself from the start "Can I save time 
# by using a dictionary?"