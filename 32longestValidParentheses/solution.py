# https://leetcode.com/problems/longest-valid-parentheses/description/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return 0
    
'''
solution notes
( = open
) = close

first character must be open
last character must be close
total # opens = # closes
at any given point you can always add an open
at any given point you can only add a close if # opens > # closes
at any given point you can only add an open if # opens - # closes < remaining
characters in the string

'''