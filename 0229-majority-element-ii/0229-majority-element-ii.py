class Solution:
    def majorityElement(self, arr: List[int]) -> List[int]:
        # Find all the element more that n//3 times.
        d = {}
        N=len(arr)
        for i in range(N):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]]+=1
        lst = []
        times = N//3
        for keys,value in d.items():
            if value > times:
                lst.append(keys)

        return lst