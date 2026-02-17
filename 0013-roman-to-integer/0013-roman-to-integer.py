class Solution:
    def romanToInt(self, s: str) -> int:
        mpp = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        sp = {
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400, 
            "CM" : 900
        }

        n = len(s)
        rslt = 0
        rslt+=mpp[s[0]]
        for i in range(1, n):
            cse = s[i-1] + s[i]
            print(cse)
            if cse not in sp.keys():
                rslt+=mpp[s[i]]
            else:
                rslt -= mpp[s[i-1]]
                rslt+=sp[cse]
        
        return rslt