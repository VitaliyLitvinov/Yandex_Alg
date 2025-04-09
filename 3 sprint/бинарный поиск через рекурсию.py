import sys
def Binary_search(arr: list, x: int, left:int, right: int):
    mid: int = (left + right) // 2
    if arr[mid] == x:
        return mid
    if right <= left:
        return -1
    if arr[mid] > x:
        return Binary_search(arr, x, left, mid)
    else:
        return Binary_search(arr, x, mid + 1, right)

if __name__ == "__main__":
    arr = [1,3,4,5,6,7,8,9]
    x = int(sys.stdin.readline().rstrip())
    sys.stdout.write(str(Binary_search(arr, x, 0, len(arr))))