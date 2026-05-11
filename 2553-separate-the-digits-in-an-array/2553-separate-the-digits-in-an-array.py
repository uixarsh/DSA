class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for ele in nums:
            if ele > 9:
                x = str(ele)
                for i in x:
                    answer.append(int(i))
            else:
                answer.append(ele)

        return answer