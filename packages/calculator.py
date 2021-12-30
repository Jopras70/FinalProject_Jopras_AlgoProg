# Function to calculate and get mean value for a collection of data
def getMean(data):
    n = len(data)
    total = 0
    
    for i in range(n):
        total = total + data[i]
    
    mean = total / n
    return mean

# Function to calculate and get total value for a collection of data
def getTotal(data):
    n = len(data)
    total = 0
    
    for i in range(n):
        total = total + data[i]
    
    return total

# Function to get maximum value in a collection of data and its index
def getMax(data):
    return max(data), data.index(max(data))

# Function to get minimum value in a collection of data and its index
def getMin(data):
    return min(data), data.index(min(data))