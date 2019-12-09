'''
// Source : https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
// Author : Hal
// Date   : 2019-12-09

/**********************************************************************************
*
* Given a string, find the length of the longest substring without repeating characters.
* For example, the longest substring without repeating letters for "abcabcbb" is "abc",
* which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
*
**********************************************************************************/
'''

'''
Solution:
Start with an increasing window size, if the new char is not duplicate, expand
the window size, if duplicate, slide the window by one position. If slided
window still include duplicates, continue sliding until reach the end.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == '':
            return 0

        size = 1
        index = 0
        while True:
            if len(s[index : (index + size)]) == len(set(s[index : (index + size)])):
                res = s[index : (index + size)]
                size += 1
            else:
                index += 1
            if (size + index) > len(s):
                return len(res)
