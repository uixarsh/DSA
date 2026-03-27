class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        mat_cpy = [row[:] for row in mat]
        k = k % len(mat[0])
        
        while k:
            for row in range(len(mat_cpy)):
                if row % 2 == 0:
                    x = mat_cpy[row].pop(0)
                    mat_cpy[row].append(x)
                else:
                    y = mat_cpy[row].pop()
                    mat_cpy[row].insert(0, y)
            k-=1

        return mat_cpy == mat
