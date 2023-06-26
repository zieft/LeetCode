"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

"""


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
        dp[i]: 达到第i阶所需要的花费
        O(n)
        O(n)
        """
        dp = [0] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = 0

        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[len(cost)]


if __name__ == '__main__':
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    res = sol.minCostClimbingStairs(cost)
    print(res)
