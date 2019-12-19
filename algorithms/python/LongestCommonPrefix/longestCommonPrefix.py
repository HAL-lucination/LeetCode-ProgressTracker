'''
// Source : https://oj.leetcode.com/problems/longest-common-prefix/
// Author : Hal
// Date   : 2019-12-19

/**********************************************************************************
*
* Write a function to find the longest common prefix string amongst an array of strings.
*
**********************************************************************************/
'''
strs = ['']

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if strs == []:
            return ""

        strs.sort(key = len)
        res = []
        for index in range(len(strs[0])):
            for element in range(len(strs)):
                if strs[element][index] != strs[0][index]:
                    return ''.join(res)
            res.append(strs[0][index])
        return ''.join(res)

    print(longestCommonPrefix(strs))
