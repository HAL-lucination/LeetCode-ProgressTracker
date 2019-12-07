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

public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int len = nums.Length;
    int index = 0;
    while (index < len)
    {
        if (nums[index] == val)
        {
            nums[index] = nums[len-1];
            len--;
        }
        else
        {
            index++;        
        }
    }
    
    return len;
    }
}
