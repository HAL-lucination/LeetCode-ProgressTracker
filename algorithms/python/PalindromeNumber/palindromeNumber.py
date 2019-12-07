'''
// Source : https://oj.leetcode.com/problems/palindrome-number/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Determine whether an integer is a palindrome. Do this without extra space.
*
*
* Some hints:
*
* Could negative integers be palindromes? (ie, -1)
*
* If you are thinking of converting the integer to string, note the restriction of using extra space.
*
* You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
* you know that the reversed integer might overflow. How would you handle such case?
*
* There is a more generic way of solving this problem.
*
*
**********************************************************************************/
'''

class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        old_num = str(x)
        new_num = old_num[::-1]
        if old_num == new_num:
            return True
        else:
            return False
