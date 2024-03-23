# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return [P().to_str()]

class P:
    '''Parentheses class'''
    def __init__(self, children = []):
        self.children = children 
    
    def to_str(self):
        if len(self.children) == 0:
            return '()'
        return f'({"".join([c.to_str() for c in self.children])})'

p = P(children=[P(), P([P()])])
print(p.to_str())


# Recursive approach
# You nave n steps to complete
# The first step is always creating a single closed parentheses
# From there you branch to either appending a parentheses or adding a subparantheses to one of the existing sets of parantheses
# Best way to keep track is probably a node structure where each parentheses node can have child parantheses
# 1 ()
    
# 2a ()()
# 2b (())
    
# 3a1 ()()()
# 3a2 (())()
# 3a3 ()(())
    
# 3b1 (()())
# 3b2 ((())) 
