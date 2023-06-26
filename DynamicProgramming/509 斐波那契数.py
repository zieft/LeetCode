"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。

输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
"""


class Solution:
    def fib(self, n: int) -> int:
        """
        动规 滚动数组
        O(n)
        O(1)
        """
        if n < 2:
            return n

        dp_n_2, dp_n_1, dp_n = 0, 0, 1
        for i in range(2, n + 1):
            dp_n_2, dp_n_1 = dp_n_1, dp_n
            dp_n = dp_n_2 + dp_n_1

        return dp_n


if __name__ == '__main__':
    sol = Solution()
    res = sol.fib(6)
    print(res)
