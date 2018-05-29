# Merge Meeting Times
# Given a list of meeting times, return a list of times when people are
# unavailable. Meeting times are given as a tuple of two integers 
# (start_time, end_time), each representing the number of 30 min. blocks after 
# 9 AM. E.g. (0,1) represents a meeting from 9-9:30AM.

# e.g. input [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
# return [(0, 1), (3, 8), (9, 12)]

meeting_times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

def merge_ranges(meetings):
    
    # if we compare each meeting time to every other meeting time, the 
    # runtime would be O(n^2).
    
    # if we sorted the meetings by start time, we can go then go through the
    # list of meetings times in ONE pass in O(n) time. But sorting takes 
    # O(nlogn), so our run time improves to O(nlogn).
    # The space complexity is worst-case O(n), where every meeting in the list
    # does not overlap and we create a new list of size n.
    
    # Compare every meeting to the meeting with the closest start time
    sorted_meetings = sorted(meetings)
    
    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]
    
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        
        # if current and last meeting overlap, use the later of the two end times
        if last_merged_meeting_end >= current_meeting_start:
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))          
    
    return merged_meetings
    

merged = merge_ranges(meeting_times)

# What we learned
# We saw we might be able to do better than O(n^2) time. We tried going through
# the list just once - a greedy approach, but required the times to be sorted 
# by start time, which takes O(nlogn), so our run time is O(nlogn). Note that
# if we were given sorted lists, our greedy approach takes O(n) time. 
