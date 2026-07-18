# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hashset = {}

        curr = head
        while curr:
            if curr in hashset:
                return True

            elif curr not in hashset:
                hashset[curr] = 0
            hashset[curr] += 1

            curr = curr.next
        return False


            