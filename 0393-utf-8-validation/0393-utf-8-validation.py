class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        count=0
        for nums in data:
            binary=format(nums,'08b')
            if count==0:
                if binary.startswith('0'):
                    count=0
                elif binary.startswith('110'):
                    count=1    
                elif binary.startswith('1110'):
                    count=2    
                elif binary.startswith('11110'):
                    count=3
                else:
                    print(1)
                    return False
            else:
                if not binary.startswith('10'):
                    return False
                count-=1
        else:
            if count==0:
                return True
            else:
                return False                            