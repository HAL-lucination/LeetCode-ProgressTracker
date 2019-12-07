'''
// Source : https://leetcode.com/problems/move-zeroes/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * Given an array nums, write a function to move all 0's to the end of it while
 * maintaining the relative order of the non-zero elements.
 *
 * For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should
 * be [1, 3, 12, 0, 0].
 *
 * Note:
 * You must do this in-place without making a copy of the array.
 * Minimize the total number of operations.
 *
 * Credits:
 * Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
 *
 ***************************************************************************************/
'''

class Solution:
    
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        res = []
        for num in nums:
            if num != 0: res.append(num)
        res.extend([0] * (len(nums) - len(res)))
        for i in range(0,len(nums)): nums[i] = res[i]
