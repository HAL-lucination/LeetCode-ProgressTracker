'''
// Source : https://oj.leetcode.com/problems/remove-element/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Given an array and a value, remove all instances of that value in place and return the new length.
*
* The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*
*
**********************************************************************************/
'''
class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = (i for i in nums if i != val)
