# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        '''
        如果两个链表长度不同，pA将先遍历A链表后遍历B链表到达None，pB将遍历B链表后遍历A链表到达None，消除了长度差

        如果两个链表长度相同且有交点，在3处，pA != pB，将在6处返回
        1 - 2 - 3 - 4
                     \
                       6 - 7 - 9
                     /
        2 - 1 - 3 - 5

        如果两个链表没有交点
        a. 如果长度相同，pA将遍历A链表到达None，pB将遍历B链表到达None，然后返回
        b. 如果长度不同，pA将先遍历A链表后遍历B链表到达None，pB将遍历B链表后遍历A链表到达None，然后返回
        '''
        if headA == None or headB == None:
            return None

        pA, pB = headA, headB
        while pA != pB:
            pA = pA.next if pA != None else headB
            pB = pB.next if pB != None else headA

        return pA


if __name__ == "__main__":
    pass
