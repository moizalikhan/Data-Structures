# Singly Linked list--------------------------------------------------------------------------------------------------------------------
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        array = []
        currentNode = self.head
        while currentNode is not None:
            array.append(currentNode.data)
            currentNode = currentNode.next
        return array

    def insertatend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
    
    def insertatstart(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node    
    
    
    def delete(self, data):
		    if self.head == None:
			    return
		    if self.head.data == data:
			    self.head = self.head.next
			    return
		    temp = self.head
		    while temp != None:
			    if temp.next.data == data:
				    temp.next = temp.next.next
				    return
			    temp = temp.next        
    
    def deletefromStart(self):
        self.head = self.head.next
        return
    
    def deletefromEnd(self):
        temp = self.head
        while(temp.next.next !=None):
            temp = temp.next
        temp.next = None
        return
    
    def deletefromParticular(self,index):
        temp = self.head
        counter = 1
        while(counter < index-1):
            temp = temp.next
            counter +=1
        temp.next = temp.next.next
    
    
    def insertatparticular(self, data, index):
        new_node = Node(data)    
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        counter = 2
        print(f"counter value before{counter}")
        while counter < index:
            temp = temp.next
            counter += 1
            print(f"counter value after{counter}")
        new_node.next = temp.next
        temp.next = new_node
# two pointers
    def reversal(self):
        temp = self.head
        prev = None
        while(temp!=None):
            link = temp.next
            temp.next = prev
            prev = temp
            temp = link
        self.head = prev
        return self.head
    
    def removeduplicates(self):
        if(self.head == None):
            return
        temp = self.head
        setfor = set()
        setfor.add(temp.data)
        while(temp != None and temp.next!=None):
            if(temp.data == temp.next.data):
                temp.next = temp.next.next
            else:
                setfor.add(temp.next.data)
                temp = temp.next
        return setfor
                
# Doubly linked lists ------------------------------------------------------------------------------------------------------
class nodeforDoublyLinkedlist:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
# class doublyLinkedlist:
    def __init__(self):
        self.head = None
    
    def display(self):
        array = []
        currentNode = self.head
        while currentNode != None:
            array.append(currentNode.data)
            currentNode = currentNode.next
        return array
    
    def insertatend(self, data):
        new_node = nodeforDoublyLinkedlist(data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        while(temp.next!= None):
            temp = temp.next
        new_node.prev= temp
        temp.next = new_node
        new_node.next = None
        return
    
    def insertatstart(self, data):
        new_node = nodeforDoublyLinkedlist(data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        new_node.next = temp
        new_node.prev = None
        temp.prev = new_node
        self.head = new_node
        return

    def insertatparticular(self, data, index):
        new_node = nodeforDoublyLinkedlist(data)
        if (self.head == None):
            self.head = new_node
            return
        temp = self.head
        counter = 1
        while(counter < index):
            temp = temp.next
            counter +=1
        new_node.next = temp.next
        new_node.prev = temp
        temp.next = new_node
        temp.next.prev= new_node.next
        return

    def deletefordata(self, data):
        temp = self.head
        while(temp!= None):
            if(temp.data == data):
                if(temp.next == None):
                    temp.prev.next = temp.next
                    return
                elif(temp.prev == None):
                    self.head = temp.next
                    self.head.prev = None
                    return
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return
            temp = temp.next
        return
    
    def deletefromStart(self):
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        return
    
    def deletefromEnd(self):
        temp = self.head
        while(temp.next !=None):
            temp = temp.next
        temp.prev.next = None
        return
    
    def deletefromParticular(self,index):
        temp = self.head
        counter = 0
        while(temp!= None):
                if(counter == index):
                    if(temp.prev!=None):
                        temp.prev.next = temp.next
                    if(temp.next!=None):
                        temp.next.prev = temp.prev
                    if (temp.prev == None):
                        self.head == temp.prev
                    if (temp.next == None):
                        temp.next = None
                temp = temp.next
                counter +=1
        return
    def reversal(self):        
        return
#-----------------------------------------------------------------------------------------
# circular linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class circularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def display(self):
        array = []
        if self.head is None:
            return array

        currentNode = self.head
        while True:
            array.append(currentNode.data)
            currentNode = currentNode.next
            if currentNode == self.head:
                break
        return array
    
    def insertatend(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return
        
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = self.head

# ------------------------------------------------------------------------------
# cycle detection
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListWithCycle:
    def __init__(self):
        self.head = None

    # Insert nodes at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    # Method to create a cycle in the list
    def create_cycle(self, pos):
        if pos < 0:
            return

        cycle_node = None
        temp = self.head
        index = 0

        while temp.next is not None:
            if index == pos:
                cycle_node = temp
            temp = temp.next
            index += 1
        
        if cycle_node:
            temp.next = cycle_node  # Creating a cycle by linking the last node to the node at 'pos'

    # Method to detect if there is a cycle in the list (Floyd's Cycle Detection Algorithm)
    def detect_cycle(self):
        slow_pointer = self.head
        fast_pointer = self.head.next
        
        while(fast_pointer!= None and fast_pointer.next!= None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if(slow_pointer == fast_pointer):
                return True
        return False

    # Method to display the list (will only print up to 10 elements to avoid infinite loop in case of a cycle)
    def display(self):
        temp = self.head
        count = 0
        result = []
        while temp is not None and count < 10:
            result.append(temp.data)
            temp = temp.next
            count += 1

        return result

#----------------------------------------------------------------------------------------------------- 
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertatend(1)
    ll.insertatend(2)
    ll.insertatend(3)
    ll.insertatend(2)
    ll.insertatend(2)
    ll.insertatend(2)
    ll.insertatend(4)
    ll.insertatend(5)
    ll.insertatend(6)
    ll.insertatend(7)
    ll.insertatend(8)
    print(ll.display())
    ll.removeduplicates()
    print(ll.display())
    ll.deletefromStart()
    print(ll.display())
    ll.deletefromEnd()
    print(ll.display())
    ll.deletefromParticular(3)
    print(ll.display())
    print(ll.insertatparticular(5,4))
    print(ll.display())
    ll2 = LinkedList()
    ll2.insertatstart(1)
    ll2.insertatstart(2)
    ll2.insertatstart(3)
    ll2.delete(1)
    print(ll2.display())
    ll.reversal()
    print(ll.display())
# ---------------------------------------------------------------------
    lld = doublyLinkedlist()
    lld.insertatstart(3)
    lld.insertatstart(4)
    lld.insertatstart(5)
    lld.insertatstart(6)
    lld.insertatstart(7)
    print(lld.display())
    lld.insertatend(8)
    print(lld.display())
    lld.insertatparticular(3,2)
    lld.deletefromStart()
    print(lld.display())
    lld.deletefromEnd()
    lld.deletefordata(7)
    print(lld.display())
    lld.deletefromParticular(4)
    print(lld.display())
    lld.reversal()
    print(lld.display())
# -----------------------------------------------------------------------
    cll = circularLinkedList()
    cll.insertatend(1)
    cll.insertatend(2)
    cll.insertatend(3)
    cll.insertatend(4)
    cll.insertatend(5)
    cll.insertatend(6)
    cll.insertatend(7)
    print(cll.display())
# ------------------------------------------------------------------------