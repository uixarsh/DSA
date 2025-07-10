class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        close = openn = n
        op = []
        rslt = []
        self.solve(openn, close, op, rslt)
        return rslt

    def solve(self, openn, close, op, rslt):
        if openn == 0 and close == 0:
            rslt_str = "".join(op)
            rslt.append(rslt_str)
            return
        
        if openn != 0:
            op.append('(')
            self.solve(openn-1, close, op, rslt)
            op.pop()
        
        if close > openn:
            op.append(')')
            self.solve(openn, close-1, op, rslt)
            op.pop()

