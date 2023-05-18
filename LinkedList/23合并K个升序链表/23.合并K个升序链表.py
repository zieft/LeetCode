from LinkedList import BaseSolution, ListNode

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
"""


class Solution(BaseSolution):
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        """
        这段代码的时间复杂度取决于链表的总长度和链表的数量。假设链表的总长度为 N，链表的数量为 K。

        在 for 循环中，将各个链表的头节点依次压入堆中，时间复杂度为 O(K logK)。每次压入堆的时间复杂度为 O(logK)，需要进行 K 次操作。

        在 while 循环中，每次从堆中取出最小值，并将其插入结果链表，然后将该链表的下一个节点压入堆中。
        由于每个节点最多只会被插入堆一次，所以循环的迭代次数最多为 N。
        每次从堆中取出最小值的时间复杂度为 O(logK)，插入堆的时间复杂度也为 O(logK)。
        因此，循环的总时间复杂度为 O(N logK)。

        综上所述，该段代码的时间复杂度为 O(N logK)，其中 N 是链表的总长度，K 是链表的数量。

        空间复杂度方面，除了输入的链表和输出的链表之外，额外使用了一个堆来存储节点。堆的大小最多为 K，所以堆的空间复杂度为 O(K)。
        除此之外，还使用了常数级别的额外空间。
        因此，整体的空间复杂度为 O(K)。
        """

        # 优先级队列
        # https://docs.python.org/zh-cn/3/library/heapq.html#module-heapq
        import heapq
        dummy = ListNode(0)  # 新建链表的虚拟头节点
        p = dummy  # p是个指针，指向新建链表的当前位置
        head = []  # 维护一个heap列表，存储各个链表的当前节点
        for i in range(len(lists)):
            if lists[i]:  # lists[i]是个指针，指向各个链表中当前的节点
                # 把所有链表的头节点依次压入队列，并记录该头节点来自于哪条链表
                # i标识第i个链表
                heapq.heappush(head, (lists[i].val, i))  # 压入队列（头节点的值，第i条链表）
                """
                这里之所以不能像c++一样，不需要传入元组，是因为lists[i]是链表节点对象，而c++中的list是节点对象的指针。
                c++指针天然带有哪条链表的信息，并且使用指针入堆的时候，可以直接根据指针指向的数据进行大小比较，同时可以调用next成员
                而ListNode对象没有大小比较的实现，也没有哪条链表的位置信息（内存位置）。如果直接压入lists[i].val，
                这样虽然可以比较大小，但又失去了对.next成员变量的访问。
                所以，python需要往堆里压入包含链表位置信息和值的元组。
                
                同时要注意的是，python元组比较大小的规则。
                在元组的比较中，会逐个比较元组中对应位置的元素，直到找到一个不同的元素为止。
                也就是说，如果两个元组的第一个元素相等，那么会继续比较第二个元素，以此类推。
                只有在遇到不同的元素时，才能确定两个元组的大小关系。
                """
                lists[i] = lists[i].next  # for循环结束后，lists[i]指向各个链表的第二个节点

        while head:
            # heapq是小根堆，其根节点一定是堆中的最小值
            val, idx = heapq.heappop(head)  # 最小值出堆，idx表示当前值属于哪个链表
            p.next = ListNode(val)  # 链入新链表
            p = p.next  # 移动指针
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))  # 将当前链表的下一个值压入堆（lists[i]指针在for循环中被更新）
                lists[idx] = lists[idx].next  # 再次更新lists[i]指针

        return dummy.next


if __name__ == '__main__':
    sol = Solution()

    l1 = sol.create_linklist_tail([1, 4, 5])
    l2 = sol.create_linklist_tail([1, 3, 4])
    l3 = sol.create_linklist_tail([2, 6])

    lists = [l1, l2, l3]

    res = sol.mergeKLists(lists)
    sol.print_LinkedList(res)
