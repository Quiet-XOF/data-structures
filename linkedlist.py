class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:    
    def __init__(self):
        self.head = None
        self.length = 0

    # Print Methods
    def printList(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        chart = []
        while current:
            chart.append(str(current.data))
            current = current.next
        print(" -> ".join(chart))

    # TODO toList(self):

    # TODO copyList(self):

    def countOccurrences(self, value):
        if not self.head:
            return
        current = self.head
        count = 0
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    # TODO isPalindrome(self):

    # Insertion Methods
    def insertHead(self, data):
        dummy = Node(data)
        if not self.head:
            self.head = dummy
        else:
            dummy.next = self.head
            self.head = dummy
        self.length += 1

    def insertTail(self, data):
        dummy = Node(data)
        if not self.head:
            self.head = dummy
        else:
            current = self.head
            while current.next: 
                current = current.next
            current.next = dummy
        self.length += 1

    def insertIndex(self, data, index):
        if index < 0 or index > self.length:
            print(f"Index {index} out of bounds.")
            return
        dummy = Node(data)
        current = self.head
        position = 0
        
        if position == index: 
            self.insertHead(data)
        else:
            while current and position + 1 != index:
                position += 1
                current = current.next
                
            if current:
                dummy.next = current.next
                current.next = dummy
        self.length += 1
            
    def insertListHead(self, data):
        for item in data:
            self.insertHead(item)
            self.length += 1
            
    def insertListTail(self, data):
        for item in data:
            self.insertTail(item)
            self.length += 1

    # Removing Methods
    def removeHead(self):
        if not self.head:
            return
        self.head = self.head.next
        self.length -= 1

    def removeTail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            current = self.head
            while current.next.next: 
                current = current.next
            current.next = None
        self.length -= 1

    def removeIndex(self, index):
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
        self.length -= 1

    def removeNode(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.removeHead()
            self.length -= 1
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
            self.length -= 1

    def removeDuplicates(self):
        current = self.head
        seen = set([current.data])
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
                self.length -= 1
            else:
                seen.add(current.next.data)
                current = current.next

    # TODO removeAll(self, value):

    def clearList(self):
        self.head = None
        self.length = 0    

    # Changing Methods
    def updateNode(self, data, index):
        current = self.head
        position = 0
        if position == index: 
            current.data = data
        else:
            while current and position != index:
                position += 1
                current = current.next
            if current: 
                current.data = data

    def reverseList(self):
        current = self.head
        forward = None
        previous = None
        while current:
            forward = current.next
            current.next = previous
            previous = current
            current = forward
        self.head = previous

    # TODO splitList(self):

    # Sort Methods
    def bubbleSort(self):
        if not self.head or not self.head.next:
            return
        swapped = True
        while swapped:
            swapped = False
            previous = None
            current = self.head
            while current and current.next:
                if current.data > current.next.data:
                    swapped = True
                    temp = current.next
                    current.next = temp.next
                    temp.next = current
                    if previous:
                        previous.next = temp
                    else:
                        self.head = temp
                    previous = temp
                else:
                    previous = current
                    current = current.next

    def insertionSort(self):
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_current = sorted_head
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            current = next_node
        self.head = sorted_head

    def mergeSort(self): 
        if not self.head or not self.head.next:
            return self.head
        
        def mergeHelper(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            mid = slow.next
            slow.next = None

            left = mergeHelper(head)
            right = mergeHelper(mid)

            dummy = Node(0)
            tail = dummy

            while left and right:
                if left.data <= right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next

            tail.next = left if left else right
            return dummy.next
        self.head = mergeHelper(self.head)

    # TODO quick sort

    # Searching Methods

    # TODO findMiddle(self):

    def getIndex(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1   

if __name__ == '__main__': 
    try:
        myList = LinkedList()
        myList.printList()

        myList.insertListHead([5, 7, 9])
        myList.printList()
        
        for i in range(0, 10): 
            myList.insertTail(i + 1)

        myList.insertIndex(99, 2)
        myList.printList()
        print(myList.countOccurrences(9))

        myList.bubbleSort()
        myList.printList()

    except Exception as e:
        print(e)