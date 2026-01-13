from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    if n == 0:
        return True
    for index in range(len(flowerbed)):
        if flowerbed[index] == 0 and (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0) and (index == 0 or flowerbed[index - 1] == 0):
            flowerbed[index] = 1
            n -= 1
            if n == 0:
                return True
    return False

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))