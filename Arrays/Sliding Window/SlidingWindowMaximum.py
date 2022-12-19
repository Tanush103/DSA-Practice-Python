# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array 
# to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

 

# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from collections import deque
def maxSlidingwindow(nums,k):
    q=deque()
    i=0
    list1=[]
    for j in range(len(nums)):
        while q and nums[q[-1]]<nums[j]:
            q.pop()
        q.append(j)
        if i>q[0]:
            q.popleft()
        if j-i+1==k:
            list1.append(nums[q[0]])
            i+=1
    return list1

print(maxSlidingwindow([1,3,-1,-3,5,3,6,7],3))

    