import sys
def longest_word():
    n = int(sys.stdin.readline())
    string = sys.stdin.readline()
    max_r: int = 0
    max_l: int = 0
    l = 0
    for r in range(n):
        if string[r] == ' ':
            if r - l > max_r - max_l:
                max_r = r
                max_l = l
            l = r+1
    if n - l > max_r - max_l:
        max_r = n
        max_l = l
    print(string[max_l:max_r])
    print(max_r-max_l)
if __name__ == '__main__':
    longest_word()


