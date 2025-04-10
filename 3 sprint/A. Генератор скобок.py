import sys
def generator(n: int, prefix: str) -> str:
    if n == 0:
        if validate(prefix):
            sys.stdout.write(prefix + '\n')
    else:
        generator(n-1, prefix + "(")
        generator(n-1, prefix + ")")
def validate(sequence: str) -> bool:
    cnt = 0
    for i in sequence:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True if cnt == 0 else False

if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip())
    generator(n, '')

