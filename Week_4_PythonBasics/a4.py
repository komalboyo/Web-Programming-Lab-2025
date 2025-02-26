class ParenthesesValidator:
    def __init__(self, string):
        self.string = string

    def is_valid(self):
        stack = []
        matching_parentheses = {')': '(', '}': '{', ']': '['}
        
        for char in self.string:
            if char in matching_parentheses.values():
                stack.append(char)
            elif char in matching_parentheses.keys():
                if stack and stack[-1] == matching_parentheses[char]:
                    stack.pop()
                else:
                    return False
        return not stack

validator = ParenthesesValidator("()[]{}")
print("Valid Parentheses:", validator.is_valid())
