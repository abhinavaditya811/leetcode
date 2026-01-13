from typing import List

def maxArea(height: List[int]) -> int:
    # print(height)
    max_area = 0
    i = 0
    j = len(height) - 1

    while i < j:
        max_area = max(max_area, (j - i) * min(height[i], height[j]))

        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    
    return max_area

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))