import sys
def binary_system():
    a: list = list(sys.stdin.readline().rstrip())
    b: list = list(sys.stdin.readline().rstrip())
    result: list = []
    var: int = 0
    lenght: int = 0
    if len(a)  > len(b): lenght = len(a)
    else: lenght = len(b); b, a = a, b
    point: int = len(b) - 1
    for i in range(lenght-1, -1, -1):
        digit: int = int(a[i]) + var
        if point >= 0: digit += int(b[point]); point -= 1
        var = digit // 2
        result.append(digit % 2)
    if var == 1: result.append(1)
    print(''.join(map(str, result[::-1])))
if __name__ == '__main__':
    binary_system()
