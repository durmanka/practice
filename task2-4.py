def validate_brackets(code: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())

    for char in code:
        if char in opening:
            stack.append(char)
        elif char in pairs:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0