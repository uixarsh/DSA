class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dct = {}
        lst=[]
        for ele in nums:
            if ele in dct:
                dct[ele]+=1
            else:
                dct[ele]=0
        for key,val in dct.items():
            if val>0 and val<=2:
                lst.append(key)
        return lst