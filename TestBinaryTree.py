#  File: TestBinaryTree.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


import sys


class Node (object):
    # constructor
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None

    def print_node(self, level=0):

        if self.lChild != None:
            self.lChild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rChild != None:
            self.rChild.print_node(level + 1)

    def get_height(self):
        if self.lChild != None and self.rChild != None:
            return 1 + max(self.lChild.get_height(), self.rChild.get_height())
        elif self.lChild != None:
            return 1 + self.lChild.get_height()
        elif self.rChild != None:
            return 1 + self.rChild.get_height()
        else:
            return 1


class Tree(object):
    # constructor
    def __init__(self):
        self.root = None
        #allows easy access to max and min instead of using iteration
        self.max = None
        self.min = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            #sets up initial max and min values in tree
            self.min=data
            self.max=data
            return
        else:
            parent = self.root
            curr = self.root
            # finds location to insert new node
            while curr != None:
                parent = curr
                if data < curr.data:
                    curr = curr.lChild
                else:
                    curr = curr.rChild
            # inserts new node based on comparision to parent node
            if data < parent.data:
                parent.lChild = new_node
            else:
                parent.rChild = new_node
            #checks for max and min values in tree    
            if data>self.max:
                self.max=data
            if data<self.min:
                self.min=data
                
            return

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
        if self.root==None:
            return None
        elif (self.root.lChild==None) and (self.root.rChild==None):
            return 0
        else:
            return self.max-self.min

        
    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        result=[]
        #left=self.root
        #right=self.root
        parent=self.root
        #counter=0
        
        if level==0:
            result.append(self.root.data)
            return result
        if level==1:
            if self.root.lChild==None:
                pass
            else:
                result.append(self.root.lChild.data)
            if self.root.rChild==None:
                pass
            else:
                result.append(self.root.rChild.data)
            return result
       #rest of cases         
        #for i in range(level):
            #result=self.helper1(parent,result,level)
            
        return self.helper1(parent,result,level)
            
        
    def helper1(self,parent,result,level):
        if parent==None:
            return
        elif level==0:
            result.append(parent.data)
        else:
            self.helper1(parent.lChild,result,level-1)
            self.helper1(parent.rChild,result,level-1)
        
        return result


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
        nodes = []
        for i in range(self.get_height()):
            level_nodes = self.get_level(i)
            nodes.append(level_nodes[0])
        return nodes

    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        leaf_sum = 0
        
        """
        for i in range(self.get_height()):
            level_nodes = self.get_level(i)
            for node in level_nodes:
                if node.lChild == None and node.rChild == None:
                    leaf_sum += node.data
        """
        leaves = self.find_leaves(self.root)
        for leaf in leaves:
            leaf_sum += leaf.data
        return leaf_sum

    def find_leaves(self, root):
        leaves = []
        if root == None:
            return None
        if root.lChild == None and root.rChild == None:
            return [root]
        
        left_leaves = self.find_leaves(root.lChild)
        right_leaves = self.find_leaves(root.rChild)
        
        if left_leaves != None:
            leaves += left_leaves
        if right_leaves != None:
            leaves += right_leaves
        
        return leaves  


def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
    tree1_input = [] 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    
    print(t1.get_level(0))
    print(t1.get_level(2))
    print(t1.get_level(5))
    print("##########################")



if __name__ == "__main__":
    main()




