# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the
#  result must be unique and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


def intersectionofarrays(nums1,nums2):
    ptr1,ptr2=0,0
    res=set()
    nums1.sort()
    nums2.sort()
    while ptr1<len(nums1) and ptr2<len(nums2):
        if nums1[ptr1]<nums2[ptr2]:
            ptr1+=1
        elif nums1[ptr1]>nums2[ptr2]:
            ptr2+=1
        else:
            res.add(nums1[ptr1])
            ptr1+=1
            ptr2+=1
    return list(res)


print(intersectionofarrays([1,2,2,1],[2,2]))


