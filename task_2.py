from collections import deque


def is_palindrome(word: str) -> bool:
    """
    Check if a given word is a palindrome.

    :param word: The word to be checked for being a palindrome
    :return: True if the word is a palindrome, False otherwise
    """
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
