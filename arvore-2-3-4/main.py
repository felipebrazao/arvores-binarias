class Node234:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_leaf(self):
        return len(self.children) == 0

    def is_full(self):
        return len(self.keys) == 3


class Tree234:
    def __init__(self):
        self.root = Node234()

    # -------------------------
    # Split de nó 4 (3 chaves)
    # -------------------------
    def split_child(self, parent, index):
        node = parent.children[index]

        # O nó cheio tem: [A, B, C]
        A, B, C = node.keys

        # Novo nó direito
        right = Node234(keys=[C], children=node.children[2:])

        # Nó esquerdo permanece com A
        left = Node234(keys=[A], children=node.children[:2])

        # Inserir chave B no pai
        parent.keys.insert(index, B)

        # Substituir o filho por left e inserir right
        parent.children[index] = left
        parent.children.insert(index + 1, right)

    # -------------------------
    # Inserção principal
    # -------------------------
    def insert(self, key):
        root = self.root

        # Se a raiz está cheia, precisa split antes de descer
        if root.is_full():
            new_root = Node234(children=[root])
            self.split_child(new_root, 0)
            self.root = new_root

        self._insert_non_full(self.root, key)

    # Inserção em nó não cheio
    def _insert_non_full(self, node, key):

        # Caso 1: nó folha
        if node.is_leaf():
            node.keys.append(key)
            node.keys.sort()
            return

        # Caso 2: nó interno
        # Escolher filho adequado
        for i in range(len(node.keys)):
            if key < node.keys[i]:
                child_index = i
                break
        else:
            child_index = len(node.keys)

        # Se o filho está cheio, split antes de descer
        if node.children[child_index].is_full():
            self.split_child(node, child_index)

            # Após split, decidir qual dos dois filhos seguir
            if key > node.keys[child_index]:
                child_index += 1

        self._insert_non_full(node.children[child_index], key)

    # -------------------------
    # Busca
    # -------------------------
    def search(self, node, key):
        if node is None:
            return False

        # Verifica chaves no nó atual
        for i, k in enumerate(node.keys):
            if key == k:
                return True
            if key < k:
                return self.search(node.children[i], key)

        return self.search(node.children[-1] if node.children else None, key)

    # -------------------------
    # Impressão da árvore (nivel por nivel)
    # -------------------------
    def print_tree(self):
        from collections import deque
        queue = deque([(self.root, 0)])
        current_level = 0

        print("\nÁrvore 2-3-4 (níveis):")
        while queue:
            node, level = queue.popleft()

            if level != current_level:
                print()
                current_level = level

            print(f"{node.keys}", end=" ")

            for child in node.children:
                queue.append((child, level + 1))
        print("\n")
