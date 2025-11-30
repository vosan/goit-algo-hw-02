from collections import deque


def is_palindrome(word: str) -> bool:
    dq = deque()
    for char in word:
        dq.append(char)

    for i in range(len(word) // 2):
        if dq.pop() != dq.popleft():
            return False

    return True


print(f"{is_palindrome("racecar")=}")
print(f"{is_palindrome(f"hello")=}")
print(f"{is_palindrome(f"madam")=}")
print(f"{is_palindrome(f"step on no pets")=}")
print(f"{is_palindrome(f"python")=}")
