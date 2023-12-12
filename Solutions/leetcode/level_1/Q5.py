"""Valid Parentheses"""
"""Link to the problem: https://leetcode.com/problems/valid-parentheses/"""


class Solution:
    def isValid(self, s: str) -> bool:
        open_list = ["[", "{", "("]
        close_list = ["]", "}", ")"]
        stack = []
        for i in s:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if stack and open_list[pos] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    Input = {"s": "()[]{}"}
    print(f"Input:{Input}")
    Output = solution.isValid(Input["s"])
    print(f"Output:{Output}")
