class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1):
                self.stack2.append(self.stack1.pop())
        if len(self.stack2) > 0:
            return self.stack2.pop()
