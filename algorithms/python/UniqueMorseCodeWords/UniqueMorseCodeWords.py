'''
// Source : https://leetcode.com/problems/unique-morse-code-words/description/
// Author : Hal
// Date   : 2019-12-07

/***************************************************************************************
 *
 * International orse Code defines a standard encoding where each letter is mapped to
 * a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c"
 * maps to "-.-.", and so on.
 *
 * For convenience, the full table for the 26 letters of the English alphabet is given
 * below:
 *
 *
 * [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.",
 * "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
 *
 * Now, given a list of words, each word can be written as a concatenation of the orse
 * code of each letter. For example, "cab" can be written as "-.-.-....-", (which is
 * the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation, the
 * transformation of a word.
 *
 * Return the number of different transformations among all words we have.
 *
 *
 * Example:
 * Input: words = ["gin", "zen", "gig", "msg"]
 * Output: 2
 * Explanation:
 * The transformation of each word is:
 * "gin" -> "--...-."
 * "zen" -> "--...-."
 * "gig" -> "--...--."
 * "msg" -> "--...--."
 *
 * There are 2 different transformations, "--...-." and "--...--.".
 *
 *
 *
 *
 * Note:
 *
 *
 * 	The length of words will be at most 100.
 * 	Each words[i] will have length in range [1, 12].
 *     words[i] will only consist of lowercase letters.
 ***************************************************************************************/
'''

class Solution(object):

    def stringToMorse(word):

        import string
        alphabetlist = list(string.ascii_lowercase)
        morselist = [".-","-...","-.-.","-..",".","..-.","--.","....",".."
        ,".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
        "..-","...-",".--","-..-","-.--","--.."]
        morsedict = dict(zip(alphabetlist, morselist))

        result = []
        for letter in word:
            result.append(morsedict[letter])
        result = ''.join(result)
        return result

    def uniqueMorseRepresentations(self, words):

        outputs = []
        for word in words:
            outputs.append(Solution.stringToMorse(word))
        return len(set(outputs))
