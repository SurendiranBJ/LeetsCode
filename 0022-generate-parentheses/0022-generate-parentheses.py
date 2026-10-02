class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack=[]
        r=l=0
        ans=[]
        def dfs(r,l,st):
            nonlocal ans
            if r==n and l==n:
                ans.append(''.join(st))
                return 
            if l<n:
                dfs(r,l+1,st+['('])
            if r<l:
                dfs(r+1,l,st+[')'])
            if len(st)==0:
                return
            p=st.pop()
            if p=='(':
                l-=1
            else:
                r-=1    
        dfs(0,0,[])        
        return ans
