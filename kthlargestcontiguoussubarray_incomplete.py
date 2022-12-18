#Given an array of integers. Write a program to find the K-th largest sum of contiguous subarray
#  within the array of numbers that has both negative and positive numbers.

def kthlargestcontiguous(nums,k):
    sum = []
    sum.append(0)
    sum.append(nums[0])
    for i in range(2, len(nums) + 1):
        sum.append(sum[i - 1] + nums[i - 1])
    print(sum)

print(kthlargestcontiguous([10,-10,20,-40],6))

    


