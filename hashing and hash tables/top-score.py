# Top Scores
# We've made a game more popular than Angry Birds. Players want to see how they
# stack up against other players in the community by highscore, but are
# giving us feedback that their rankings aren't updating fast enough. Given a 
# list of scores and the highest possible score in the game, return a sorted 
# list of scores less than O(nlogn) time.

# e.g. unsorted_scores = [29, 29, 56, 0, 14, 43, 9]
#      HIGHEST_POSSIBLE_SCORE = 100
#      sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE) returns
#      [56, 43, 29, 29, 14, 9, 0]

# We have to beat O(nlogn) time. Even if our list of scores is already sorted,
# we'd have to do a full walkthrough the list to confirm that it was in fact
# fully sorted. So we have to spend at least O(n) time on our sorting function.
# If we're going to do better than O(nlogn), we're probably going to do exactly
# O(n).

# Two common ways to get O(n) runtime are the greedy algorithm and counting. In
# this case, we're not looking to grab a specific value from the input (e.g.
# the largest or the greatest difference) - we're looking to reorder the whole
# set. That doesn't lend itself well to a greedy approach. We can build a list
# score_counts where the indicies represent scores and the values represent how
# many times the score appears. Once we have that, can we generate a sorted 
# list of scores? 
def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
    
    score_counts = [0]*(HIGHEST_POSSIBLE_SCORE + 1) # 0 included as a valid score
    sorted_scores = []
    
    for score in unsorted_scores:
        score_counts[score] += 1
        
    for score in range(len(score_counts)-1, -1, -1):
        for time in range(score_counts[score]):
            sorted_scores.append(score)
    
    return sorted_scores

# O(n) time and space complexity

unsorted_scores = [29, 29, 56, 0, 14, 43, 9]
HIGHEST_POSSIBLE_SCORE = 100
sorted_scores = sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# returned [56, 43, 29, 29, 14, 9, 0]

# What we learned:
# I learned that counting is another commonly used way to reduce runtime down 
# to O(n). It cleverly exploits the implicit information contained in a list,
# and building a sorted list from the counts is trivial.

