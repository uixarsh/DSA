class Solution:
    def addDigits(self, num: int) -> int:
        # s = num
        # while s > 9:
        #     temp = str(s)
        #     s = sum(int(i) for i in temp)   
        # return s

        if num == 0:
            return 0
        else:
            return 1 + (num - 1) % 9
        
    

              
        