class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def solve(opn, cl, out, rslt):
            if opn == 0 and cl == 0:
                rslt.append(out)
                return

            if opn != 0:
                op1 = out
                op1 += '('
                solve(opn-1, cl, op1, rslt)
            
            if cl > opn:
                op2 = out
                op2 += ')'
                solve(opn, cl-1, op2, rslt)

        opn = cl = n
        rslt = []
        out = ""

        solve(opn, cl, out, rslt)
        return rslt