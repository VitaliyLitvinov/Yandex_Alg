import sys
def Find_neighbour(n:int, m:int, matrix: list[list[int]], row: int, col: int):
    lst = []
    if col-1 >= 0: lst.append(matrix[row][col-1])
    if col+1 <= m: lst.append(matrix[row][col+1])
    if row-1 >= 0: lst.append(matrix[row-1][col])
    if row+1 <= n: lst.append(matrix[row+1][col])
    return sorted(lst)
if __name__ == '__main__':
    n, m = int(input()), int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    row = int(input())
    col = int(input())
    neighbours = Find_neighbour(n, m, matrix, row, col)
#    sys.stdout.write(' '.join(map(str, Find_neighbour(n, m, matrix, row, col))))
    sys.stdout.write(' '.join(str(num) for num in Find_neighbour(n, m, matrix, row, col)))
