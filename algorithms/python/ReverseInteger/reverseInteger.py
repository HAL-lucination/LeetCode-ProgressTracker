'''
// Source : https://oj.leetcode.com/problems/reverse-integer/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Reverse digits of an integer.
*
* Example1: x =  123, return  321
* Example2: x = -123, return -321
*
*
* Have you thought about this?
*
* Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
*
* > If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
*
* > Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
*   then the reverse of 1000000003 overflows. How should you handle such cases?
*
* > Throw an exception? Good, but what if throwing an exception is not an option?
*   You would then have to re-design the function (ie, add an extra parameter).
*
*
**********************************************************************************/
'''

import re

class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x >= 0:
            y = str(x)
            new_list = []
            for i in range(len(y) - 1, -1, -1):
                new_list.append(y[i])
            new_int = ''.join(new_list)
            if abs(int(new_int)) > 2**31:
                return 0
            else:
                return int(new_int)

        else:
            x = -x
            y = str(x)
            new_list = []
            for i in range(len(y) - 1, -1, -1):
                new_list.append(y[i])

            new_int = ''.join(new_list)
            if abs(int(new_int)) > 2**31:
                return 0
            else:
                return (-int(new_int))
