class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        r=0
        n=len(fruits)
        d={}
        max_len = 0

        while l<=r and r<n:
            if fruits[r] not in d:
                d[fruits[r]] = 0

            if len(d) <= 2:
                max_len = max(max_len, (r-l+1))
                
            else:
                d[fruits[l]] -=1
                if d[fruits[l]] == 0:
                    d.pop(fruits[l])
                l+=1
                continue
                
            d[fruits[r]] +=1
            r+=1

        return max_len