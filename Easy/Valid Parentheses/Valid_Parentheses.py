class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in '({[':
                stack.append(i)
            # i가 닫힌 괄호일 경우,
            else:
                 # 스택이 비어있거나 (if not stack) 혹은 닫힌 괄홈이에도 불구하고 스택의 맨 앞 괄호가 열린 괄호가 아니면 False
                if not stack or \
                    (i == ')' and stack[-1] != '(') or \
                    (i == '}' and stack[-1] != '{') or \
                    (i == ']' and stack[-1] != '['):
                    return False
                #짝이 맞으니 pop
                stack.pop()

        #스택 내  문자열 잔재 여부 확인
        return not stack

myObj = Solution()
result = myObj.isValid("()[]{")