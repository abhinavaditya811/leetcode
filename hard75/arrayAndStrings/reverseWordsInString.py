def reverseWords(self, s: str) -> str:
  i = 0
  words = s.split()
  j = len(words) - 1
  if not words:
      return ""

  while i < j:
      words[i], words[j] = words[j], words[i]

      i += 1
      j -= 1
  
  new_s = " ".join(words)
  return new_s

if __name__ == "__main__":
    print(reverseWords(None, "Hello World")) # Output: "World Hello"
    print(reverseWords(None, "  Hello   World  ")) # Output: "World Hello"
    print(reverseWords(None, "a good   example")) # Output: "example good a"
