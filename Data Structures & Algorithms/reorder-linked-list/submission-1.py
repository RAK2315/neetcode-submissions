# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        """
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
        """

        slow = head
        fast = head.next

        # 1,2,3,4,5,6
        #     s     f

        # by this, slow wil stop at mid and fast at last node
        # so first half will be start to slow
        # and 2nd half from slow.next to fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # second half, well be reversing it
        second = slow.next
        
        slow.next = None
        
        reverse = None
        # 4 5 6
        while second:
            nextNode = second.next
            second.next = reverse
            reverse = second
            second = nextNode

        first = head
        second = reverse
        # in odd num like  [1,2,3, 5,6]
        # first half wil be more numbers always or eqyal halfs in even, sp


        # in [1,2,3, 4,5], first pass 
        while second:
            temp1 = first.next  #temp1 = 2
            temp2 = second.next #temp2 = 4

            first.next = second # 1->5
            
            second.next = temp1  # 5->2, so 1->5->2

            first = temp1
            second = temp2


    

        