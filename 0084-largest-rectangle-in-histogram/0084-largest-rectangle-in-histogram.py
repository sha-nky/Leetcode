class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                maxArea = max(maxArea, h * width)
            stack.append(i)

        heights.pop()
        return maxArea
