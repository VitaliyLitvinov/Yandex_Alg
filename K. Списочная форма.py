import sys
def solution():
    x: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    k: list[int] = list(map(int, sys.stdin.readline().rstrip()))
    p2: int = -1
    if len(x) < len(k):
        x, k = k, x
    result: list[str] = []
    var = 0
    for p1 in range(len(x)-1,-1,-1):
        sum_num = 0
        if abs(p2) <= len(k):
            sum_num = x[p1 - len(x)] + k[p2] + var
            if sum_num >= 10: var = 1; result.append(str(sum_num%10))
            else: result.append(str(sum_num)); var = 0
        else:
            sum_num = x[p1] + var
            if sum_num >= 10: var = 1; result.append(str(sum_num%10))
            else: result.append(str(sum_num)); var = 0
        p2 -=  1
    if var == 1: result.append(str(1))
#     sys.stdin.write(''.join(result[::-1]))
    print(''.join(result[::-1]))

if __name__=="__main__":
    solution()