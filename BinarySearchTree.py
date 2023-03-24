from Node import Node

class BinarySearchTree:
    # Assigns root with null (None).
    def __init__(self):
        # initialize the BST with a null root (empty).
        self.root = None
        
    # Checks to see if the BST is empty
    def isEmpty(self):
        # if the root is null, then the BST is empty
        return self.root is None
    
    def __lt__(self, other):
        return self.Node(data) < other.Node(data)
      
    # Inserts a new item into the binary search tree.
    def insert(self, data):
        # create a new node using the data
        newNode = Node(data)
        
        # is this a new tree?
        if self.isEmpty() == True:
            self.root = newNode
        else:
            # start at the top (root)
            current = self.root
            found = False     # did you find a position for the new node?
            
            # find an empty (null/None) position for the new node (where does it go?)
            while found == False:
                if newNode.data < current.data:
                    if current.left is None:
                        current.left = newNode
                        found = True      # flip flag since position found!
                    else:
                        current = current.left    # go down left branch
                else:
                    if current.right is None:
                        current.right = newNode
                        found = True      # flip flag since position found!
                    else:
                        current = current.right   # go down right branch
        
    # Removes an item with matching key from the BST.
    def remove(self, data):
        
        found = False
        
        # if the BST is empty, then nothing to remove
        if self.isEmpty() == True:
            return       # end the method
        
        # create a current reference and a parent reference
        current = self.root
        parent = None
        
        # keep searching until you find the data or run out of nodes
        while current is not None:
            if current.data == data:
                found = True
                break        # break out of the search loop
            else:
                parent = current
                if current.data < data:
                    current = current.right   # go down right branch
                else:
                    current = current.left    # go down left branch
                    
        # return if the data is not found
        if found == False:
            return        # end the method
        
        # data was found if we make it this far so w have 3 possible cases:
        # 1. We're removing a single leaf node
        # 2. We're removing a node with a single child
        # 3. We're removing a node with 2 children
        
        # 1. node that is a single leaf
        if current.left is None and current.right is None:
            if parent is None:    # node is root with no child nodes
                self.root = None
            elif parent.left is current:
                parent.left = None
            else:
                parent.right = None
                
            return     # end the method since node was deleted
        
        # 2. node with a single child
        if (current.left is None and current.right is not None) or (current.left is not None and current.right is None):
            if current.left is None and current.right is not None:  # right child present and no left child
                if parent is None:   # node is root
                    self.root = current.right
                elif parent.left is current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            else: # left child present and no right child
                if parent is None:   # node is root
                    self.root = current.left
                elif parent.left is current:
                    parent.left = current.left
                else:
                    parent.right = current.left
                    
            return    # end the method since node was deleted
        
        # 3. Node with 2 children - replace node with smallest value in right subtree
        if current.left is not None and current.right is not None:
            if parent is None:  # node is root
                temp = current.left
                self.root = current.right
                current = self.root
                while current.left is not None:
                    current = current.left
                current.left = temp
            elif parent.right is current:
                temp = current.left
                parent.right = current.right
                current = parent.right
                while current.left is not None:
                    current = current.left
                current.left = temp
            else:
                temp = current.left
                parent.left = current.right
                current = parent.left
                while current.left is not None:
                    current = current.left
                current.left = temp

                    
            return   # end the method since node was deleted
        
    # Removes an item with the smallest value from the BST.
    def remove_minimum(self):
        
        # if the BST is empty, then nothing to find
        if self.isEmpty() == True:
            return None   # end the method and return nothing (None)
        
        # create a current reference and a parent reference
        current = self.root
        parent = None
        
        # keep going down the left side until you run out of nodes
        while current.left is not None:
            parent = current
            current = current.left    # go down left branch
        
        # smallest was found if we make it this far so w have 3 possible cases:
        # 1. We're removing a single leaf node
        # 2. We're removing a node with a single child
        # 3. We cannot have two children since this is the minimum value
        
        # create reference for our minimum data
        min_data = None
        
        # 1. node that is a single leaf
        if current.left is None and current.right is None:
            if parent is None:    # node is root with no child nodes
                min_data = self.root.data
                self.root = None
            elif parent.left is current:
                min_data = current.data
                parent.left = None
            else:
                min_data = current.data
                parent.right = None
                
            return min_data    # return data and end the method since node was deleted
        
        # 2. node with a single child
        if (current.left is None and current.right is not None) or (current.left is not None and current.right is None):
            if current.left is None and current.right is not None:  # right child present and no left child
                if parent is None:   # node is root
                    min_data = current.data
                    self.root = current.right
                elif parent.left is current:
                    min_data = current.data
                    parent.left = current.right
                else:
                    min_data = current.data
                    parent.right = current.right
            # else: cannot have left child since this is the min value
                    
            return min_data    # return data and end the method since node was deleted
        
        # something went wrong if we made it this far
        return None

    # Removes an item with the largest value from the BST.
    def remove_maximum(self):
        
        # if the BST is empty, then nothing to find
        if self.isEmpty() == True:
            return None   # end the method and return nothing (None)
        
        # create a current reference and a parent reference
        current = self.root
        parent = None
        
        # keep going down the right side until run out of nodes
        while current.right is not None:
            parent = current
            current = current.right    # go down right branch
        
        # largest was found if we make it this far so w have 3 possible cases:
        # 1. We're removing a single leaf node
        # 2. We're removing a node with a single child
        # 3. We cannot have two children since this is the maximum value
        
        # create reference for our maximum data
        max_data = None
        
        # 1. node that is a single leaf
        if current.left is None and current.right is None:
            if parent is None:    # node is root with no child nodes
                max_data = self.root.data
                self.root = None
            elif parent.left is current:
                max_data = current.data
                parent.left = None
            else:
                max_data = current.data
                parent.right = None
                
            return max_data    # return data and end the method since node was deleted
        
        # 2. node with a single child
        if (current.left is None and current.right is not None) or (current.left is not None and current.right is None):
            if current.right is None and current.left is not None:  # left child present and no right child
                if parent is None:   # node is root
                    max_data = current.data
                    self.root = current.left
                elif parent.left is current:
                    max_data = current.data
                    parent.left = current.left
                else:
                    max_data = current.data
                    parent.right = current.left
            # else: cannot have right child since this is the max value
                    
            return max_data    # return data and end the method since node was deleted
        
        # something went wrong if we made it this far
        return None         
         
    # Searches for an item with matching data in the binary search tree.
    # Returns the item if found, or None if not found.
    def search(self, data):
        # is this a new tree?
        if self.isEmpty() is True:
            return None
        else:
            # start at the top (root)
            current = self.root
            
            # search for data remembering that left is smaller and right is larger
            while current is not None:
                if current.data == data:
                    return current.data
                elif data > current.data:
                    current = current.right   # go down right branch
                else:
                    current = current.left    # go down left branch
                    
            # if we hit a null (None) before finding the data, then the data does not exist in BST
            return None
        
    # get the minimum value in the BST
    def get_minimum(self):
        # is this a new tree?
        if self.isEmpty() == True:
            return None
        else:
            # start at the top (root)
            current = self.root 
            
            # go down the LEFT side since left is smaller
            while current.left is not None:
                current = current.left 
                
            # return the bottom, left node's data
            return current.data            
    
    # get the maximum value in the BST
    def get_maximum(self):
        # is this a new tree?
        if self.isEmpty() == True:
            return None
        else:
            # start at the top (root)
            current = self.root 
            
            # go down the RIGHT side since right is larger
            while current.right is not None:
                current = current.right 
                
            # return the bottom, right node's data
            return current.data
           
    # display the BST in order
    def displayInOrder(self):
        # start at the top
        current = self.root 
        self.displaySubtreeInOrder(current)
        print()  # drop to the next line
        
    def displaySubtreeInOrder(self, current):
        if current is None:
            return   # exit condition
        
        # traverse left subtree recursively
        self.displaySubtreeInOrder(current.left)
            
        # visit the node and print it
        print(current.data, end=" ")
            
        # traverse right subtree recursively
        self.displaySubtreeInOrder(current.right)
    
    # display the BST in pre-order
    def displayPreOrder(self):
        # start at the top
        current = self.root 
        self.displaySubtreePreOrder(current)
        print()  # drop to the next line
        
    def displaySubtreePreOrder(self, current):        
        if current is None:
            return   # exit condition
        
        # visit the node and print it
        print(current.data, end=" ")
        
        # traverse left subtree recursively
        self.displaySubtreePreOrder(current.left)
        
        # traverse right subtree recursively
        self.displaySubtreePreOrder(current.right)
    
    # display the BST in post-order
    def displayPostOrder(self):
        # start at the top
        current = self.root 
        self.displaySubtreePostOrder(current)
        print()  # drop to the next line
        
    def displaySubtreePostOrder(self, current):        
        if current is None:
            return   # exit condition
        
        # traverse left subtree recursively
        self.displaySubtreePostOrder(current.left)
        
        # traverse right subtree recursively
        self.displaySubtreePostOrder(current.right)
        
        # visit the node and print it
        print(current.data, end=" ")
    
    # delete all items in the BST
    def clear(self):
        # Python has a garbage collector so you can simply
        # kill the root reference to clear the tree
        self.root = None 

    # Overloaded string conversion method to create a string
    # representation of the entire binary search tree.
    # reference: Demailly, L. & Davies, T. (2011, February 11). How to print binary tree diagram? Stack Overflow. https://stackoverflow.com/questions/4965335/how-to-print-binary-tree-diagram
    def __str__(self):
        # is the tree empty?
        if self.root is None:
            return "<None>";
        
        # create an output string
        output = ""
        spaces = "         "
        
        # build the right side first
        if self.root.right is not None:
            output = self.printTree(self.root.right, True, spaces, output)
        
        # add the data to the output string and drop down to next line
        output += "root-->  " + str(self.root.data) + "\n"
        
        # build the left side last
        if self.root.left is not None:
            output = self.printTree(self.root.left, False, spaces, output)
        
        # return the output
        return "\n" + output
        
    def printTree(self, current, isRightSide, spaces, output):
        # build the right side first          
        if current.right is not None:
            if isRightSide == True:
                more = "         "
            else:
                more = " |       "
            output = self.printTree(current.right, True, spaces + more, output)
        
        # show the current data with slashes and dashes
        if isRightSide == True:
            output += spaces + " ┌────── "
        else:
            output += spaces + " └────── "

        output += str(current.data) + "\n"
        
        # build the left side last
        if current.left is not None:
            if isRightSide == True:
                more = " |       "
            else:
                more = "         "        
            output = self.printTree(current.left, False, spaces + more, output)
        
        # return the BST diagram
        return output
    
    
    
    
    
    
    
    
    
    
    