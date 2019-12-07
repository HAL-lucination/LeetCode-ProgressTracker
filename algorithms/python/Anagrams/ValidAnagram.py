'''
// Source : https://leetcode.com/problems/valid-anagram/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
 *
 * Given two strings s and t, write a function to determine if t is an anagram of s.
 *
 * For example,
 * s = "anagram", t = "nagaram", return true.
 * s = "rat", t = "car", return false.
 *
 * Note:
 * You may assume the string contains only lowercase alphabets.
 *
 **********************************************************************************/
'''
class Solution:
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(list(s))
        t = sorted(list(t))

        if s == t:
            return True
        else:
            return False
