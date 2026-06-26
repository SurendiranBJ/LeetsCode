class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        if len(blocks)<k:
            return 0
        b='B'*k
        if b in blocks:
            return 0
        ans=0
        op=0
        for i in range(k):
            if blocks[i]=='W':
                op+=1
        ans=op
        for i in range(k,len(blocks)):
            if  blocks[i-k]=='W':
                op-=1
            if blocks[i]=='W':
                op+=1
            ans=min(op,ans) 
        return ans                      