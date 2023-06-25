"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
"""


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
        回溯+深度优先搜索
        时间复杂度为 O(RC3^L)
        空间复杂度为 O(L)
        其中 R 和 C 分别为网格的行数和列数，L 为单词的长度。
        """

        def dfs(board, r, c, index):
            if not 0 <= r < len(board) or not 0 <= c < len(board[0]):
                return  # 出界直接跳过
            if ([r, c] in stack):
                return  # 标记为已使用的跳过
            stack.append([r, c])  # 标记当前节点为已使用
            if board[r][c] == word[index]:
                index += 1  # 如果和单词中对应的字母匹配，则接着找下一个字母
            else:
                stack.pop()  # 否则当前节点出栈，标记为未使用。
                return False

            if index == len(word):  # 退出条件
                return True  # 如果dfs的深度和word的长度相同，说明找到对应的单词

            if dfs(board, r + 1, c, index) or \
                    dfs(board, r - 1, c, index) or \
                    dfs(board, r, c + 1, index) or \
                    dfs(board, r, c - 1, index):
                return True  # 说明在任意方向上找到了对应的字母，并把True返回给上一层
            stack.pop()  # 如果一个节点的四个方向上都没找到正确的字母，说明这条路走不通了，把当前这条路上的”已使用“回溯成”未使用“

        for r in range(len(board)):  # for循环用来遍历不同的起点
            for c in range(len(board[0])):
                index = 0  # index用于记录dfs的深度
                if board[r][c][0] == word[index]:
                    stack = []  # 维护一个栈，用来记录已使用的节点
                    if dfs(board, r, c, index) == True:  # dfs用来从不同的起点深入进去走路
                        return True

        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    sol = Solution()
    res = sol.exist(board, word)
    board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word2 = "ABCCED"
    res2 = sol.exist(board2, word2)
    board3 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word3 = "ABCESEEEFS"
    res3 = sol.exist(board3, word3)
    print(res)
    print(res2)
    print(res3)
