class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solve(op, cl, rslt, pair):
            if op==0 and cl==0:
                new_str = "".join(pair)
                rslt.append(new_str)
                return
            
            if op > 0:
                pair.append('(')
                solve(op-1, cl, rslt, pair)
                pair.pop()
            
            if op < cl:
                pair.append(')')
                solve(op, cl-1, rslt, pair)
                pair.pop()
                        

        rslt = [] 
        solve(n, n, rslt, [])
        return rslt