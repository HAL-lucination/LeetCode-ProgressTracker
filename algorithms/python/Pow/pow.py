'''
// Source : https://oj.leetcode.com/problems/powx-n/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Implement pow(x, n).
*
*
**********************************************************************************/
'''

class Solution:

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n == 0:
            return 1
        else:
            half = self.myPow(x, n//2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x
