def twosum(nums,target):
  set1=set()
  for i in range(len(nums)):
    temp=target-nums[i]
    if temp in set1:
      return [nums.index(temp),i]
    else:
      set1.add(nums[i])

print(twosum([1,2,3,4],7))