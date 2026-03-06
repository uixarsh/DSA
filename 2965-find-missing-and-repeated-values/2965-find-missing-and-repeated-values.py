class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # SUM
        # 1 to n2 ka sum
        # 1+2+3+4 = 10
        ''' 
        1 3
        2 4


        9 1 7
        8 9 2
        3 4 6

        map = {1:, 2: 3: ......}

        mpp = {0: key, 1: key, 2: key}
        '''

        mpp = {}
        n = len(grid)
        for i in range(1, int(n**2)+1):
            mpp[i] = 0

        for i in range(n):
            for j in range(n):
                mpp[grid[i][j]]+=1

        rslt = [0, 0]

        for k, v in mpp.items():
            if v==2:
                rslt[0] = k
            if v==0:
                rslt[1] = k

        return rslt

