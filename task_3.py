class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None


def check_closures(text: str) -> bool:
    """
    Checks if all closures in the given text are properly matched and closed.

    :param text: The input string containing closures to be validated.
    :return: True if all closures are properly matched and closed, False otherwise.
    """
    closure_pairs = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    stack = Stack()
    for char in text:
        if char in closure_pairs:
            stack.push(char)
        elif char in closure_pairs.values():
            if stack.is_empty():
                # Immediately return False if encounter a closing bracket with no previous opening bracket
                return False

            last_opening_bracket = stack.pop()
            if closure_pairs[last_opening_bracket] != char:
                return False

    return stack.is_empty()


print(f"{check_closures("( ){[ 1 ]( 1 + 3 )( ){ }}")=}")
print(f"{check_closures("( 23 ( 2 - 3)")=}")
print(f"{check_closures("( 11 }")=}")
print(f"{check_closures("([)]")=}")
print(f"{check_closures("][")=}")
