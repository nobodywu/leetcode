# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        '''
        递归
        '''
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 新建一个链表
        a = ListNode(0)
        b = a

        while l1 != None and l2 != None:
            if l1.val < l2.val:
                a.next = l1
                l1 = l1.next
            else:
                a.next = l2
                l2 = l2.next
            
            a = a.next
        
        a.next = l1 if l1 != None else l2

        return b.next

if __name__ == "__main__":
    # 两个链表是有序的
    # 2 -> 3 -> 4
    nodelist1 = ListNode(2)
    nodelist1.next = ListNode(3)
    nodelist1.next.next = ListNode(4)

    # 1 -> 6 -> 7
    nodelist2 = ListNode(1)
    nodelist2.next = ListNode(6)
    nodelist2.next.next = ListNode(7)

    s = Solution()
    a = s.mergeTwoLists2(nodelist1, nodelist2)
    
    if None != a:
        print(a.val)
        while None != a.next:
            a = a.next
            print(a.val)