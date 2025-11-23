class Node:
    def __init__(self, key, color="RED"):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.NULL = Node(None, color="BLACK")
        self.root = self.NULL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.NULL:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        node = Node(key)
        node.left = self.NULL
        node.right = self.NULL
        node.parent = None

        y = None
        x = self.root

        while x != self.NULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        node.color = "RED"
        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent and k.parent.color == "RED":
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.rotate_left(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.rotate_right(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == "RED":
                    k.parent.color = "BLACK"
                    u.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rotate_right(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.rotate_left(k.parent.parent)
        self.root.color = "BLACK"

    def search(self, node, key):
        if node == self.NULL or key == node.key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        else:
            return self.search(node.right, key)
 
    def inorder(self, node):
        if node != self.NULL:
            self.inorder(node.left)
            print(f"{node.key}({node.color})", end=" ")
            self.inorder(node.right)

    def minimum(self, node):
        while node.left != self.NULL:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, key):
        z = self.search(self.root, key)
        if z == self.NULL:
            print(f"Valor {key} não encontrado na árvore")
            return False

        y = z
        y_original_color = y.color
        
        if z.left == self.NULL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
                
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == "BLACK":
            self.fix_delete(x)
            
        return True

    def fix_delete(self, x):
        while x != self.root and x.color == "BLACK":
            if x == x.parent.left:
                w = x.parent.right
                
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.rotate_left(x.parent)
                    w = x.parent.right
                
                if w.left.color == "BLACK" and w.right.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.right.color == "BLACK":
                        w.left.color = "BLACK"
                        w.color = "RED"
                        self.rotate_right(w)
                        w = x.parent.right
                    
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.right.color = "BLACK"
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                
                if w.color == "RED":
                    w.color = "BLACK"
                    x.parent.color = "RED"
                    self.rotate_right(x.parent)
                    w = x.parent.left
                
                if w.right.color == "BLACK" and w.left.color == "BLACK":
                    w.color = "RED"
                    x = x.parent
                else:
                    if w.left.color == "BLACK":
                        w.right.color = "BLACK"
                        w.color = "RED"
                        self.rotate_left(w)
                        w = x.parent.left
                    
                    w.color = x.parent.color
                    x.parent.color = "BLACK"
                    w.left.color = "BLACK"
                    self.rotate_right(x.parent)
                    x = self.root
                    
        x.color = "BLACK"