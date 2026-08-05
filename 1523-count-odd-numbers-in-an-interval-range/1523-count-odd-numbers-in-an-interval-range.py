class Solution:
    def countOdds(self, low: int, high: int) -> int:
        l=low%2
        h=high%2
        if l==0 and h==0:
            return int((high-low)/2)
        else:
            return int((high-low+1)/2+0.5)  
       
            