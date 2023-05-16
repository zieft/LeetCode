from LinkedList import BaseSolution, ListNode

"""
19.Given the head of a linked list, remove the nth node from the end of the list and return its head.

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

class Solution(BaseSolution):
    def removeNthFromEnd(self, head, n: int) -> ListNode:
        """
        快慢双指针
        时间复杂度：O(L)，其中 L 是链表的长度。
        空间复杂度：O(1)。
        """
        # 创建虚拟头节点
        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, dummy
        print(slow == fast and fast == dummy)  # True: slow, fast和dummy都在操作同一块内存
        # fast 先走n+1步
        for _ in range(n + 1):
            fast = fast.next
        # slow和fast同时右移，直到fast为None（链表尾部）
        while fast:
            slow, fast = slow.next, fast.next
        # slow所指的元素下一个元素即为待删除元素
        slow.next = slow.next.next
        # 由于并没有真正地删除元素
        # 所以最后不能直接return head，以防要删除的节点为head
        return dummy.next

if __name__ == '__main__':
    sol = Solution()
    head = sol.create_linklist_tail([1, 2, 3, 4, 5])

    res = sol.removeNthFromEnd(head, n=2)
    sol.print_LinkedList(res)
    