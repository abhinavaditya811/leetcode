class Solution:
    def isValid(self, s: str) -> bool:
        pair_idx = {')': '(', ']': '[', '}': '{'}
        i = 0
        stack = []
        for i in s:
            if i in pair_idx.values():
                stack.append(i)
            elif i in pair_idx:
                if not stack or pair_idx[i] != stack.pop():
                    return False

        return not stack
    
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((((((()))))))", True),
        ("(((((())", False),
    ]
    
    for s, expected in test_cases:
        result = sol.isValid(s)
        print(f"isValid({s!r}) = {result}, expected = {expected}, {'PASS' if result == expected else 'FAIL'}")