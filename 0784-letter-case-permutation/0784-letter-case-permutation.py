class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def solve(s, op, ans):
            if len(s) == 0:
                ans.append(op)
                return

            if s[0].isalpha():
                op1 = s[0].lower()
                op2 = s[0].upper()
                s = s[1:]
                solve(s, op+op1, ans)
                solve(s, op+op2, ans)
            else:
                op = op+s[0]
                s = s[1:]
                solve(s, op, ans)

        ans = []
        solve(s, "", ans)
        return ans   