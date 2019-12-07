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
public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        var res = new int[numRows][];
        for (int y = 0; y < numRows; y++)
        {
            var row = res[y] = new int[y + 1];
            row[0] = row[y] = 1;
            for (int x = 1; x < y; x++)
                row[x] = res[y - 1][x - 1] + res[y - 1][x];
        }
        return res;
    }
}
