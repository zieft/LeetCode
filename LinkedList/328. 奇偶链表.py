from LinkedList import ListNode, BaseSolution

"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even 
indices, and return the reordered list.
The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd groups should remain as it was in the input.
You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""


class Solution(BaseSolution):
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        双指针，注意循环条件的选择，以处理边界问题。
        时间复杂度为 O(n)
        空间复杂度为 O(1)
        """
        if not head:
            return head
        # 在原链表上加上两个指针，一个指向奇数节点，另一个指向偶数节点，可以将他们想象成两个新的链表的head。
        odd = head
        even = head.next
        # 再创建两个操作指针，指向两个“新”链表的头部
        odd_cur, even_cur = odd, even
        while even_cur and even_cur.next:
            odd_cur.next = odd_cur.next.next  # 奇节点绕过偶节点，连接下一个奇节点
            even_cur.next = even_cur.next.next  # 偶节点绕过奇节点，连接下一个偶节点

            odd_cur = odd_cur.next  # 指针移到下一个奇节点上
            even_cur = even_cur.next  # 指针移到下一个偶节点上
            # 循环结束后，原链表按奇偶位，分成两个链表，分别保存在odd和even中

        # 将odd和even拼接起来，即可
        odd_cur.next = even

        return odd


sol = Solution()
head = sol.create_linklist_tail([1, 2, 3, 4, 5, 6, 7])
res = sol.oddEvenList(head)
sol.print_LinkedList(res)
