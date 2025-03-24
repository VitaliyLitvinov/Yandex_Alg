import sys
a, b, c = map(int, sys.stdin.readline().split())
result = 'FAIL'
if (a%2 == 0 and b%2 == 0 and c%2 == 0 or
a%2 != 0 and b%2 != 0 and c%2 != 0): result = 'WIN'
sys.stdout.write(result)