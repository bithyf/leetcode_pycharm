class MaxQueue(object):

    def __init__(self):
        self.f_stack = []
        self.b_stack = []

    def max_value(self):
        """
        :rtype: int
        """
        if len(self.f_stack) != 0 and len(self.b_stack) != 0:
            return max(self.f_stack[-1][1], self.b_stack[-1][1])
        elif len(self.f_stack) != 0:
            return self.f_stack[-1][1]
        elif len(self.b_stack) != 0:
            return self.b_stack[-1][1]
        return -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        if len(self.f_stack) == 0:
            self.f_stack.append([value, value])
        else:
            self.f_stack.append([value, max(value, self.f_stack[-1][1])])

    def pop_front(self):
        """
        :rtype: int
        """
        if len(self.b_stack) > 0:
            return self.b_stack.pop()[0]
        if len(self.f_stack) > 0:
            num = self.f_stack.pop()
            self.b_stack.append([num[0], num[0]])
            while len(self.f_stack) > 0:
                num = self.f_stack.pop()
                self.b_stack.append([num[0], max(num[0], self.b_stack[-1][1])])
            return self.b_stack.pop()[0]
        return [-1]
