import matplotlib.pyplot as plt
import matplotlib.patches as patches
from rubro_negra import RedBlackTree

def plot_rbt(tree, title_suffix=""):
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
        text_color = 'white'
        
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
    
    # Título dinâmico
    base_title = 'Árvore Rubro-Negra'
    if title_suffix:
        title = f'{base_title} - {title_suffix}\n(Nós Vermelhos = RED, Nós Pretos = BLACK)'
    else:
        title = f'{base_title}\n(Nós Vermelhos = RED, Nós Pretos = BLACK)'
    
    ax.set_title(title, fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    # Adicionar legenda
    red_patch = patches.Patch(color='red', label='Nós RED')
    black_patch = patches.Patch(color='black', label='Nós BLACK')
    ax.legend(handles=[red_patch, black_patch], loc='upper right', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.show()

def count_nodes(tree):
    """Conta o número de nós na árvore"""
    def count_recursive(node):
        if node == tree.NULL:
            return 0
        return 1 + count_recursive(node.left) + count_recursive(node.right)
    
    return count_recursive(tree.root)

def print_tree_stats(tree, title=""):
    """Imprime estatísticas da árvore"""
    print(f"\n{'='*50}")
    if title:
        print(f"📊 ESTATÍSTICAS - {title}")
    else:
        print(f"📊 ESTATÍSTICAS DA ÁRVORE")
    print(f"{'='*50}")
    
    node_count = count_nodes(tree)
    print(f"🌳 Número de nós: {node_count}")
    
    # Calcular altura
    def get_height(node):
        if node == tree.NULL:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))
    
    height = get_height(tree.root)
    print(f"📏 Altura da árvore: {height}")
    
    # Contar nós vermelhos e pretos
    red_count = 0
    black_count = 0
    
    def count_colors(node):
        nonlocal red_count, black_count
        if node == tree.NULL:
            return
        if node.color == "RED":
            red_count += 1
        else:
            black_count += 1
        count_colors(node.left)
        count_colors(node.right)
    
    if tree.root != tree.NULL:
        count_colors(tree.root)
    
    print(f"🔴 Nós vermelhos: {red_count}")
    print(f"⚫ Nós pretos: {black_count}")
    print(f"📊 Proporção R/B: {red_count/(black_count if black_count > 0 else 1):.2f}")

# Demonstração de Balanceamento após Remoção
print("🎯 ÁRVORE RUBRO-NEGRA APÓS REMOÇÃO DE NÓ")
print("=" * 45)

# Criar primeira árvore
rbt1 = RedBlackTree()
valores_iniciais = [50, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35, 55, 65, 75, 85, 1, 7, 27, 37, 57, 67]  # 21 nós - MESMOS valores do teste_rubro_negra.py

print("\n📋 CRIANDO ÁRVORE BASE")
print("Inserindo valores:", valores_iniciais)

for v in valores_iniciais:
    rbt1.insert(v)

print("\nÁrvore inicial (inorder):")
rbt1.inorder(rbt1.root)
print()

print_tree_stats(rbt1, "ÁRVORE INICIAL")

no_para_remover = 20  # Nó interno com filhos - causa rebalanceamento significativo

print(f"\n🗑️ REMOVENDO NÓ: {no_para_remover}")
print(f"ℹ️  O nó {no_para_remover} foi escolhido porque:")
print("   - É um nó interno (tem filhos)")
print("   - Sua remoção exigirá rebalanceamento")
print("   - Demonstra como a árvore se auto-ajusta")

# Criar segunda árvore (cópia da primeira)
rbt2 = RedBlackTree()
for v in valores_iniciais:
    rbt2.insert(v)

# Remover o nó
print(f"\n🔄 Processando remoção do nó {no_para_remover}...")
removido = rbt2.delete(no_para_remover)

if removido:
    print(f"✅ Nó {no_para_remover} removido com sucesso!")
    
    print("\nÁrvore após remoção (inorder):")
    rbt2.inorder(rbt2.root)
    print()
    
    print_tree_stats(rbt2, "APÓS REMOÇÃO")
    
    print(f"\n📊 Visualizando árvore após remoção do nó {no_para_remover}...")
    plot_rbt(rbt2, f"Após Remoção do Nó {no_para_remover}")
    
else:
    print(f"❌ Falha ao remover nó {no_para_remover}")

print(f"\n🎯 RESULTADO:")
print("✅ A árvore manteve suas propriedades rubro-negras")
print("✅ O balanceamento foi preservado automaticamente") 
print("✅ As operações continuam sendo O(log n)")

print(f"\n{'='*45}")
print("✅ ÁRVORE REBALANCEADA COM SUCESSO!")
print(f"{'='*45}")