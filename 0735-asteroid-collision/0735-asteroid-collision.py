class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        n = len(asteroids)

        for ele in asteroids:
            if ele > 0:
                st.append(ele)
            else:
                while st and st[-1] > 0 and abs(ele) > st[-1]:
                    st.pop()
            
                if st and st[-1] == abs(ele):
                    st.pop()
                elif not st or st[-1] < 0:
                    st.append(ele)

        return st