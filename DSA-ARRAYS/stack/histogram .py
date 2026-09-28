class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maximum = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                top = stack.pop()
                height = heights[top]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                maximum = max(maximum, area)

            stack.append(i)

        # Process remaining bars
        i = len(heights)

        while stack:
            top = stack.pop()
            height = heights[top]

            if stack:
                width = i - stack[-1] - 1
            else:
                width = i

            area = height * width
            maximum = max(maximum, area)

        return maximum

heights = [2,1,5,6,2,3]
Solution =Solution()
result =Solution.largestRectangleArea(heights)


print(result)


    