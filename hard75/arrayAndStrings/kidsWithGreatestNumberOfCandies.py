from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    temp = []
    for index in range(len(candies)):
        if candies[index] + extraCandies >= max(candies):
            temp.append(True)
        else:
            temp.append(False)

    return temp

if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))