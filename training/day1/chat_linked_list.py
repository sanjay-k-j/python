class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        return self.top

    def printNode(self):
         while True:
            if self.is_empty():
                break
            else:
                removed_node = self.top
                self.top = removed_node.next
                print(removed_node.value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            removed_node = self.top
            self.top = removed_node.next
            return removed_node.value

# Example usage:
stack = Stack()
# switch = int(input("Enter your choice :\n1.Insert\n2.Pop\n3.Display\n4.Exit\n"))
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print(stack.pop())  # Output: 3
# print(stack.pop())  # Output: 2
# print(stack.pop())  # Output: 1
# print(stack.pop())  # Output: None
while True:
    switch = int(input("Enter your choice :\n1.Insert\n2.Pop\n3.Display\n4.Exit\n"))
    if switch ==1 :
        value = input("Enter the value : ")
        new_node3 = stack.push(value)
        
    elif switch == 2 :
        print("The element popped out is ", stack.pop())
        
    elif switch == 3 :
        stack.printNode()
    else :
        exit()
