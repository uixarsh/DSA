class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 in s2:
            return True
        else:
            # Store frequency of characters in s1
            freq = [0]*26
            for ele in s1:
                freq[ord(ele)-97] +=1
            
            Ns1 = len(s1)
            Ns2 = len(s2)
            for i in range(Ns2):
                temp = [0]*26
                for j in range(i, i+Ns1):
                    if j == Ns2:
                        return False
                    temp[ord(s2[j])-97] +=1

                if temp == freq:
                    return True
        
            return False

