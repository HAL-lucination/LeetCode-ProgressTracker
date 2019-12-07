'''
// Source : https://leetcode.com/problems/top-k-frequent-elements/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * Given a non-empty array of integers, return the k most frequent elements.
 *
 * For example,
 * Given [1,1,1,2,2,3] and k = 2, return [1,2].
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
 * Your algorithm's time complexity must be better than O(n log n), where n is the
 * array's size.
 *
 ***************************************************************************************/
'''

class Solution:

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        for num in nums:
            if num not in hash:
                hash[num] = 0
            else:
                hash[num] += 1
        freq = sorted(hash, key=hash.get)
        freq = freq[::-1]
        print("freq list is ", freq)
        res = []
        for i in range(k):
            print(i)
            res.append(freq[i])
        return res
