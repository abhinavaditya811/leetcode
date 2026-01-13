def reverseVowels(s: str) -> str:
    i = 0
    j = len(s) - 1
    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    char_list = list(s)
    while i < j:
        if char_list[i] in vowels:
            if char_list[j] in vowels:
                temp = char_list[i]
                char_list[i] = char_list[j]
                char_list[j] = temp

                j -= 1
                i += 1
            elif char_list[j] not in vowels:
                j -= 1
        elif char_list[i] not in vowels:
            i += 1
    
    print(char_list)
    new_s = "".join(char_list)
    return new_s

if __name__ == "__main__":
    s = "IceCreAm"
    print(reverseVowels(s))