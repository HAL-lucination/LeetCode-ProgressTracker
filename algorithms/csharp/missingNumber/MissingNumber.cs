// Source : https://leetcode.com/problems/missing-number/
// Author : Hal
// Date   : 2019-12-07

/*************************************************************************************** 
 *
 * Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the 
 * one that is missing from the array.
 * 
 * For example,
 * Given nums = [0, 1, 3] return 2.
 * 
 * Note:
 * Your algorithm should run in linear runtime complexity. Could you implement it using 
 * only constant extra space complexity?
 * 
 * Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating 
 * all test cases.
 *               
 ***************************************************************************************/

public class Solution {
	
    public int MissingNumber(int[] nums) {
        int sum = nums.Sum();
        int len = nums.Length;
        int sum_new = (len + 1) * len / 2;
        return (sum_new - sum);
    }
}