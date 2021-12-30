# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        '''
        1 --> 2 --> 4 --> None
        None <-- 1 <-- 2 <-- 4
        '''

        prev = None
        curr = head

        while curr != None:
            temp = curr.next  # 暂存当前节点的下一个节点
            curr.next = prev  # 将当前节点链接前一个节点
            prev = curr  # 前一个节点成为当前节点
            curr = temp  # 当前节点变为下一个节点，进入下次迭代

        # 最后的curr为None，没有链接前一个节点，因此返回prev
        return prev

    def reverseList2(self, head: ListNode) -> ListNode:
        '''
        递↓                         归↑
        1 --> 2 --> 4 --> None      head = 节点1, 2 --> 1, 1 --> None, 返回
        |
       head                         ↑
                                                           |  节点4  |位置|
              2 --> 4 --> None      p = 节点4, head = 节点2, head.next.next = head, 4 --> 2, 此时2 <--> 4, head.next = None, 2 --> None, 返回
              |
             head                   ↑

                    4 --> None      head.next == None 返回节点4
                    |
                   head

        None <-- 1 <-- 2 <-- 4

        '''
        if head == None or head.next == None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p


if __name__ == "__main__":
    pass
