from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]
                }
        result = []

        if not digits:
            return result

        def recursive(currentCombination, currentDigits):
            if len(currentDigits) == 0:
                result.append(currentCombination)
            else:
                for c in dict[currentDigits[0]]:
                    recursive(currentCombination + c, currentDigits[1:])

        recursive("", digits)
        return result


s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations(""))
print(s.letterCombinations("2"))
