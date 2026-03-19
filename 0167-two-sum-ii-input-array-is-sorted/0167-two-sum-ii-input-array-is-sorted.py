class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = (n-1)

        if n < 2:
            return []

        while i<j:
            calc = numbers[i] + numbers[j]

            if calc == target:
                return [i+1, j+1]

            if calc < target:
                i+=1
            else:
                j-=1
