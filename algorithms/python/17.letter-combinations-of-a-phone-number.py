#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def __init__(self):
        self.answers = []
        self.answer = ''
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    def letterCombinations(self, digits):
        if not digits: return []
        self.get_string_on_i_of_digits(digits, 0) # (digits, i)
        return self.answers
    def get_string_on_i_of_digits(self, digits, index):
        if index > len(digits) - 1:
            self.answers.append(self.answer)
            return 
        letters = self.letter_map[digits[index]]
        for letter in letters:
            self.answer += letter
            self.get_string_on_i_of_digits(digits, index + 1)
            self.answer = self.answer[:-1]       
# @lc code=end

