# reservoir sampling. Obtain uniform sample of k data points from a large data
# set whose size is unknown
import random
import matplotlib.pyplot as plt
import numpy as np

k = 50 # reservoir size
N = 10000 # population size
data = [random.gauss(0,1) for i in range(0, N)] 

#plt.hist(data)
#plt.title("Showing Distribution of Data") 

# get a uniform sample
def get_reservoir(k, data):
    res = [None]*k
    
    for i in range(k):
        res[i] = data[i]
    
    for i in range(k, len(data)):
        if random.randint(0,1) < k/i:
            # drop a random collected datapoint and collect ith datapoint
            res[random.randint(0, k-1)] = data[i]
    
    return res
    
reservoir = get_reservoir(k, data)

plt.hist(reservoir)
plt.title("Distribution of Reservoir is similar to original data distribution due to uniform sampling.")