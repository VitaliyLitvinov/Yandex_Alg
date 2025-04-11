import sys
def combination(numbers: str) -> str:
    letters = {2:'abc', 3:'def', 4:'ghi', 5:'jki', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    if len(numbers) <= 1:
        return letters[int(numbers[0])]
#    return letters[int(numbers[0])] + combination(numbers[1:], n)
    for i in letters[int(numbers[0])]:
        return i + combination(numbers[1:])


if __name__ == "__main__":
    nums = sys.stdin.readline().rstrip()
    print(combination(nums))