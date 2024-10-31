class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        new_node = Node(data)
        if (self.root == None):
            self.root = new_node
            return
        current_node = self.root
        while (True):
            if(new_node.data < current_node.data):
                if(current_node.left == None):
                    current_node.left = new_node
                    break
                current_node = current_node.left
            elif(new_node.data > current_node.data):
                if(current_node.right == None):
                    current_node.right = new_node
                    break
                current_node = current_node.right
                        
                
# breadth first search(queue)
    def breadthfirstsearch(self):
        if(self.root == None):
            return []

        queue = [self.root]
        result = []

        while(len(queue) > 0):
            current_node = queue.pop(0)
            result.append(current_node.data)

            if(current_node.left != None):
                queue.append(current_node.left)
            if(current_node.right != None):
                queue.append(current_node.right)

        return result

 
    def depthfirstsearch(self):
        current_node = self.root
        stack = []
        result = []
        while True:
            if(current_node!= None):
                stack.append(current_node)
                current_node = current_node.left
            elif(len(stack)>0):
                current_node = stack.pop()
                result.append(current_node.data)
                current_node = current_node.right
            else:
                break
        return result
        
    def insertbinary(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        queue = [self.root]
        
        while queue:
            current_node = queue.pop(0)
            
            # Insert in left child if available
            if current_node.left is None:
                current_node.left = new_node
                return
            else:
                queue.append(current_node.left)
            
            # Insert in right child if available
            if current_node.right is None:
                current_node.right = new_node
                return
            else:
                queue.append(current_node.right)
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(7)
bst.insert(12)
bst.insert(18)

# BFS (Level Order Traversal)
print("BFS:", bst.breadthfirstsearch())  # Output: [10, 5, 15, 3, 7, 12, 18]

# DFS Inorder Traversal
print("DFS Inorder:", bst.depthfirstsearch())  # Output: [3, 5, 7, 10, 12, 15, 18]
        