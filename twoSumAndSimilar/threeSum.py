from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
  three_idx = []
  nums.sort()

  for index in range(len(nums) - 1):
      #check if the previous number is the same as the current number
      if index > 0 and nums[index] == nums[index - 1]:
          continue # continue with the next iteration
      i = index + 1 # pointer at the start
      j = len(nums) - 1 # pointer at the end
      while i < j:
          target = nums[i] + nums[j] + nums[index]
          if target == 0:
              three_idx.append([nums[i], nums[j], nums[index]])

              while i < j and nums[i] == nums[i + 1]:
                  i += 1
              while i < j and nums[j] == nums[j - 1]:
                  j -= 1

              i += 1
              j -= 1
          elif target > 0:
              j -= 1
          elif target < 0:
              i += 1
  
  return three_idx

if __name__ == "__main__":
    print(threeSum(None, [-1, 0, 1, 2, -1, -4]))
    print(threeSum(None, []))
    print(threeSum(None, [0]))