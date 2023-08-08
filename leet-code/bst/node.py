class Node:
    """Node class for Binary Search Tree"""
    def __init__(self, key: int) -> None:
        """Node class for Binary Search Tree"""
        self.left = None
        self.right = None
        self.val = key


def insert(root : Node, key : int):
    """Insert a node into the BST"""
    if root is None:
        # Create a new node and return it
        print("Root is None")
        return Node(key)
    else:
        if root.val == key:
            # Do nothing, key already exists (bst can not assgine duplicate keys)
            print("Duplicate")
            return root
        elif root.val > key:
            # Left subtree
            print("Left subtree")
            root.left = insert(root.left, key)
        else:
            # Right subtree
            print("Right subtree")
            root.right = insert(root.right, key)
    return root

def search(root, key):
    """Search for a key in BST"""
    # Root is None and Node's value is key
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)


def min_value_node(node):
    """Find the minimum value node in BST"""
    current = node
    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left
    return current

def delete(root, key):
    """Delete a key from BST"""
    if root is None:
        return root
    # Find the node to be deleted
    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    # Find the node. Now delete it
    else:
        # Node with only one child or no child -> delete the node and return the child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # If the node has two children, e.g) 10(left) - 15(root) - 20(right)
        # root is deleted and right children will be root.
        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)
    return root

def inorder(root):
    """Inorder traversal of BST"""
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
        
def preorder(root):
    """Preorder traversal of BST"""
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    """Postorder traversal of BST"""
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
        

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print("inorder", inorder(r))
print("post order : ", postorder(r))
temp = search(r, 20)
print(temp.val)
temp2 = search(r, 11)
print(temp2)

print("\nDelete 20")
r = delete(r, 20)
print("Inorder traversal of the modified tree")
inorder(r)
 
print("\nDelete 30")
r = delete(r, 30)
print("Inorder traversal of the modified tree")
inorder(r)
 
print("\nDelete 50")
r = delete(r, 50)
print("Inorder traversal of the modified tree")
inorder(r)