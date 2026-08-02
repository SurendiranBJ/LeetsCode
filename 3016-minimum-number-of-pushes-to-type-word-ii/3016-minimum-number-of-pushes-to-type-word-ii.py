class Solution:
    def minimumPushes(self, word: str) -> int:
        word1=Counter(word)
        word2=dict(sorted(word1.items(),key=lambda x:x[1],reverse=True))
        sol=0
        key=1
        c=0
        for i,j in word2.items():
            sol+=(j*key)
            if (c+1)%8==0:
                key+=1  
            c+=1          
        return (sol)   