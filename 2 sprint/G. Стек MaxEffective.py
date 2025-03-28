#import sys
class StackMax:
    def __init__(self):
        self.stack: list[int] = []
        self.mx_stack: list = []

    def push(self, item) -> None:
        self.stack.append(int(item))
        if int(item) >= self.stack[-1]:
            self.mx_stack.append(int(item))

    def pop(self) -> None:
        value = self.stack.pop()
        if value == self.mx_stack[-1] and self.mx_stack:
            self.mx_stack.pop()

    def get_max(self) -> int|None:
        if self.stack:
            return self.mx_stack[-1]
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

# 10
# pop
# pop
# push 4
# push -5
# push 7
# pop
# pop
# get_max
# pop
# get_max

# 6
# push 2
# push -2
# get_max
# pop
# get_max
# pop






