'''
// Source : https://oj.leetcode.com/problems/add-two-numbers/
// Author : Hal
// Date   : 2019-12-07

/**********************************************************************************
*
* You are given two linked lists representing two non-negative numbers.
* The digits are stored in reverse order and each of their nodes contain a single digit.
* Add the two numbers and return it as a linked list.
*
* Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
* Output: 7 -> 0 -> 8
*
**********************************************************************************/
'''

class Solution:

    def getNum(self, firstnode):
        currentnode = firstnode
        counter = 0
        num = 0
        i = 1
        while currentnode != None:
            num += (i * currentnode.val)
            i *= 10
            currentnode = currentnode.next
        return num

    def stringToListNode(self, stringTotal):
        previousNode = None
        first = None
        for i in stringTotal:
            currentNode = ListNode(int(i))
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode
        return first

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = self.getNum(l2) + self.getNum(l1)
        res = str(res)[::-1]
        return self.stringToListNode(res)
