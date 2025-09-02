class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []

        if k == n:
            return "0"

        for i in num:
            while k>0 and st and int(i) < int(st[-1]):
                st.pop()
                k-=1
            st.append(i)

        if k>0:
            for i in range(len(st), len(st)-k, -1):
                st.pop()
        
        while st:
            if st[0] == '0':
                st.pop(0)
            else:
                break
            
        if not st:
            return "0"
        
        x = "".join(st)
        return x