from LinkedList import BaseSolution, ListNode

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.
"""


class Solution(BaseSolution):
    def detectCycle(self, head: ListNode) -> ListNode or None:
        if not head:
            return

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        if not fast or not fast.next:
            # 如果快指针或快指针的下一个节点为空，说明链表中无环
            return

        fast = head  # 将快指针重新指向链表头部
        while fast != slow:  # 同时移动慢指针和快指针，直到它们相遇，即为环的入口节点
            fast = fast.next
            slow = slow.next

        return fast


if __name__ == '__main__':
    sol = Solution()
    head = sol.create_linklist_with_circle([3,2,0,-4], 1)
    res = sol.detectCycle(head)
    print(res)
