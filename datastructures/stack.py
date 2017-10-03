class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        try:
            item = self.stack[-1]
            self.stack = self.stack[:-1]
            return item
        except IndexError as e:
            print 'Stack is Empty :)'
