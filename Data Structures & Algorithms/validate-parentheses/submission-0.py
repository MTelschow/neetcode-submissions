class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_braces = ['()', '[]', '{}']
        open_braces = set(c[0] for c in valid_braces)
        brace_codes = {c: i for i, pair in enumerate(valid_braces) for c in pair}

        for c in s:
            if c in open_braces:
                stack.append(brace_codes[c])
                continue
            if len(stack) == 0 or stack[-1] != brace_codes[c]:
                return False
            stack.pop()


        return len(stack) == 0

        