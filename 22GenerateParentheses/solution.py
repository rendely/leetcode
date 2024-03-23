# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return [P().to_str()]

        p_answers = self.recursiveParentheses(n, P())
        return [p.to_str() for p in p_answers]
        
    def recursiveParentheses(self, n: int, p_head: 'P') -> 'List[P]':
        if n == 1:
            p_head.children = [P()]
            return [p_head]
        
        return self.recursiveParentheses(n-1, p_head)

class P:
    '''Parentheses class'''
    def __init__(self, children: 'List[P]' = None):
        if children is None:
            children = []
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
