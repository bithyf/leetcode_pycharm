class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        i, j = 0, 0
        while i < len(pushed) or j < len(popped):
            while len(stack) == 0 or popped[j] != stack[-1]:
                # 若栈中无匹配则返回False
                if i == len(pushed):
                    return False
                stack.append(pushed[i])
                i += 1
            del stack[-1]
            j += 1
        return True
