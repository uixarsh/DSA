class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum = 0 
        rsum = 0
        maxSum = 0
        n = len(cardPoints)
        for i in range(0, k):
            lsum+=cardPoints[i]
        maxSum=lsum
        r_idx=(n-1)
        for i in range((k-1), -1, -1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[r_idx]
            r_idx-=1
            maxSum = max(maxSum, (lsum+rsum))
            
        return maxSum