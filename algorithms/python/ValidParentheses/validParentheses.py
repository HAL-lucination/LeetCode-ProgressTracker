# Basic of stack.

s = "[([]])"

def is_valid(str):
    stack = []
    mapping = {')':'(', ']':'[', "}":"{"}

    for i in range(len(str)):
        print(stack)
        if str[i] in mapping:
            top = stack.pop() if stack else '0'
            if mapping[str[i]] != top:
                return False
        else:
            stack.append(str[i])

    if not stack:
        return True

print(is_valid(s))
