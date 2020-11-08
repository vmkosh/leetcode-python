class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        for i in range(len(s)):
            result += dict[s[i]]
            if i > 0 and dict[s[i]] > dict[s[i-1]]:
                result -= 2 * dict[s[i-1]]
        return result