from typing import List

class Solution(object):
    """
    使用栈记录整数值，使用变量记录待计算的符号
    time: O(n)
    space: O(n)
    """
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        op = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num *= 10
                num += int(s[i])
            if i == n - 1 or s[i] in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                op = s[i]
                num = 0
        return sum(stack)
