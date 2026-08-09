class Solution:
    def twoEditWords(self, queries: List[str], di: List[str]) -> List[str]:
        ans=[]
        for i in queries:
            for j in di:
                c=0
                for k,l in zip(i,j):
                    if k!=l:
                        c+=1
                        if c>2:
                            continue
                if c<=2:
                    print(i,j)
                    ans.append(i)
                    break               
        return ans            