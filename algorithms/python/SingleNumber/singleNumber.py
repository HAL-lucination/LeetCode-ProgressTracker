'''
// Source : https://oj.leetcode.com/problems/single-number/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Given an array of integers, every element appears twice except for one. Find that single one.
*
* Note:
* Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
*
*
**********************************************************************************/
'''

class Solution:
    
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for num in nums:
            try:
                hash.pop(num)
            except:
                hash[num] = 1

        for key in hash.keys():
            return(key)
