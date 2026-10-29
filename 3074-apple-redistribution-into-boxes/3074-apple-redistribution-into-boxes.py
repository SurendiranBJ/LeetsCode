class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        aa=sum(apple)
        capacity.sort(reverse=True)
        i=0
        ans=0
        while i!=len(capacity):
            if aa<=0:
                return i
            else:
                aa-=capacity[i]
            i+=1
        return i

