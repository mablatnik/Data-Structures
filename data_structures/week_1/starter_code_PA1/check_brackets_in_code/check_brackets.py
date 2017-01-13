# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False


def bracket_check(text):
    opening_brackets_stack = []
    for index, next in enumerate(text, start=1):
        if next in ("[", "(", "{"):
            opening_brackets_stack.append(Bracket(next, index))

        elif next in ("]", ")", "}"):
            if not opening_brackets_stack:
                return index

            top = opening_brackets_stack.pop()
            if not top.match(next):
                return index
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        return top.position

    return "Success"


if __name__ == "__main__":
    text = sys.stdin.read().strip("\n")
    print(bracket_check(text))
