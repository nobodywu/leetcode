from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        将一个链表不断地从中间拆分，最底层的merge是node与node之间的merge，往上变为两个有序链表的合并（第21题）
        '''
        def sort(head, tail):
            # 输入为空
            if not head:
                return head

            # 输入只有一个node，直接返回，无需排序
            if head.next == tail:
                # 如果到达末尾，则进行截断，下一个节点变为None
                head.next = None
                return head

            slow, fast = head, head
            # 如果fast没有到达末尾
            while fast != tail:
                slow = slow.next
                fast = fast.next

                if fast != tail:
                    fast = fast.next

            mid = slow
            return merge(sort(head, mid), sort(mid, tail))

        def merge(head1, head2):
            '''
            参考第21题
            '''
            dummy = ListNode(0)
            temp, temp1, temp2 = dummy, head1, head2

            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next

                temp = temp.next

            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2

            return dummy.next

        return sort(head, None)


if __name__ == "__main__":
    pass
