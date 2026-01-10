from typing import List

def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    closest_sum = nums[0] + nums[1] + nums[2]
    for index in range(len(nums) - 2):
        # print(nums[index])
        i = index + 1
        j = len(nums) - 1

        while i < j:
            total = nums[index] + nums[i] + nums[j]

            if abs(closest_sum - target) > abs(total - target):
                closest_sum = total

            if total > target:
                j -= 1
            elif total < target:
                i += 1
            else:
                return closest_sum
    return closest_sum

if __name__ == "__main__":
    print(threeSumClosest(None, [-1, 2, 1, -4], 1)) # Output: 2
    print(threeSumClosest(None, [0, 0, 0], 1)) # Output: 0
    print(threeSumClosest(None, [1, 1, 1], 0)) # Output: 3