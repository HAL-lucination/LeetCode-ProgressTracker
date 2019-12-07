'''
// Source : https://oj.leetcode.com/problems/two-sum/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Given an array of integers, find two numbers such that they add up to a specific target number.
*
* The function twoSum should return indices of the two numbers such that they add up to the target,
* where index1 must be less than index2. Please note that your returned answers (both index1 and index2)
* are not zero-based.
*
* You may assume that each input would have exactly one solution.
*
* Input: numbers={2, 7, 11, 15}, target=9
* Output: index1=1, index2=2
*
*
**********************************************************************************/
'''

def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    result = []

    for first_num_index in range(len(nums)):
        for second_num_index in range(first_num_index + 1, len(nums)):
          if nums[first_num_index] + nums[second_num_index] == target:
              result.append(first_num_index)
              result.append(second_num_index)
    return result
