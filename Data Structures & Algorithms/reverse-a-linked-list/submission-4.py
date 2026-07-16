# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        # consider every elemtn in the array as a node itself
        # unlike c there is no actual pointer that can be used for tracking, every elemnt has 
        #       a value

        if not head: return None


        current = head

        previos = None


        while current: # while current != None

            # storing nextnode for later use
            next_node = current.next

            # updating current node to store prev value so the LL will be reverse
            current.next = previos 

            # updating prev to current node so that next loop has next value in list for prev
            previos = current

            # updation
            current = next_node
        
        # at the end of loop, prev will point to last node in array and in backward sequence
        return previos


