# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        hashset = {}

        # we can use hash map or hashset to keep seen "nodes" since nodes ara type of opjects 
        # like str, int float tuple etc, nodes can also be stored as keys as each node
        # is always is unique

        curr = head
        while curr:
            if curr in hashset:
                return True

            elif curr not in hashset:
                hashset[curr] = True

            curr = curr.next
        return False


            