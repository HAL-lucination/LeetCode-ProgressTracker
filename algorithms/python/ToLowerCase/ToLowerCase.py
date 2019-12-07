'''
// Source : https://leetcode.com/problems/to-lower-case/description/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
 * Example 1:
 * Input: "Hello"
 * Output: "hello"
 * Example 2:
 * Input: "here"
 * Output: "here"
 * Example 3:
 * Input: "LOVELY"
 * Output: "lovely"
 ***************************************************************************************/
'''

class Solution:
    
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        input = list(str)
        for i in range(0, len(input)):
            if ord(input[i]) in range(65,90):
                input[i] = chr(ord(input[i]) + 32)
            else:
                pass
        return ''.join(input)
