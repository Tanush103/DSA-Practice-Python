# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after 
# raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
import math
def trappingrainwater(height):
    count=0
    max_preff,max_suff=-math.inf,-math.inf
    preffix,suffix=[],[]
    for i in range(len(height)):
        max_preff=max(max_preff,height[i])
        preffix.append(max_preff)
    for j in range(len(height)-1,-1,-1):
        max_suff=max(max_suff,height[i])
        suffix.append(max_suff)
    for i in range(len(height)):
        diff=min(preffix[i],suffix[i])-height[i]
        if diff>0:
            count+=diff
    return count

print(trappingrainwater([4,2,0,3,2,5]))
    


