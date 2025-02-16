import sys
def solution():
    n: int = int(sys.stdin.readline())
    flag = True
    while n != 1:
        if n % 4 == 0: n /= 4
        else:
            flag = False
            break
    sys.stdout.write(str(flag))
if __name__ == '__main__':
    solution()