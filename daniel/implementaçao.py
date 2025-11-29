from main import Tree234


tree = Tree234() 
nums = [10, 20, 30, 40, 50]
for n in nums:
    print(f"Inserindo {n}...")
    tree.insert(n)
    tree.print_tree()

print("Buscar o número 30 →", tree.search(tree.root, 30))
print("Buscar o número 99 →", tree.search(tree.root, 99))
