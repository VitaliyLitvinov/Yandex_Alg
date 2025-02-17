import sys
def solution():
    one: str = sys.stdin.readline()
    two: str = sys.stdin.readline()
    for i in two:
        if i in one: one = one.replace(i, '', 1)
        else: sys.stdout.write(i); break
if __name__=="__main__":
    solution()
