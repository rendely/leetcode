# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # create set for checking against
        check_set = set(words)

        # word length for managing loop
        word_len = len(words[0])

        # substring length to manage iteration loop
        substring_len = word_len * len(words)

        # string length for managing loops
        s_len = len(s)

        # create used set
        used_set = set()

        # store indices results
        results = []

        # initialize substring starting index
        i = 0

        # exit early if impossible
        if substring_len > s_len:
            return

        # while we enough characters left for substring, increment by one and check
        while i + substring_len < s_len:
            #temporary index for checking substring
            j = i
            #while we keep finding words in the substring
            this_substring = s[j:j+word_len]
            while this_substring in check_set and this_substring not in used_set:
                j = j + word_len
                used_set.add(this_substring)
                this_substring = s[j:j+word_len]
            
            if len(used_set) == len(words):
                results.append(i)
            #reset before next loop
            used_set.clear()
            i = i + 1

        return results


''' Solution Notes 
One approach could be to take the first substring and check if it's in a set of
the words list. If yes, add that to a used_set. keep advancing and checking if
the next substring is in words set but not in used set until all words used

Since set lookup is O(1), this would be O(n*m) where n is string length and m 
is words length

Some ways to save time, check 

'''    