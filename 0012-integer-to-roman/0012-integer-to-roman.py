class Solution:
    def intToRoman(self, num: int) -> str:
        # List of value-symbol pairs in descending order, including subtractive notations
        value_symbols = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = []
        
        for val, symbol in value_symbols:
            if num == 0:
                break
            # Determine how many times the current symbol fits into num
            count = num // val
            if count > 0:
                result.append(symbol * count)
                num %= val
                
        return "".join(result)