"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""


class Solution:
    def numIslands_dfs(self, grid: list[list[str]]) -> int:
        """
        深度优先搜索实现
        时间复杂度为O(RC)
        空间复杂度为O(RC)
        """
        def dfs(grid, r, c):
            # if r > len(grid[:]) or c > len(grid[0]) or grid[r][c] == "0" or grid[r][c] == "2": # 这样写造成IndexError
            if not 0 <= r <= len(grid) or not 0 <= c <= len(grid[0]) or grid[r][c] == "0" or grid[r][c] == "2":
                return

            grid[r][c] = "2"

            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
            return

        island = 0
        for r in range(len(grid[:])):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    island += 1

        return island


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    sol = Solution()
    print(sol.numIslands_dfs(grid))
