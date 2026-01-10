from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    pair_index = {}

    for index, x in enumerate(nums):
        diff = target - x
        if diff in pair_index:
            return [index, pair_index[diff]]
        pair_index[x] = index

if __name__ == "__main__":
    print(twoSum(None, [2, 7, 11, 15], 9))
    print(twoSum(None, [3, 2, 4], 6))
    print(twoSum(None, [3, 3], 6))

## Example Run:

# Let's say:

# nums = [2, 7, 11, 15]
# target = 9

# **Step-by-step:**

# 1. `index=0, x=2`
#     - `diff = 9 - 2 = 7`
#     - 7 not in `pair_index`
#     - Store `2:0` → `pair_index = {2: 0}`
# 2. `index=1, x=7`
#     - `diff = 9 - 7 = 2`
#     - 2 is in `pair_index` at index 0
#     - Return `[1, 0]`