'''
// Source : https://leetcode.com/problems/product-of-array-except-self/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
 *
 * Given an array of n integers where n > 1, nums, return an array output such that
 * output[i] is equal to the product of all the elements of nums except nums[i].
 *
 * Solve it without division and in O(n).
 *
 * For example, given [1,2,3,4], return [24,12,8,6].
 *
 * Follow up:
 * Could you solve it with constant space complexity? (Note: The output array does not
 * count as extra space for the purpose of space complexity analysis.)
 *
 **********************************************************************************/
'''

class Solution:

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        products = [1] * len(nums)

        tmp = 1
        for index in range(len(nums)):
            products[index] = tmp
            tmp *= nums[index]

        tmp = 1
        for index in reversed(range(len(nums))):
            products[index] *= tmp
            tmp *= nums[index]

        return products
