'''
// Source : https://oj.leetcode.com/problems/median-of-two-sorted-arrays/
// Author : Hal
// Date   : 2019-12-09

/**********************************************************************************
*
* There are two sorted arrays A and B of size m and n respectively.
* Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
*
**********************************************************************************/
'''
'''
Brute force solution
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        import numpy as np
        return np.median(np.asarray(nums1 + nums2))
