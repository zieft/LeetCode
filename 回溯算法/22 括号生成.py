"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
1 <= n <= 8
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def dfs(string, left, right):
            """
            回溯+剪枝
            时间复杂度: O(2^(2n))
            空间复杂度: O(2n)=O(n)
            """
            if left > right:  # 右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支
                return  # 否则剪枝

            if left == 0 and right == 0:  # 在左边和右边剩余的括号数都等于 0 的时候结算。
                res.append(string)

            # 当前左右括号都有大于 0 个可以使用的时候，才产生分支
            # 下面两个if 顺序无所谓
            if right > 0:
                dfs(string + ")", left, right - 1, )

            if left > 0:
                dfs(string + '(', left - 1, right)

        res = []
        left = n
        right = n
        dfs('', left, right)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.generateParenthesis(3)
    print(res)
