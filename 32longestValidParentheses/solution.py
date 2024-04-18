# https://leetcode.com/problems/longest-valid-parentheses/description/


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        longest = 0
        
        if len(s)< 2:
            return longest

        
        for i in range(0,len(s)):
            curr_length = 0
            num_opens = 0
            num_closes = 0
            for j in range(i, len(s)):  
                # print(i,j)
                if i == j and s[j] == ')':
                    break 
                
                if s[j] == '(':
                    if num_opens - num_closes < (len(s) - j) - 1:
                        num_opens +=1
                    else:
                        break
                
                if s[j] == ')':
                    if num_opens > num_closes:
                        num_closes +=1
                        if num_closes == num_opens and curr_length + 1 > longest:
                            longest = curr_length + 1
                    else:
                        break
                
                curr_length += 1
            # print(f'{longest=} {curr_length=}, {num_closes=}, {num_opens=}')
            
        return longest
    
Solution().longestValidParentheses('(())()(()((')
    
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