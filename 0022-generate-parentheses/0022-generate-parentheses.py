class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solve(op, cl, rslt, pair):
            if op==0 and cl==0:
                rslt.append(pair)
                return
            
            if op != 0:
                solve(op-1, cl, rslt, pair+'(')
            
            if op < cl:
                solve(op, cl-1, rslt, pair+')')
                        

        rslt = []
        solve(n, n, rslt, "")
        return rslt
        