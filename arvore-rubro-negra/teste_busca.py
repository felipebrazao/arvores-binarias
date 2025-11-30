from rubro_negra import RedBlackTree

# Criar a árvore Rubro-Negra
rbt = RedBlackTree()
valores = [50, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35]

print("Inserindo valores:", valores)
for v in valores:
    rbt.insert(v)
    print(f"Inseriu {v}")

print("\nÁrvore Rubro-Negra após inserções (inorder):")
rbt.inorder(rbt.root)
print("\n")

# Testar buscas
valores_busca = [25, 100, 50, 1]
print("Testando buscas:")
for valor in valores_busca:
    res = rbt.search(rbt.root, valor)
    status = 'Encontrado' if res != rbt.NULL else 'Não encontrado'
    print(f"Busca por {valor}: {status}")