class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        close = openn = n
        op = ""
        rslt = []
        self.solve(openn, close, op, rslt)
        return rslt

    def solve(self, openn, close, op, rslt):
        if openn == 0 and close == 0:
            rslt.append(op)
            return
        
        if openn !=0:
            temp = op
            temp+='('
            self.solve(openn-1, close,temp, rslt)
        
        if close > openn:
            temp = op
            temp+=')'
            self.solve(openn, close-1, temp, rslt)

