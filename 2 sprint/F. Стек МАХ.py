#import sys
class StackMax:
    def __init__(self):
        self.stack: list[int] = []

    def push(self, item) -> None:
        self.stack.append(int(item))
    def pop(self) -> None:
        self.stack.pop()
    def get_max(self) -> int|None:
        if self.stack:
            mx = -99999
            for i in self.stack:
                if i > mx:
                    mx = i
            return mx
        return None

def Solution() ->None:
    stack = StackMax()
    answer: list = []
    for i in range(int(input())):
        request: str = input()
        if request.startswith('push'):
            StackMax.push(stack, request.split()[-1])
        elif request.startswith('pop'):
            if stack.stack:
                StackMax.pop(stack)
            else: answer.append('error')
        elif request.startswith('get_max'):
            answer.append(StackMax.get_max(stack))
    print(*answer, sep='\n')

if __name__=='__main__':
    Solution()

# 8
# get_max
# push 7
# pop
# push -2
# push -1
# pop
# get_max
# get_max



