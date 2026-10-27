from collections import Counter
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        alp=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        dig=['0','1','2','3','4','5','6','7','8','9']
        sudo=Counter(s)
        print(sudo)
        visi=set()
        ans=0
        for i in s:
            if not i.isdigit():
                if i not in visi:
                    j=alp[122-ord(i)]
                    if j not in sudo:
                        ans+=sudo[i]
                        visi.add(i)
                        visi.add(j)
                    elif j in sudo:
                        ans+=abs(sudo[i]-sudo[j])
                        visi.add(j)
                        visi.add(i)
            else:
                if i not in visi:
                    j=str(dig[9-int(i)])
                    if j not in sudo:
                        ans+=sudo[i]
                        visi.add(i)
                    elif j in sudo:
                        ans+=abs(sudo[i]-sudo[j])
                        visi.add(j)
                        visi.add(i)
        return ans

        