import sys
def binary_search(arr: list[int], x: int, left:int, right: int) -> int:
    mid: int = (left + right) // 2
    if right <= left:
        return -1
    if arr[mid] == x:
        while arr[mid] == x:
            if arr[mid - 1] == x:
                mid -= 1
            else: return mid + 1
    if arr[mid] > x:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid + 1, right)

def two_bicycles(arr: list[int], price: int, days: int) -> None:
    sys.stdout.write(str(binary_search(arr, price, 0, days)) + " ")
    sys.stdout.write(str(binary_search(arr, price * 2, 0, days)))


if __name__ == "__main__":
    days = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    price = int(sys.stdin.readline())
    two_bicycles(arr, price, days)
# 6
# 1 3 3 4 5 5
# 3
