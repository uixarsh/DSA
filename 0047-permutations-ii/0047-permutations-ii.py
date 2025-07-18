class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        lst = []
        self.find_permutations(nums, 0, lst)
        return lst
    
    def find_permutations(self, ip : List[int], start : int, rslt : List[int]) -> None:
        
        if start == len(ip)-1:
            rslt.append(ip[:])
            return
        
        used = set()
        for i in range(start, len(ip)):
            
            if ip[i] in used:
                continue

            used.add(ip[i])
            ip[start], ip[i] = ip[i], ip[start]
            self.find_permutations(ip, start+1, rslt)
            ip[start], ip[i] = ip[i], ip[start]     # Backtracking