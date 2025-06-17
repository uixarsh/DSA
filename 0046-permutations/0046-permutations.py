class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = []
        self.find_permutations(nums, [], lst)
        return lst
    
    def find_permutations(self, ip, op, rslt) -> None:
        ip_len = len(ip)
        
        if ip_len == 0:
            rslt.append(op)
            return

        for i in range(ip_len):
            new_ip = ip[0:i] + ip[i+1:]
            new_op = op + [ip[i]]
            self.find_permutations(new_ip, new_op, rslt)