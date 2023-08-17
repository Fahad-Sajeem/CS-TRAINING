o = ['(', '[', '{']
c = [')', ']', '}']


def check(s):
    stack = []
    for i in s:
        if i in o:
            stack.append(i)
        elif i in c:
            pos = c.index(i)
            if (len(stack) > 0) and (o[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


string = input("Enter the string: ")
print(check(string))
