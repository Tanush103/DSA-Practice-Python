import sys
def maxsumsubarray(nums,k):
    i=0
    sum,maxSum=0,-sys.maxsize
    for j in range(len(nums)):
        sum+=nums[j]
        window=j-i+1
        if window==k:
            maxSum=max(sum,maxSum)
            sum-=nums[i]
            i+=1
    return maxSum


print(maxsumsubarray([1, 4, 2, 10, 23, 3, 1, 0, 20],4))