// Source : https://leetcode.com/problems/reverse-string/
// Author : Hal
// Date   : 2019-12-07

/*************************************************************************************** 
 *
 * Write a function that takes a string as input and returns the string reversed.
 * 
 * Example:
 * Given s = "hello", return "olleh".
 ***************************************************************************************/

public class Solution {
	
    public string ReverseString(string s) {
        char[] arr = s.ToCharArray();
        Array.Reverse(arr);
        return new string(arr);
    }
}