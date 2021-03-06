'''
// Source : https://leetcode.com/problems/intersection-of-two-arrays-ii/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * Given two arrays, write a function to compute their intersection.
 *
 * Example:
 * Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
 *
 * Note:
 * Each element in the result should appear as many times as it shows in both arrays.
 * The result can be in any order.
 *
 * Follow up:
 * What if the given array is already sorted? How would you optimize your algorithm?
 * What if nums1's size is small compared to num2's size? Which algorithm is better?
 * What if elements of nums2 are stored on disk, and the memory is limited such that you
 * cannot load all elements into the memory at once?
 *
 ***************************************************************************************/
 '''

 class Solution:
     
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        count = {}

        for num in nums1 + nums2:
            count[num] = 0

        for num in nums1:
            count[num] += 1

        for num in nums2:
            if count[num] > 0:
                res.append(num)
                count[num] -= 1
        return res
