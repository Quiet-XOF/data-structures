class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:    
    def __init__(self):
        self.head = None

    # Helpers
    def errorHandle(self, key):
        ERROR_MSG = {
            "empty": "LinkedList is empty.",
            "index": "Index out of bounds.",
            "node": "Node does not exist in LinkedList."
        }
        print(f"Error: {ERROR_MSG[key]}")

    # Print Methods
    def printList(self):
        if not self.head:
            return self.errorHandle("empty")
            
        current = self.head
        chart = f"{current.data}"
        while current.next:
            chart += f" -> {current.next.data}"
            current = current.next
        print(chart)

    # Insertion Methods
    def insertHead(self, data):
        dummy = Node(data)
        if not self.head:
            self.head = dummy
            return
        else:
            dummy.next = self.head
            self.head = dummy

    def insertTail(self, data):
        dummy = Node(data)
        if not self.head:
            self.head = dummy
            return
        current = self.head
        while current.next: 
            current = current.next
        current.next = dummy

    def insertIndex(self, data, index):
        dummy = Node(data)
        current = self.head
        position = 0
        if index < 0:
            return self.errorHandle("index")
        elif position == index: 
            self.insertHead(data)
        else:
            while current and position + 1 != index:
                position += 1
                current = current.next
            if current:
                dummy.next = current.next
                current.next = dummy
            else: 
                return self.errorHandle("index")

    # Removing Methods
    def removeHead(self):
        if not self.head:
            return
        self.head = self.head.next

    def removeTail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        current = self.head
        while current.next.next: 
            current = current.next
        current.next = None

    def removeList(self):
        self.head = None

    def removeIndex(self, index):
        if not self.head:
            return
        current = self.head
        position = 0
        if position == index: 
            self.removeHead()
        else:
            while(current and position + 1 != index):
                position += 1
                current = current.next
            if current: 
                current.next = current.next.next
            else: 
                return self.errorHandle("index")

    def removeNode(self, data):
        current = self.head
        if current.data == data:
            self.removeHead()
            return
        while current.next and current.next.data != data:
            current = current.next
        if not current: 
            return
        else: 
            return self.errorHandle("node")

    # Changing Methods
    def updateNode(self, data, index):
        if not self.head:
            return self.errorHandle("empty")
        current = self.head
        position = 0
        if position == index: current.data = data
        else:
            while current and position != index:
                position += 1
                current = current.next
            if current: 
                current.data = data
            else: 
                return self.errorHandle("index")

    def reverseList(self):
        if not self.head:
            return self.errorHandle("empty")
        current = self.head
        forward = None
        previous = None
        while current:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
        self.head = previous

    # TODO sort list, merge lists

    # Searching Methods
    def getLength(self):
        length = 0
        if self.head:
            current = self.head
            while current:
                length += 1
                current = current.next
        return length

    def getIndex(self, data):
        if not self.head:
            return self.errorHandle("empty")
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return self.errorHandle("node")

def main():
    # LinkedList samples
    myList = LinkedList()
    myList.printList()

    for i in range(0, 10): 
        myList.insertTail(i + 1)
        
    myList.printList()
    myList.reverseList()
    myList.printList()

if __name__ == '__main__': main()    