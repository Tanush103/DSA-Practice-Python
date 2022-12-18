import heapq
def kthlargest(nums,k):
    return heapq.nlargest(k,nums)[-1]


print(kthlargest([5,3,2,8,10,4],2))