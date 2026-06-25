class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left=0
        di={}
        ans=0
        for right in range(len(fruits)):
            di[fruits[right]]=di.get(fruits[right],0)+1
            while len(di)>2:
                di[fruits[left]]-=1
                if di[fruits[left]]==0:
                    del di[fruits[left]]
                left+=1
            ans=max(ans,sum(di.values()))
        return ans          