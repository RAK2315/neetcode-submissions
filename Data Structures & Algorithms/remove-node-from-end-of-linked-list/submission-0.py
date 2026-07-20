# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        # [1,2,3,4,5,6,7]

        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
                
        target = count - n + 1

        # if deleting first node, ex: [5], n=1
        if target == 1:
            return head.next


        curr = head
        prev = None
        
        # 1,2,3, 4 ,5,6
        for i in range(1,count+1):
            if i==target:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        
        return head
