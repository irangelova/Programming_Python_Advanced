def palindrome(word, index = 0):
    mid_length_word = len(word) // 2
    if index == mid_length_word:
        return f"{word} is a palindrome"
    if word[index] != word[len(word) - 1 - index]:
        return f"{word} is not a palindrome"
    index += 1
    return palindrome(word, index)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
