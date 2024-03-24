# https://leetcode.com/problems/generate-parentheses/

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_count = n -1
        close_count = n
        return self.addParanthesis(open_count, close_count, '(')
    
    def addParanthesis(self, open_count, close_count, curr):
        if open_count ==0 and close_count == 0:
            return [curr]
        if open_count == 0:
            return self.addParanthesis(open_count, close_count-1, curr + ')')
        
        if close_count > open_count:
            return self.addParanthesis(open_count-1, close_count, curr+'(') \
                   + self.addParanthesis(open_count, close_count-1, curr+')')
        
        else:
            return self.addParanthesis(open_count-1, close_count, curr+'(') 



class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return [P().to_str()]

        p_answers = self.recursiveParentheses(n, P())
        return [p.to_str() for p in p_answers]
        
    def recursiveParentheses(self, n: int, p_head: 'P') -> 'List[P]':
        if n == 1:
            p_head.children = [P()]
            return [p_head, P()]
        
        results = [self.recursiveParentheses(n-1,i) for i in p_head.children]
        return results

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

print(Solution().generateParenthesis(2))


# solution 1
# Recursive approach with text based and simple rules
# Another observation is you can keep track of opening and closing in a more 
# simple way since the total number of left and right parentheses is known
# See diagram file for reasoning 
# Keep track of number of available left and right parentheses 

# solution 2 (unfinished)
# Recursive approach with nodes
# You nave n steps to complete
# The first step is always creating a single closed parentheses
# From there you branch to either appending a parentheses or adding a
# subparantheses to one of the existing sets of parantheses
# Best way to keep track is probably a node structure where each parentheses
# node can have child parantheses
# 1 ()
    
# 2a ()()
# 2b (())
    
# 3a1 ()()()
# 3a2 (())()
# 3a3 ()(())
    
# 3b1 (()())
# 3b2 ((())) 

