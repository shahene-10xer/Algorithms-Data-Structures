class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # 1st phase -> get string
                substr = ''
                while stack and stack[-1] != '[':
                    ch = stack.pop()
                    substr = ch + substr
                stack.pop() # pop actual opening bracket
                # 2nd phase -> get k 
                k = ''
                while stack and stack[-1].isnumeric():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
                    
        return ''.join(stack)