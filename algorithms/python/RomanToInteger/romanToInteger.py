'''
// Source : https://oj.leetcode.com/problems/roman-to-integer/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Given a roman numeral, convert it to an integer.
*
* Input is guaranteed to be within the range from 1 to 3999.
*
**********************************************************************************/
'''

class Solution(object):

    def romanToInt(self, s):
        numeral_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        sum = 0
        for i in xrange(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i - 1]]:
                sum += numeral_map[s[i]] - 2 * numeral_map[s[i - 1]]
            else:
                sum += numeral_map[s[i]]
        return sum
