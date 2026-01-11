class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        maxArea = 0

        for row in matrix:
            for i in range(cols):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0

            maxArea = max(maxArea, self.largestRectangleArea(heights))

        return maxArea

    def largestRectangleArea(self, heights):
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
