def isSubsequence(s: str, t: str) -> bool:
    slow = 0
    count = 0

    if len(s) == 0:
        return True

    for fast in range(len(t)):
        if s[slow] == t[fast]:
            count += 1
            slow += 1

        if slow == len(s):
            break

    return count == len(s)

if __name__ == "__main__":
    s = "abc"
    t = "ahbgdc"
    print(isSubsequence(s, t))