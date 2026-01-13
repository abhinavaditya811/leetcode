from typing import List

def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        if nums[slow] != 0:
            slow += 1

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    print(nums)