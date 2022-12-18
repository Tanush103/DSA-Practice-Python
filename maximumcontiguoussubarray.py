
import math
def maxsumcontiguoussubarray(arr):
    
    sum,maxsum=0,-math.inf
    for i in range(len(arr)):
        
        sum+=arr[i]
        print(sum)
        maxsum=max(sum,maxsum)
        if sum<0:
            sum=0
    return maxsum


#Kadane's Algoritm
def maxsumcontiguoussubarraykadanes(arr):
    current_subarray,max_subarray=arr[0],arr[0]
    for i in range(1,len(arr)):
        current_subarray=max(arr[i],current_subarray+arr[i])
        max_subarray=max(current_subarray,max_subarray)
    return max_subarray

#optimized
def maxsumcontiguoussubarrayoptimized(arr):
    for i in range(1,len(arr)):
        if arr[i-1]>0:
            arr[i]+=arr[i-1]
    return max(arr)
print(maxsumcontiguoussubarrayoptimized([-2,1,-3,4,-1,2,1,-5,4]))
print(maxsumcontiguoussubarraykadanes([-2,1,-3,4,-1,2,1,-5,4]))
