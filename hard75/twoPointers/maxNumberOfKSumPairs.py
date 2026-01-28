from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    nums.sort()
    i, j = 0, len(nums) - 1
    count = 0

    while i < j:
        total = nums[i] + nums[j]
        if total == k:
            count += 1
            i += 1
            j -= 1
        elif total > k:
            j -= 1
        else:
            i += 1

    return count

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    k = 5
    print(maxOperations(nums, k))