import sys

def check_validation(sequence):
    stack:list = []
    reverse_brace: dict = {')': '(', ']': '[', '}': '{'}
    for i in sequence:
        if i in '({[':
            stack.append(i)
        elif not stack or stack[-1] != reverse_brace[i]:
            return 'False'
        else: stack.pop()
    return 'True' if len(stack) == 0 else 'False'
if __name__=="__main__":
    sequence: str = sys.stdin.readline().rstrip()
    sys.stdout.write(check_validation(sequence))

# def check(string):
#     if string:
#         left = ''
#         for i in range(len(string)):
#             if string[i] in '([{':
#                 if string[i] == '(': left += ')'
#                 elif string[i] == '[': left += ']'
#                 elif string[i] == '{': left += '}'
#             elif len(left) > 0 and left == string[i+len(left)-1:i-1:-1]:
#                 left = ''
#                 continue
#             elif len(left) > 0 and left != string[i+len(left)-1:i-1:-1]:
#                 return False
#         return True
#
#     else:
#         return True
#
# if __name__=="__main__":
#     print(check(input()))

#    {[()]}(()){{(([]))}}

