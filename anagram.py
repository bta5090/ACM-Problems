
def isAnagram(self, s: str, t: str) -> bool:
        
        countS = {}
        countT = {}
        
        if len(s) != len(t):
            return False
        elif s == t[::-1]:
            return True
        else:
            
            for i in range(len(s)):
                
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
