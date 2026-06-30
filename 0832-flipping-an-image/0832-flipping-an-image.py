class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(len(image)):
            j=(image[i])[::-1]
            k=[]
            for i in j:
                if i==0:
                    k.append(1)
                else:
                    k.append(0)    
            ans.append(k)
        return ans    
            