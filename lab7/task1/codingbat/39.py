def max_end3(nums):
  if(nums[0] > nums[len(nums) - 1]):
    a = []
    a.append(nums[0])
    a.append(nums[0])
    a.append(nums[0])
  else:
    a = []
    a.append(nums[len(nums) - 1 ])
    a.append(nums[len(nums) - 1 ])
    a.append(nums[len(nums) - 1 ])
  return a