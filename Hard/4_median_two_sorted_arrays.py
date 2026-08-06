class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged =nums1+nums2
        merged.sort()

        length=len(merged)
        middle =length//2

        if length %2==1:
            return float(merged[middle])
        else:
            return (merged[middle-1]+merged[middle])/2

        
