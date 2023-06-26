"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        和斐波那契数是一样的
        O(n)
        O(1)
        """
        if n < 2:
            return n

        dp0, dp1, dp2 = 0, 1, 2

        for i in range(2, n):
            dp0, dp1 = dp1, dp2
            dp2 = dp1 + dp0

        return dp2


if __name__ == '__main__':
    sol=Solution()
    res = sol.climbStairs(5)
    print(res)
