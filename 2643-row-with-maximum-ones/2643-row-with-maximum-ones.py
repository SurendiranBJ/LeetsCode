class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans=0
        row=0
        for i in range(len(mat)):
            c=mat[i].count(1)
            if c>ans:
                ans=c
                row=i
        return [row,ans]
