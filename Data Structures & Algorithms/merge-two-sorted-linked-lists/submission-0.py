# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        final = head = ListNode()

        # final - is the one storing the start of LL
        # head will be the temp pointer that we use for moving and addding stuff

        # [1,2,3]
        # [1,5,6]
        # f = h (only at start)
        #  0 -> 1
        #       h

        while list1 and list2:
            if list1.val <= list2.val:
                
                # lets say head is at 0 at start
                head.next = list1 # next to 0 connect 1, so 0 -> 1
                head = head.next  # update head to be now point on 1
                list1 = list1.next
            else:
                head.next = list2
                head = head.next
                list2 = list2.next

        # at end of loop, one or both of LLs are at the end
        # so we simply connect this with final
        # (remeber given arrs are sorted so the connected part will be sorted anyway)
        if list1: head.next = list1
        if list2: head.next = list2

        return final.next # not jsut final since we have 0 stored as a dummy so it returns 
                          #         that too if not done .next





