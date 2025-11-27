class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = self.get_hash(s)
        d2 = self.get_hash(t)
        if d1 == d2:
            return True
        return False
        
    def get_hash(self, s : str) -> dict:
        d = dict()
        for i in s:
            if i not in d:
                d[i] = 0
            else:
                d[i]+=1
        return d