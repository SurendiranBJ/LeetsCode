class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        bd={}
        cd={}
        ans=[]
        for ball,color in queries:
            if ball not in bd:
                if color not in cd:
                    cd[color]=set()
                cd[color].add(ball)
                bd[ball]=color
            else:
                prev_color=bd[ball]
                cd[prev_color].discard(ball)
                if len(cd[prev_color])==0:
                    del cd[prev_color]
                bd[ball]=color
                if color not in cd:
                    cd[color]=set()
                cd[color].add(ball)
            ans.append(len(cd))
        return ans