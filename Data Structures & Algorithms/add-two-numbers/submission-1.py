# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 321 + 756
        # 1 2 3
        # 6 4 7
        

        res = ListNode()
        carry = 0
        curr = res

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            summ = val1 + val2 + carry

            carry = summ //10

            digit = ListNode(summ % 10)
            curr.next = digit
            curr = curr.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return res.next

            







            