# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits):
      digits = list(digits)
      digits = [int(d) for d in digits]
      if len(digits) == 0:
        return []

      letters = self.getLetters(digits[0])    

      for d in digits[1:]:
        letters = self.appendLetters(letters, self.getLetters(d))
      return letters
    
    def appendLetters(self, input, added):
      out = []
      for i in input:
        for a in added:
          out.append(i+a)
      return out

    def getLetters(self, digit):
      if digit == 2:
        return ['a','b','c']
      elif digit == 3:
        return ['d','e','f']
      elif digit == 4:
        return ['g','h','i']
      elif digit == 5:
        return ['j','k','l']
      elif digit == 6:
        return ['m','n','o']
      elif digit == 7:
        return ['p','q','r','s']
      elif digit == 8:
        return ['t','u','v']
      elif digit == 9:
        return ['w','x','y','z']




solution = Solution()

digits = '23'
result = solution.letterCombinations(digits)
print(f'{result=}')