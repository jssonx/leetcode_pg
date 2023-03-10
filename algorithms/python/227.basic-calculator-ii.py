#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = collections.deque(s)
        stack = []
        sign = '+'
        num = 0
        while len(s) > 0:
            c = s.popleft()
            if c.isdigit():
                num = 10 * num + int(c)
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1] / float(num))       
                num = 0
                sign = c

        return sum(stack)



        
# @lc code=end

