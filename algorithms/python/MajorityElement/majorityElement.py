'''
// Source : https://oj.leetcode.com/problems/majority-element/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
 *
 * Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
 *
 * You may assume that the array is non-empty and the majority element always exist in the array.
 *
 * Credits:Special thanks to @ts for adding this problem and creating all test cases.
 *
 **********************************************************************************/
'''

class Solution:
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = set(nums)
        for element in elements:
            count = nums.count(element)
            if count > 0.5 * len(nums):
                return element
