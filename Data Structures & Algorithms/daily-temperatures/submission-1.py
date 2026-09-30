class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stack:
                stack.append(i)
                result[i] = 0
            elif temperatures[i] > temperatures[stack[-1]]:
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    j = stack.pop()
                    result[j] = i - j
                stack.append(i)
            else:
                stack.append(i)
        return result
