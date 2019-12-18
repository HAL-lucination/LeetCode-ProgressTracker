'''
// Source : https://oj.leetcode.com/problems/zigzag-conversion/
// Author : Hal
// Date   : 2019-12-18

/**********************************************************************************
*
* The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
* (you may want to display this pattern in a fixed font for better legibility)
*
* P   A   H   N
* A P L S I I G
* Y   I   R
*
* And then read line by line: "PAHNAPLSIIGYIR"
*
* Write the code that will take a string and make this conversion given a number of rows:
*
* string convert(string text, int nRows);
*
* convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
*
*
**********************************************************************************/
'''
s = 'ABC'
n = 2

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # edge cases
        if len(s) <= numRows:
            return s
        if numRows == 1:
            return s

        mat = [[None for i in range(len(s) // 2 + 1)] for j in range(numRows)]
        pointer = 0
        integer = len(s) // numRows + 1
        col = -1

        for x in range(0, 2 * integer, 2):

            # when the pointer is on downward straight lines
            if pointer >= (numRows - 1) * x and pointer <= (numRows - 1) * (x + 1):
                col += 1
                for row in range(0, numRows):
                    if pointer >= len(s):
                        break
                    mat[row][col] = s[pointer]
                    pointer += 1

            # when the pointer is on diagonal straight lines
            if pointer > (numRows - 1) * (x + 1) and pointer < 2 * (numRows - 1) * (x + 1):
                for row in reversed(range(1, numRows - 1)):
                    if pointer >= len(s):
                        break
                    col += 1
                    mat[row][col] = s[pointer]
                    pointer += 1

        res = ''

        for ele1 in mat:
            for ele2 in ele1:
                if ele2 != None:
                    res += ele2

        return res
