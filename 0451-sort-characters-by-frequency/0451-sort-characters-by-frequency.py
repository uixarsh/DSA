class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for ele in s:
            if ele not in d:
                d[ele] = 1
            else:
                d[ele] +=1

        new_d = sorted(d.items(), key=lambda item: item[1], reverse=True)

        s = ""
        for key, val in new_d:
            for i in range(val):
                s+=key

        return s

