import sys
def palindrome():
    word = sys.stdin.readline()
    l = 0
    r = len(word) - 1
    while l < r:
        while not word[l].isalpha() and l < r:
            l += 1
        while not word[r].isalpha() and l < r:
            r -= 1
        if l < r and word[l].lower() != word[r].lower(): return False
        l += 1
        r -= 1
    return True
print(palindrome())

