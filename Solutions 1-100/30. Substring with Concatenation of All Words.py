from typing import List
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount
        result = []
        wordDict = Counter(words)

        for i in range(wordLen):
            left = right = i
            count = 0
            currentDict = Counter()

            while right + wordLen <= len(s):
                currentWord = s[right: right + wordLen]
                right += wordLen
                count += 1

                if currentWord in wordDict:
                    currentDict[currentWord] += 1
                    while currentDict[currentWord] > wordDict[currentWord]:
                        leftWord = s[left: left + wordLen]
                        left += wordLen
                        currentDict[leftWord] -= 1
                        count -= 1

                    if count == wordCount:
                        result.append(left)

                else:
                    currentDict.clear()
                    count = 0
                    left = right

        return result


s = Solution()
print(s.findSubstring("barfoothefoobarman", ["foo","bar"]))
print(s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]))
print(s.findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
