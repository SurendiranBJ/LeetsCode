class Solution(object):
    def maxArea(self, height):
        mini = 0
        i = 0
        j = len(height) - 1

        while i < j:
            mi = min(height[i], height[j])
            length = j - i
            area = mi * length

            if area > mini:
                mini = area

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return mini