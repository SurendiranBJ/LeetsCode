class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mul=1
        p=[]
        n=len(grid)
        m=len(grid[0])
        l=n*m
        g2=list(map(int,(str(grid).replace('[','').replace(']','').split(','))))
        
        prefix=[0]*(l)
        suffix=[0]*(l)
        prefix[0]=g2[0]%12345
        suffix[l-1]=g2[l-1]%12345
        i=1
        j=l-2   
        while i!=l and j!=-1:
            prefix[i]=(prefix[i-1]*g2[i])%12345
            suffix[j]=(suffix[j+1]*g2[j])%12345
            i+=1
            j-=1
        r=[]    
        for i in range(l):
            if len(r)==m:
                p.append(r)
                r=[]
            if i==0:
                r.append(suffix[i+1])
            elif i==l-1:
                r.append(prefix[i-1])
            else:
                r.append((prefix[i-1]*suffix[i+1])%12345)
        p.append(r)        
        return p                

