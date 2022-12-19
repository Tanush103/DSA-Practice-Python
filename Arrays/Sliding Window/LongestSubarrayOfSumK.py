import sys
def longestsubarray(nums,k):
    i=0
    sum=0
    longestsubarray=-sys.maxsize
    for j in range(len(nums)):
        sum+=nums[j]
        if sum==k:
            longestsubarray=max(longestsubarray,j-i+1)
            sum-=nums[i]
            i+=1
        elif sum>k:
            while sum>k:
                sum-=nums[i]
                i+=1
    return longestsubarray

print(longestsubarray([10, 5, 2, 7, 1, 9 ],15))
