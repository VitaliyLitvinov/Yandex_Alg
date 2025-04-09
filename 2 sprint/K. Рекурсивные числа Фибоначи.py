import sys
def number_commit(i) -> int:
    if i < 2: return 1
    return i + number_commit(i-1)

if __name__ == "__main__":
    i = int(sys.stdin.readline())
    sys.stdout.write(str(number_commit(i)))

