class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        isPrime = [True for _ in range(max(n+1, 3))]
        isPrime[0] = False
        isPrime[1] = False
        for i in range(2, int(math.sqrt(n))+2):
            mul = 2
            if isPrime[i]:
                while i*mul <= n:
                    isPrime[i*mul] = False
                    mul += 1
        ans = []
        for i in range((n//2)+1):
            if isPrime[i]:
                if isPrime[n-i]:
                    ans.append((i, n-i))
        return ans
                    
            
        
                