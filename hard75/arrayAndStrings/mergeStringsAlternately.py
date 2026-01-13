def mergeAlternately(word1: str, word2: str) -> str:
    len1 = len(word1)
    len2 = len(word2)
    word3 = ""
    temp = max(len1, len2)
    i = 0
    j = 0
    while i < temp or j < temp:
        if i != len1:
            word3 += word1[i]
            i += 1
        if j != len2:
            word3 += word2[j]
            j += 1
        
        if i == temp or j == temp:
            break
    return word3

if __name__ == "__main__":
    word1 = "abc"
    word2 = "pqr"
    print(mergeAlternately(word1, word2))