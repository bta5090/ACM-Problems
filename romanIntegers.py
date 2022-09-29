class Solution:
    def romanToInt(self, s: str) -> int:
        
        sum = 0
        i = 0
        
        while i < len(s):
            
            
            if s[i:i+2] == 'CM':
                sum += 900
                i += 2
                continue
            elif s[i:i+2] == 'CD':
                sum += 400
                i += 2
                continue
            elif s[i:i+2] == 'XC':
                sum += 90
                i += 2
                continue
            elif s[i:i+2] == 'XL':
                sum += 40
                i += 2
                continue
            elif s[i:i+2] == 'IX':
                sum += 9
                i += 2
                continue
            elif s[i:i+2] == 'IV':
                sum += 4
                i += 2
                continue
                
            elif s[i] == 'M':
                sum += 1000
                i += 1
                continue
            elif s[i] == 'D':
                sum += 500
                i += 1
                continue
            elif s[i] == 'C':
                sum += 100
                i += 1
                continue
            elif s[i] == 'L':
                sum += 50
                i += 1
                continue
            elif s[i] == 'X':
                sum += 10
                i += 1
                continue
            elif s[i] == 'V':
                sum += 5
                i += 1
                continue
            elif s[i] == 'I':
                sum += 1
                i += 1
                continue
        
        return sum
