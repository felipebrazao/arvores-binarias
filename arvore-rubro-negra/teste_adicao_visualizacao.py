import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rubro_negra import RedBlackTree

def plot_rbt(tree):
    if tree.root == tree.NULL:
        print("Árvore vazia!")
        return
    
    # Calcular posições dos nós
    positions = {}
    levels = {}
    
    def calculate_positions(node, x, y, x_offset):
        if node == tree.NULL:
            return x
        
        positions[node.key] = (x, y)
        levels[y] = levels.get(y, 0) + 1
        
        # Calcular posição do filho esquerdo
        left_x = calculate_positions(node.left, x - x_offset, y - 1, x_offset / 2)
        
        # Calcular posição do filho direito
        right_x = calculate_positions(node.right, x + x_offset, y - 1, x_offset / 2)
        
        return x
    
    # Calcular altura da árvore
    def get_height(node):
        if node == tree.NULL:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    height = get_height(tree.root)
    calculate_positions(tree.root, 0, height, 4)
    
    # Criar figura
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    ax.set_aspect('equal')
    
    # Desenhar arestas primeiro
    def draw_edges(node):
        if node == tree.NULL:
            return
        
        x, y = positions[node.key]
        
        if node.left != tree.NULL:
            left_x, left_y = positions[node.left.key]
            ax.plot([x, left_x], [y, left_y], 'k-', linewidth=1.5, alpha=0.7)
            draw_edges(node.left)
        
        if node.right != tree.NULL:
            right_x, right_y = positions[node.right.key]
            ax.plot([x, right_x], [y, right_y], 'k-', linewidth=1.5, alpha=0.7)
            draw_edges(node.right)
    
    # Desenhar nós
    def draw_nodes(node):
        if node == tree.NULL:
            return
        
        x, y = positions[node.key]
        
        # Cor do nó baseada na cor da árvore rubro-negra
        color = 'red' if node.color == 'RED' else 'black'
        text_color = 'white' if node.color == 'BLACK' else 'white'
        
        # Desenhar círculo
        circle = patches.Circle((x, y), 0.3, facecolor=color, edgecolor='black', linewidth=2)
        ax.add_patch(circle)
        
        # Adicionar texto
        ax.text(x, y, str(node.key), ha='center', va='center', 
                fontsize=12, fontweight='bold', color=text_color)
        
        draw_nodes(node.left)
        draw_nodes(node.right)
    
    draw_edges(tree.root)
    draw_nodes(tree.root)
    
    # Configurar eixos
    all_x = [pos[0] for pos in positions.values()]
    all_y = [pos[1] for pos in positions.values()]
    
    margin = 1
    ax.set_xlim(min(all_x) - margin, max(all_x) + margin)
    ax.set_ylim(min(all_y) - margin, max(all_y) + margin)
    
    ax.set_title('Árvore Rubro-Negra\n(Nós Vermelhos = RED, Nós Pretos = BLACK)', 
                 fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    # Adicionar legenda
    red_patch = patches.Patch(color='red', label='Nós RED')
    black_patch = patches.Patch(color='black', label='Nós BLACK')
    ax.legend(handles=[red_patch, black_patch], loc='upper right', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.show()

# Criar a árvore Rubro-Negra
rbt = RedBlackTree()
valores = [50, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35, 55, 65, 75, 85, 1, 7, 27, 37, 57, 67]  # 21 nós

print("Inserindo valores:", valores)
for v in valores:
    rbt.insert(v)

print("\nÁrvore Rubro-Negra após inserções (inorder):")
rbt.inorder(rbt.root)
print("\n")

print("Gerando visualização da árvore...")
plot_rbt(rbt)

# Buscar exemplo
print("\nTeste de busca:")
valor = 25
res = rbt.search(rbt.root, valor)
print(f"Busca por {valor}: {'Encontrado' if res != rbt.NULL else 'Não encontrado'}")

# Testes adicionais
print("\nTestes adicionais de busca:")
valores_teste = [1, 67, 100, 50]
for v in valores_teste:
    res = rbt.search(rbt.root, v)
    status = 'Encontrado' if res != rbt.NULL else 'Não encontrado'
    print(f"Busca por {v}: {status}")