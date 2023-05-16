class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class BaseSolution:
    def create_linklist_tail(self, li):
        """尾插法将列表转换成链表的头节点"""
        head = ListNode(li[0])
        tail = head
        for element in li[1:]:
            node = ListNode(element)
            tail.next = node
            tail = node
        return head

    def print_LinkedList(self, res: ListNode):
        """print a LinkedList node by node from beginning to the end"""
        output = []
        output.append(res.val)
        while res.next:
            res = res.next
            output.append(res.val)
        print(output)
