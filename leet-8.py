class Solution:
    #since we don't have str to int, we use simple dictionary as a way to map digits for their respective number
    dict = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
    MIN_VALUE = -2147483648
    MAX_VALUE = 2147483647
    
    def myAtoi(self, s: str) -> int:
        result = 0
        s = s.lstrip()
        if not s: return result
        hasSign = (s[0] == '-' or s[0] == '+')
        isNegative = hasSign and s[0] == '-'
        start = 0        
        if (hasSign): start = 1
        for i in range(start, len(s)):
            digit = Solution.dict.get(s[i])
            if digit == None: break
            if result == Solution.MIN_VALUE: break
            if result < -214748364: 
                result = Solution.MIN_VALUE
                break
            if result == -214748364 and digit > 7: 
                result = Solution.MIN_VALUE
                break
            result =  result * 10 - digit
        if result == Solution.MIN_VALUE and not isNegative: return Solution.MAX_VALUE
        if isNegative: return result
        return -result