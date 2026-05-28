def validate_brackets(code):
    stack = []
    opening = "([{"
    closing = ")]}"
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in code:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if len(stack) == 0:
                return False
            if stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0

tests = [
    ("if (x > 0) { print([1, 2, 3]) }",    True),
    ("func(a[0], b{1})",                    True),
    ("(()())",                              True),
    ("if (x > 0) { print([1, 2, 3] }",     False),
    ("(((",                                 False),
    (")))",                                 False),
    ("([)]",                                False),
]

for code, expected in tests:
    result = validate_brackets(code)
    status = "✓" if result == expected else "✗"
    print(f"{status} '{code}'")
    print(f"   результат: {result}\n")