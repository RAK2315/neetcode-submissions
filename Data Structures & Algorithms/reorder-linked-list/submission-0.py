# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        left = 0
        right = len(nodes) - 1

        # eg [1,2,3 ,4,5,6]

        #in round 1
        temp = ListNode()
        while left < right:
            nodes[left].next = nodes[right] # 1->6
            left += 1 # left = 0+1 = 1
            nodes[right].next = nodes[left] # 6-> nodes[1] ie 2
            right-=1 # right = 5-1=4


        nodes[left].next = None # so that final node poitns at none

        # return nothign cuase we actualy update the actual nodes
        
        