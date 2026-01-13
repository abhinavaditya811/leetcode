def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    if len(str1) == len(str2):
        return str1
    if len(str1) > len(str2):
        return gcdOfStrings(str1[len(str2):], str2)
    return gcdOfStrings(str1, str2[len(str1):])

if __name__ == "__main__":
    str1 = "ABCABC"
    str2 = "ABC"
    print(gcdOfStrings(str1, str2))