# Given an integer array nums, return all the triplets [nums[i], 
# nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def twosumII(nums,i,res):
    l,r=i+1,len(nums)-1
    while l<r:
        sum=nums[l]+nums[r]+nums[i]
        if sum<0:
            l+=1
        elif sum>0:
            r-=1
        else:
            res.append([nums[l],nums[r],nums[i]])
            l+=1
            r-=1
            
            while(l<r and nums[l]==nums[l-1]):
                l+=1
            while(l<r and nums[r]==nums[r+1]):
                r-=1



def threesum(nums):
    res=[]
    nums.sort()
    for i in range(len(nums)-2):
        
        if i==0 or (i>0 and nums[i-1]!=nums[i]):
            twosumII(nums,i,res)
    return res


# def twosumII(nums,i,res):
#     l=i+1
#     h=len(nums)-1
#     while l<h:
#         sum=nums[l]+nums[h]+nums[i]
#         if sum<0:
#             l+=1
#         elif sum>0:
#             h-=1
#         else:
#             res.append([nums[l],nums[h],nums[i]])
#             l+=1
#             h-=1
#             while l<h and nums[l]==nums[l-1]:
#                 l+=1

print(threesum([-1,0,1,2,-1,-4]))