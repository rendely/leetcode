# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # word length for managing loop
        word_len = len(words[0])

        # substring length to manage iteration loop
        substring_len = word_len * len(words)

        # string length for managing loops
        s_len = len(s)

        # create used set
        used_words = []

        # store indices results
        results = []

        # initialize substring starting index
        i = 0

        # exit early if impossible
        if substring_len > s_len:
            return

        # while we enough characters left for substring, increment by one and check
        while i + substring_len <= s_len:
            #temporary index for checking substring
            j = i
            this_substring = s[j:j+word_len]
            
            #while we keep finding words in the substring
            while this_substring in words:
                print('inner')
                print(f'{this_substring=} {words=} {used_words=}')
                j = j + word_len
                words.remove(this_substring)
                used_words.append(this_substring)
                this_substring = s[j:j+word_len]
            
            if len(words) == 0:
                results.append(i)
            #reset before next loop
            words.extend(used_words)
            used_words = []
            i = i + 1
            print('outer')
            print(f'{this_substring=} {words=} {used_words=}')

        return results


''' Solution Notes 
One approach could be to take the first substring and check if it's in a set of
the words list. If yes, add that to a used_set. keep advancing and checking if
the next substring is in words set but not in used set until all words used

Since set lookup is O(1), this would be O(n*m) where n is string length and m 
is words length

Some ways to save time, check 

'''    