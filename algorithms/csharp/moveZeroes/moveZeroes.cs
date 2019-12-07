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


public class Solution {
	
    public void MoveZeroes(int[] nums) {
        int l = nums.Length;
        int[] newarray = new int[l];
        
        int n = 0;
        int m = 0;
        
        while (m < l)
        {
            if(nums[m] != 0)
            {
                newarray[n] = nums[m];
                m += 1;
                n += 1;
            }
            else
            {
                m += 1;
            }
        }
        
       for(int i = 0; i < l; i++)
       {
           nums[i] = newarray[i];
       }
        
    }
}