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
        基础动规
        O(n)
        O(n)
        """
        if n == 0:
            return 0
        dp = [1] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        if n > 2:
            for i in range(2, n+1):
                dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    sol = Solution()
    res = sol.fib(6)
    print(res)
