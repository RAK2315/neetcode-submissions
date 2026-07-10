class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # [1,2,3,4 ,5,6,7]
        #[1,2,3,4]
        # [5,6,7]

        joined_len = len(nums1) + len(nums2)

        med1 = 0
        med2 = 0
        l1,l2 = 0,0
        for _ in range((joined_len//2)+1):
            med2 = med1
            if l1<len(nums1) and l2 < len(nums2):
                if nums1[l1] >= nums2[l2]:
                    med1 = nums2[l2]
                    l2 += 1
                else:
                    med1 = nums1[l1]
                    l1 += 1
            
            elif l1 < len(nums1):
                med1 = nums1[l1]
                l1+=1
            
            else: # l2 < len(nums2)
                med1 = nums2[l2]
                l2+=1
        
        if joined_len % 2 == 0: return (med1+med2)/2.0
        else: return float(med1)
        
