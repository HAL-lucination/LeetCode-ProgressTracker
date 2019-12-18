'''
// Source : https://oj.leetcode.com/problems/longest-palindromic-substring/
// Author : Hal
// Date   : 2019-12-18

/**********************************************************************************
*
* Given a string S, find the longest palindromic substring in S.
* You may assume that the maximum length of S is 1000,
* and there exists one unique longest palindromic substring.
*
**********************************************************************************/
'''


'''
# Brute force to find all substrings, check reverse, store the longest. Too slow

def longestPalindrome(s: str) -> str:
    from itertools import combinations
    permutation = [s[x:y] for x, y in combinations(range(len(s) + 1), r = 2)]

    res = ''
    for substring in permutation:
        if list(substring)[::] == list(substring)[::-1]:
            if len(list(substring)) >= len(res):
                res = substring

    print(res)

if __name__ == "__main__":
    longestPalindrome(s)
'''

'''
# Start from the first index, check smallest window (2), if find symmetric one,
# search the neighbor two elements, if not symmetric, increase the window size
# and start another loop.
#
# Underlying problem: only two loops are necessary (single element and two
# elements), further loops are unnecessary.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''

        index = 0
        window = 2
        out = s[0:1]

        while True:
            # judge if current string is symmetric
            if list(s[index:index + window])[::] == list(s[index:index + window])[::-1]:
                # judge if its longest
                if len(list(s[index:index + window])) > len(list(out)):
                    out = s[index:index + window]
                    index -= 1
                    # judge expending one window is still the longest, need to consider egde case:
                    # Left edge
                    if index < 0:
                        index += 1
                        window += 1
                        if list(s[index : index + window])[::] != list(s[index : index + window])[::-1]:
                            window -= 1
                            index += 1
                        else:
                            out = s[index:index + window]
                    # right edge
                    if index + window + 2 > len(s):
                        window += 1
                        if list(s[index : index + window])[::] != list(s[index : index + window])[::-1]:
                            window -= 1
                            index += 2
                        else:
                            out = s[index:index + window]
                    else:
                        window += 2
                        if list(s[index : index + window + 2])[::] != list(s[index : index + window + 2])[::-1]:
                            window -= 2
                            index += 2
                        else:
                            out = s[index:index + window]
                    # if not longest, try next index
                else:
                    index += 1
            # if not symmetric, try next index
            else:
                index += 1
            if index + window > len(s):
                index = 0
                window += 1
            if window > len(s):
                return out
'''

s = "abcbadefabcba"

def longestPalindrome(s: str) -> str:
    max = 1

    # check every element in the string
    for pivot in range(1, len(s)):
        # when the length of substring is odd
        left = pivot - 1
        right = pivot + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max:
                max = right - left + 1
                start = left
            left -= 1
            right += 1

        # when the length of substring is even
        left = pivot - 1
        right = pivot
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max:
                max = right - left + 1
                start = left
            left -= 1
            right += 1

    return s[start:start + max]

print(longestPalindrome(s))
