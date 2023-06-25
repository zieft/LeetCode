"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        combination = []

        def dfs(board, r, c, index):
            if not 0 <= r < len(board) or not 0 <= c < len(board[0]) or ([r, c] in mask):
                return
            if board[r][c][0] == word[index]:
                combination.append(board[r][c][0])
                mask.append([r, c])
                index += 1
            if index == len(word):
                self.res = "".join(combination)

            dfs(board, r + 1, c, index)
            dfs(board, r - 1, c, index)
            dfs(board, r, c + 1, index)
            dfs(board, r, c - 1, index)

        for r in range(len(board)):
            for c in range(len(board[0])):
                index = 0
                if board[r][c][0] == word[index]:
                    mask = []
                    dfs(board, r, c, index)

        return self.res == word


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    sol = Solution()
    res = sol.exist(board, word)
    print(res)
