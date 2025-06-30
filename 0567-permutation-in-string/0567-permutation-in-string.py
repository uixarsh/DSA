class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 in s2:
            return True
        else:
            # Store frequency of characters in s1
            freq = [0]*26
            # 0 1 2 3.... 25 = 26 charcters
            for ele in s1:
                freq[ord(ele)-97] +=1
            
            Ns1 = len(s1)
            Ns2 = len(s2)

            for i in range(Ns2):
                temp = [0]*26   # Temp. freq array of new window
                # Sliding window of same length as that of s1 and move the window continuously.
                
                for j in range(i, i+Ns1):
                    if j == Ns2:    # if only one ele is left in window.
                        return False
                    temp[ord(s2[j])-97] +=1 

                if temp == freq:
                    return True
        
            return False

