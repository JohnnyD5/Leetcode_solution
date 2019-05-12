# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#o(n)
# Form a cyclic list
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return []
        cur = end = head
        size = 1
        while cur.next:
            size += 1
            cur = cur.next
        cur.next = head
        k %= size
        for i in range(size-k-1):
            end = end.next
        res = end.next
        end.next = None
        return res

# o(n^2)
# Take out last num every time go through the list
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return []
        if head.next == None or k==0:
            return head
        res = dummy = ListNode(-1)
        cur = head
        size = 0
        while cur:
            size += 1
            cur = cur.next
        # numbers of loop: nl
        nl = k%size
        if nl == 0:
            return head
        while nl > 0:
            cur = head
            while cur.next:
                if cur.next.next == None:
                    num = cur.next.val
                    cur.next = cur.next.next
                else:
                    cur = cur.next
            res.next = ListNode(num)
            res.next.next = head
            head = res.next
            nl -= 1
        return dummy.next
            
