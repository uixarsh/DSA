class Solution:
    def combinationSum2(self, candidates: List[int], target: int):

        candidates.sort()   # nlog(n)
        n = len(candidates)

        def solve(idx, summ, curr):

            if summ == target:
                rslt.append(curr[:])
                return

            if idx >= n or summ > target:
                return
            
            ele = candidates[idx]
            if ele > target - summ:
                return

            # NOT PICK
            next_idx = idx + 1
            while next_idx < n and candidates[next_idx] == ele:
                next_idx += 1

            solve(next_idx, summ, curr)

            # PICK
            curr.append(ele)
            solve(idx + 1, summ + ele, curr)
            curr.pop()

        rslt = []
        solve(0, 0, [])
        return rslt



'''     
  [10,1,2,7,6,1,5]
  [1, 1, 2, 5, 6, 7]

                                        f(idx, summ, curr)
                                        f(0, 0, [])
                                    /                   \
                        f(1, 0, [])                                 f(1, 1, [1])
                            /    \                                     / \
                f(2, 0, [])     f(2, 1, [1])            f(2, 1, [1])       f(2, 2, [1, 1])   
                /    \              /   \ 
f(3, 0, [])     f(3, 1, [1])     f(3, 1, [1])   f(3, 2, [1, 1])


            if ele > target - summ:
                return

            8 - 4 = 4 5 > 4
len(arr)

2 choices n branches
2^n

2^7 = 128



'''