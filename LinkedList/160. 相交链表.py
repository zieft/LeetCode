from LinkedList import BaseSolution, ListNode


class Solution(BaseSolution):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        时间复杂度为 O(m + n)
        空间复杂度为 O(1)
        其中，m 和 n 分别是两个链表的长度。
        """
        pA, pB = headA, headB
        # 循环停止条件：当两个指针指向同一个节点或者都为空时，返回它们指向的节点或者None
        while pA != pB:
            # 同步指针
            # 如果指针pA不为空，则将指针pA移到下一个节点
            # 如果指针pA为空，则将指针pA移到链表headB的头节点
            # 这样，当两个指针都经过一次替换链表后，他们的位置就同步了
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA

        return pA


if __name__ == '__main__':
    sol = Solution()
    common = sol.create_linklist_tail([8, 4, 5])
    listA = sol.create_linklist_tail([4, 1])
    listB = sol.create_linklist_tail([5, 6, 1])

    sol.merge_linklist_in_tail(listA, common)
    sol.merge_linklist_in_tail(listB, common)

    node = sol.getIntersectionNode(listA, listB)
    print(node)
