class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

"""
The nodes of a graph are also called vertices, and the pointers that connect them are called edges. 
In graphical representations, nodes/vertices are usually represented with circles and the edges are lines/arrows
that connect the circles 

The root node is the node at the "top" of the tree. Every node in the tree is accessible starting from the root node
If you have a node A with an edge to a node B, so A -> B, we call A the parent of node B, and node B a child of node A.
If a node has no children, it is called a leaf node. The leaf nodes are the leaves of the tree.

Lastly, perhaps the most important thing to understand: a subtree of a tree is a node and all its descendants. 
Trees are recursive - you can treat a subtree as if it was its own tree with the chosen node being the root.

The depth of a node is how far it is from the root node. The root has a depth of 0. Every child has a depth of 
parentsDepth + 1, so the root's children have a depth of 1, their children have a depth of 2, and so on.

Lastly, perhaps the most important thing to understand: a subtree of a tree is a node and all its descendants. 
Trees are recursive - you can treat a subtree as if it was its own tree with the chosen node being the root. 
"""