from player import Player

'''
We modified an AVLTree class we found on Github to adapt with
our main function and our Player class
Source: https://gist.github.com/girish3/a8e3931154af4da89995
'''

class AVLTree():
    def __init__(self):
        self.node = None
        self.height = -1
        self.balance = 0
   
    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def insert(self, player):
        
        if self.node == None:
            self.node = player
            self.node.right = AVLTree()
            self.node.left = AVLTree()

        elif player.score < self.node.score:
            self.node.left.insert(player)
        
        else:
            self.node.right.insert(player)
        
        self.rebalance()
 
    def rebalance(self):
        """
        Rebalance tree
        After inserting or deleting a node, 
        """
        #Key inserted, let's check if we're balanced
        self.update_heights(recursive=False)
        self.rebalance(False)
        while self.balance < -1 or self.balance > 1: 
            # if left subtree is larger than right subtree
           if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.rebalance()
                self.rrotate()
                self.update_heights()
                self.rebalance() 
            
           if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.rebalance()
                self.lrotate()
                self.update_heights()
                self.rebalance()

    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
    def update_heights(self, recursive=True):
        """
        Update tree height
        Tree height is max height of either left or right subtrees +1 for root of the tree
        """
        if self.node: 
            if recursive: 
                if self.node.left: 
                    self.node.left.update_heights()
                if self.node.right:
                    self.node.right.update_heights()
            
            self.height = 1 + max(self.node.left.height, self.node.right.height)
        else: 
            self.height = -1

    def rebalance(self, recursive=True):
        """
        Calculate tree balance factor
        The balance factor is calculated as follows: 
        balance = height(left subtree) - height(right subtree). 
        """
        if self.node:
            if recursive:
                if self.node.left:
                    self.node.left.rebalance()
                if self.node.right:
                    self.node.right.rebalance()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0
  
    def delete(self, player):
        if self.node != None:
            if self.node.name == player.name:
                if not self.node.left.node and not self.node.right.node:
                    self.node = None
                elif not self.node.left.node:                
                    self.node = self.node.right.node
                elif not self.node.right.node:
                    self.node = self.node.left.node
                else:
                    replacement = self.node.right.node  
                    while replacement and replacement.left.node:
                        replacement = replacement.left.node

                    if replacement:
                        self.node = replacement
                        self.node.right.delete(replacement)

            elif player.score <= self.node.score:
                self.node.left.delete(player)

            elif player.score > self.node.score:
                self.node.right.delete(player)

            # Rebalance tree
            self.rebalance()


    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def get_min(self):
        current = self.node
        while current.left.node is not None:
            current = current.left.node
        return current
    
    def get_max(self):
        current = self.node
        while current.right.node is not None:
            current = current.right.node
        return current
