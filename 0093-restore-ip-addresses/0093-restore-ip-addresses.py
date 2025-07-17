class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        # If Input is greater than 12 then there can't be a valid IP Address as not dot can contain more than 3 integers ...
        if len(s) > 12:
            return res

        def backtrack(curr_idx, dots, ip_add):
            # Base Case
            if dots == 4 and curr_idx == len(s):
                res.append(ip_add[:-1])
            
            if dots>4: 
                return # Prune path

            for i in range(curr_idx, min(len(s), curr_idx+3)):  # a max of 3 choices
                choice = s[curr_idx : i+1]

                if len(choice) > 1 and choice[0] == '0':  # leading zero invalid
                    continue
                    
                if choice and 0 <= int(choice) < 256:
                    # it is a valid choice
                    backtrack(i+1, dots+1, (ip_add+choice+'.'))

        backtrack(0,0,"")
        return res