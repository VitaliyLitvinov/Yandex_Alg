import sys
def solution(n: int, nums: list[int]) -> int:
    count = 0

    for i in range(n):
        prev_day: int = nums[i-1] if i > 0 else float('-inf')
        next_day: int = nums[i+1] if i < n-1 else float('-inf')
        if nums[i] > max(prev_day, next_day): count += 1
    return count
if __name__ == '__main__':
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(str(solution(n, nums)))