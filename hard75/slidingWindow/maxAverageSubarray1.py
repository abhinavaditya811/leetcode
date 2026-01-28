from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    total = sum(nums[:k])
    avg = total/k

    ans = avg

    for i in range(len(nums) - k):
        total -= nums[i]
        total += nums[i + k]

        avg = total/k
        ans = max(ans, avg)

    return ans

if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(findMaxAverage(nums, k))