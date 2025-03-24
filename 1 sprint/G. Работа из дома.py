def to_base(n:int, base: int) -> int:
    result = []
    while n > 0:
        remainder = n%base
        result.append(str(remainder))
        n = n//base
    return int(''.join(result[::-1]))
def solution():
    n: int = int(input())
    base: int = int(input())
    return to_base(n, base)
if __name__ == '__main__':
    print(solution())