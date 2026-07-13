class Solution(object):
    sol=[]
    ans=[12,123,1234,12345,123456,1234567,12345678,123456789]
    add=[11,111,1111,11111,111111,1111111,11111111,111111111]
    i=0
    a=ans[0]
    sol.append(a)
    while i<len(ans)-1:
        k=a+add[i]
        a=k
        if k%100==0:
            i+=1
            a=ans[i]
            sol.append(a)
        else:
            sol.append(k)   
    print(len(sol))                 
    def sequentialDigits(self, low, high):
        i=0
        mainans=[]
        while True:
            if Solution.sol[i]>=low and Solution.sol[i]<=high:
                mainans.append(Solution.sol[i])
            if Solution.sol[i]>high or i==35:
                break    
            i+=1
        return mainans    