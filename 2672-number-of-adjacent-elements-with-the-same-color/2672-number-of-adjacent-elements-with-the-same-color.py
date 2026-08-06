class Solution:
    def colorTheArray(self, n: int, arr: List[List[int]]) -> List[int]:
        sol=[0]*n
        ans=0
        adj=[]
        for idx,color in arr:
            l=idx-1
            r=idx+1
            if l>=0 and r<n:
                if sol[l]==sol[idx] and sol[l]!=0:
                    ans-=1
                if sol[r]==sol[idx] and sol[r]!=0:
                    ans-=1    
                sol[idx]=color  
                if sol[l]==sol[idx]:
                    ans+=1
                if sol[r]==sol[idx]:
                    ans+=1
            elif l>=0 and r>=n:
                if sol[l]==sol[idx] and sol[l]!=0:
                    ans-=1
                sol[idx]=color
                if sol[l]==color:
                    ans+=1
            elif l<0 and r<n:
                if sol[r]==sol[idx] and sol[r]!=0:
                    ans-=1 
                sol[idx]=color
                if sol[r]==color:
                    ans+=1     
            adj.append(ans)
        return adj                

                    



