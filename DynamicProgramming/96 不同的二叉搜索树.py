"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。

输入：n = 3
输出：5
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        dp[i]: 含有i个节点的BST数目为dp[i]
        dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[1]
        dp[4] = dp[0] * dp[3] + dp[1] * dp[2] + dp[2] * dp[1] * dp[3] * dp[0]
        ...
        dp[i] += dp[j] * dp[(i - 1) - j]
        O(n^2)
        O(n)
        """
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0] = 1  # 空树也算BST
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):  # 求所有子问题
            for j in range(0, i):  # 计算当前子问题的递推式
                dp[i] += dp[j] * dp[(i - 1) - j]

        return dp[n]



if __name__ == '__main__':
    sol = Solution()
    res = sol.numTrees(4)
    print(res)
