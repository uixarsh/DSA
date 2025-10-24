class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1, -1]
        
        def bs (occ=None) -> int:
            n = len(nums)
            l = 0
            r = n-1
            res = -1

            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    if nums[mid] == target:
                        res = mid

                    if occ == 'f':  # Check for first occurence.
                        r = mid - 1
                    else:
                        l = mid + 1
            return res
        
        return [bs('f'), bs()]