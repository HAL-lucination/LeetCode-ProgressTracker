'''
// Source : https://oj.leetcode.com/problems/pascals-triangle/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* Given numRows, generate the first numRows of Pascal's triangle.
*
* For example, given numRows = 5,
* Return
*
* [
*      [1],
*     [1,1],
*    [1,2,1],
*   [1,3,3,1],
*  [1,4,6,4,1]
* ]
*
*
**********************************************************************************/
'''

class Solution:

    def generate(self, numRows: 'int') -> 'List[List[int]]':
        # initialize the result
        res = []
        # y is y-th row (or y-axis)
        for y in range(numRows):
            # populate the row with null elements
            row = [None for _ in range(y + 1)]
            # assign 1 to the start and end to every row
            row[0], row[-1] = 1, 1
            # x is the x-th element in that row (or x-axis)
            for x in range(1, len(row) - 1):
                # Calculate this element based on other 2
                row[x] = res[y - 1][x - 1] + res[y - 1][x]
            # After each row is finished, append to the triangle
            res.append(row)

        return res
