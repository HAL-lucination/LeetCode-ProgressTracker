'''
// Source : https://leetcode.com/problems/score-after-flipping-matrix/description/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * We have a two dimensional matrix A where each value is 0 or 1.
 * A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
 * After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
 * Return the highest possible score.
 *
 * Example 1:
 * Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
 * Output: 39
 * Explanation:
 * Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
 * 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
 * Note:
 * 1 <= A.length <= 20
 * 1 <= A[0].length <= 20
 * A[i][j] is 0 or 1.
 ***************************************************************************************/
'''

class Solution:
    
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        input = A

        import numpy as np
        input = np.array(input)
        result = [[]] * len(input)
        for i in range(len(input)):
            if input[i][0] != 1:
                result[i] = ([1] * len(input[i]) - input[i])
            else:
                result[i] = input[i]

        tpinput = np.array(result).transpose()
        tpresult = [[]] * len(tpinput)

        for i in range(len(tpinput)):
            if tpinput[i].tolist().count(0) > tpinput[i].tolist().count(1):
                tpresult[i] = ([1] * len(tpinput[i]) - tpinput[i])
            else:
                tpresult[i] = tpinput[i]

        tpresult = np.array(tpresult).tolist()

        sum = 0
        for i in range(len(tpresult)):
            weight = 2 ** (len(tpresult) - 1 - i)
            sum += tpresult[i].count(1) * weight

        return sum
