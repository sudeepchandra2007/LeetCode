class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lis = []
        for i in range(0,len(nums1)) :
            for j in range(0,len(nums2)) :
                if nums1[i]== nums2[j] and lis.count(nums1[i])==0 :
                    lis.append(nums1[i])
        return lis