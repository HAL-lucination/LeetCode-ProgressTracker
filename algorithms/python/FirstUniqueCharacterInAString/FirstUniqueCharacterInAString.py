'''
// Source : https://leetcode.com/problems/first-unique-character-in-a-string/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * Given a string, find the first non-repeating character in it and return it's index.
 * If it doesn't exist, return -1.
 *
 * Examples:
 *
 * s = "leetcode"
 * return 0.
 *
 * s = "loveleetcode",
 * return 2.
 *
 * Note: You may assume the string contain only lowercase letters.
 ***************************************************************************************/
'''

class Solution:

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for letter in s:
            if letter not in hash:
                hash[letter] = 0
            hash[letter] += 1

        for index, letter in enumerate(s):
            if hash[letter] == 1:
                return index
        return -1
