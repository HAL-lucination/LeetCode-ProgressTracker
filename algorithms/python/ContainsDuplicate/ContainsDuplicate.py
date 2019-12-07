'''
// Source : https://leetcode.com/problems/contains-duplicate/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
 *
 * Given an array of integers, find if the array contains any duplicates.
 * Your function should return true if any value appears at least twice in the array,
 * and it should return false if every element is distinct.
 *
 **********************************************************************************/
'''

class Solution:
    
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
