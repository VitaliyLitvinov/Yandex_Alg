
def check(string):
    if string:
        left = ''
        for i in range(len(string)):
            if string[i] in '([{':
                if string[i] == '(': left += ')'
                elif string[i] == '[': left += ']'
                elif string[i] == '{': left += '}'
            elif len(left) > 0 and left == string[i+len(left)-1:i-1:-1]:
                left = ''
                continue
            elif len(left) > 0 and left != string[i+len(left)-1:i-1:-1]:
                print(left + string[i+len(left)-1:i-1:-1])
                return False
        return True

    else:
        return True

if __name__=="__main__":
    print(check(input()))

#    {[()]}(()){{(([]))}}