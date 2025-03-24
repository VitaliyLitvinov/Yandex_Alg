import sys
a, x, b, c = map(int, sys.stdin.readline().rstrip().split())
sys.stdout.write(str((a*x**2) + (b*x) + c))