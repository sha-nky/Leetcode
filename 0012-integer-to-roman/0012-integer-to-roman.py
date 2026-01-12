class Solution:
    def intToRoman(self, num: int) -> str:
        def convertToPlaceValues(num):
            res = []
            i = 0

            while num:
                num, dig = divmod(num, 10)
                res.append(dig * (10 ** i))
                i += 1
            
            return res[::-1]
        
        def convertPlace(num):
            if num == 0:
                return ""
            
            length = len(str(num)) - 1
            dig = num // (10 ** length)

            if length == 0:
                one, five, ten = "I", "V", "X"
            elif length == 1:
                one, five, ten = "X", "L", "C"
            elif length == 2:
                one, five, ten = "C", "D", "M"
            else:
                return "M" * dig
            
            if dig <= 3:
                return one * dig
            if dig == 4:
                return one + five
            if dig <= 8:
                return five + (one * (dig - 5))
            else:
                return one + ten
        
        parts = convertToPlaceValues(num)
        return ''.join(convertPlace(p) for p in parts)
