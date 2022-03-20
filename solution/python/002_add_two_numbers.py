class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 给要返回的链表建个表头，这样通过 answer.next 即可拿到要返回的链表
        answer = ListNode(0)

        # print(id(answer))
        # body = copy.copy(answer)
        # print(id(body))
        # body = copy.deepcopy(answer)
        # print(id(body))
        # 这里的赋值为引用
        # 对于链表浅拷贝或深拷贝都会创建新的地址
        body = answer
        # print(id(body))

        # 进位默认为 0
        carry = 0
        # 将 l1 和 l2 循环二合一
        while l1 != None or l2 != None:
            if l1 != None:
                x = l1.val
                l1 = l1.next
            else:
                x = 0

            if l2 != None:
                y = l2.val
                l2 = l2.next
            else:
                y = 0

            # 结果要加上进位
            sum_val = x + y + carry
            # 更新下一位的进位
            carry = sum_val // 10
            # 将结果定义为 ListNode 并赋给我们的下一节点
            body.next = ListNode(sum_val % 10)
            # 更新 body 为下一节点以完成连接
            body = body.next

        # 考虑个最后一位的情况
        if carry > 0:
            body.next = ListNode(carry)

        return answer.next


if __name__ == "__main__":
    # 2 -> 4 -> 3
    nodelist1 = ListNode(2)
    nodelist1.next = ListNode(4)
    nodelist1.next.next = ListNode(3)

    # 5 -> 6 -> 4
    nodelist2 = ListNode(5)
    nodelist2.next = ListNode(6)
    nodelist2.next.next = ListNode(4)

    s = Solution()
    a = s.addTwoNumbers(nodelist1, nodelist2)

    if None != a:
        print(a.val)
        while None != a.next:
            a = a.next
            print(a.val)
