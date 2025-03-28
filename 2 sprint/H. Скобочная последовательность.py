def check(string):
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in string:
        if i == '(': cnt1 += 1
        elif i == ')': cnt1 -= 1
        elif i == '[': cnt1 += 1
        elif i == ']': cnt1 -= 1
        elif i == '{': cnt1 += 1
        elif i == '}': cnt1 -= 1

        if cnt1<0 or cnt2<0 or cnt3<0:
            return False
    return True

if __name__=="__main__":
    print(check(input()))