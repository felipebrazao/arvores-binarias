import math
import random
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Estruturas Base
# ----------------------------------------------------------------------

class KDNode:
    def __init__(self, ponto, dim, esquerda=None, direita=None):
        self.ponto = ponto     
        self.dim = dim         
        self.esquerda = esquerda
        self.direita = direita

class ResultadoBusca:
    def __init__(self):
        self.melhor_distancia_sq = float('inf') 
        self.melhor_ponto = None

def distancia_quadratica(p1, p2):
    """Calcula a distância euclidiana quadrática para evitar sqrt desnecessário."""
    return sum((a - b)**2 for a, b in zip(p1, p2))

# ----------------------------------------------------------------------
# 1. Busca por Vizinho Mais Próximo (VMP) - CORRIGIDA
# ----------------------------------------------------------------------

def _buscar_vmp_recursivo(node, ponto_consulta, resultado):
    """Função auxiliar que realiza a busca VMP com PODA (pruning)."""
    if node is None:
        return

    # 1. Checar o ponto atual do nó
    dist_sq_atual = distancia_quadratica(node.ponto, ponto_consulta)
    
    if dist_sq_atual < resultado.melhor_distancia_sq:
        resultado.melhor_distancia_sq = dist_sq_atual
        resultado.melhor_ponto = node.ponto

    d = node.dim
    
    # Diferença na coordenada de corte
    diff = ponto_consulta[d] - node.ponto[d]

    # Decidir qual sub-árvore explorar primeiro
    primeiro_lado = node.esquerda if diff < 0 else node.direita
    segundo_lado = node.direita if diff < 0 else node.esquerda

    # 2. Explorar o lado mais provável
    _buscar_vmp_recursivo(primeiro_lado, ponto_consulta, resultado)

    # 3. O TESTE DE PODA (Pruning)
    dist_ate_plano_sq = diff**2

    # Verificar se é necessário explorar o outro lado (se o plano de corte 
    # estiver mais perto do que a melhor distância encontrada)
    if dist_ate_plano_sq < resultado.melhor_distancia_sq:
        _buscar_vmp_recursivo(segundo_lado, ponto_consulta, resultado)


def buscar_vizinho_mais_proximo(raiz, ponto_consulta):
    """Função wrapper para iniciar a busca VMP."""
    resultado = ResultadoBusca()
    _buscar_vmp_recursivo(raiz, ponto_consulta, resultado)
    
    if resultado.melhor_ponto is None:
         return None, 0.0 # Retorno para árvore vazia
         
    return resultado.melhor_ponto, math.sqrt(resultado.melhor_distancia_sq)

# ----------------------------------------------------------------------
# 2. Inserção
# ----------------------------------------------------------------------

def inserir_ponto(node, novo_ponto, k, profundidade=0):
    """Insere um novo ponto na Árvore k-D (Valores iguais vão para a Direita)."""
    if node is None:
        dim = profundidade % k
        return KDNode(novo_ponto, dim)

    d = node.dim
    
    if novo_ponto[d] < node.ponto[d]:
        node.esquerda = inserir_ponto(node.esquerda, novo_ponto, k, profundidade + 1)
    else: # Valores iguais ou maiores vão para a direita
        node.direita = inserir_ponto(node.direita, novo_ponto, k, profundidade + 1)
        
    return node
    
# ----------------------------------------------------------------------
# 3. Construção (Balanceamento Estático)
# ----------------------------------------------------------------------

def construir_kd_tree(pontos_lista, k, profundidade=0):
    if not pontos_lista:
        return None

    dim = profundidade % k
    
    # Ordenação e Mediana (Garante Balanceamento Estático)
    pontos_lista.sort(key=lambda p: p[dim]) 
    mediana_indice = len(pontos_lista) // 2
    mediana_ponto = pontos_lista[mediana_indice]

    return KDNode(
        ponto=mediana_ponto,
        dim=dim,
        esquerda=construir_kd_tree(pontos_lista[:mediana_indice], k, profundidade + 1),
        direita=construir_kd_tree(pontos_lista[mediana_indice + 1:], k, profundidade + 1)
    )

# ----------------------------------------------------------------------
# 4. Exclusão e Rebalanceamento
# ----------------------------------------------------------------------

def coletar_pontos(node, pontos):
    """Coleta todos os pontos da sub-árvore para reconstrução."""
    if node is not None:
        pontos.append(node.ponto)
        coletar_pontos(node.esquerda, pontos)
        coletar_pontos(node.direita, pontos)

def excluir_ponto_e_rebalancear(raiz, ponto_a_excluir, k):
    """Implementa o re-balanceamento por reconstrução total."""
    pontos = []
    coletar_pontos(raiz, pontos)
    
    try:
        pontos.remove(ponto_a_excluir)
        print(f"Ponto {ponto_a_excluir} removido com sucesso.")
    except ValueError:
        print(f"Ponto {ponto_a_excluir} não encontrado.")
        return raiz 
        
    # Reconstrução total (o balanceamento)
    nova_raiz = construir_kd_tree(pontos, k)
    return nova_raiz

# ----------------------------------------------------------------------
# 5. Plotagem (Espacial)
# ----------------------------------------------------------------------

def plotar_kd_tree(node, min_coords, max_coords, depth=0, k=2):
    """Plota a árvore 2D, mostrando os pontos e as linhas de divisão."""
    if node is None:
        return

    d = node.dim
    cor = 'r' if d == 0 else 'b' 
    
    plt.plot(node.ponto[0], node.ponto[1], 'ko') 

    if d == 0: 
        plt.vlines(node.ponto[0], min_coords[1], max_coords[1], colors=cor, linestyles='--')
        
        l_max_coords = (node.ponto[0], max_coords[1])
        r_min_coords = (node.ponto[0], min_coords[1])
        
        plotar_kd_tree(node.esquerda, min_coords, l_max_coords, depth + 1, k)
        plotar_kd_tree(node.direita, r_min_coords, max_coords, depth + 1, k)

    elif d == 1: 
        plt.hlines(node.ponto[1], min_coords[0], max_coords[0], colors=cor, linestyles='--')
        
        l_max_coords = (max_coords[0], node.ponto[1])
        r_min_coords = (min_coords[0], node.ponto[1])

        plotar_kd_tree(node.esquerda, min_coords, l_max_coords, depth + 1, k)
        plotar_kd_tree(node.direita, r_min_coords, max_coords, depth + 1, k)

# ----------------------------------------------------------------------
# 6. Demonstração
# ----------------------------------------------------------------------

if __name__ == '__main__':
    k_dim = 2
    N_PONTOS = 25 # Mínimo de 21 nós atendido
    
    # Geração de 25 Pontos Aleatórios
    pontos_2d = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(N_PONTOS)]
    
    # É crucial passar uma CÓPIA para a construção, pois a função a ordena
    raiz_kd = construir_kd_tree(pontos_2d[:], k_dim) 
    
    # ------------------ CÁLCULO DE LIMITES PARA PLOTAGEM ------------------
    min_x = min(p[0] for p in pontos_2d) - 5
    max_x = max(p[0] for p in pontos_2d) + 5
    min_y = min(p[1] for p in pontos_2d) - 5
    max_y = max(p[1] for p in pontos_2d) + 5
    
    # ------------------ PLOTAGEM INICIAL ------------------
    plt.figure(figsize=(8, 8))
    plt.title("1. Árvore k-D Construída (Cortes Alternados)")
    plotar_kd_tree(raiz_kd, (min_x, min_y), (max_x, max_y))
    plt.xlim(min_x, max_x)
    plt.ylim(min_y, max_y)
    plt.xlabel("Dimensão X (Corte Vermelho)")
    plt.ylabel("Dimensão Y (Corte Azul)")
    plt.grid(True)
    plt.show() 
    
    # ------------------ TESTE DE BUSCA (VMP) ------------------
    ponto_busca = (50, 50)
    melhor_ponto, melhor_distancia = buscar_vizinho_mais_proximo(raiz_kd, ponto_busca)
    
    print("\n" + "="*40)
    print("TESTE DE BUSCA (Vizinho Mais Próximo - VMP)")
    print("="*40)
    print(f"Ponto de Consulta: {ponto_busca}")
    print(f"Vizinho Mais Próximo Encontrado: {melhor_ponto}")
    print(f"Distância: {melhor_distancia:.2f}")

    # ------------------ TESTE DE EXCLUSÃO E RE-BALANCEAMENTO ------------------
    ponto_a_remover = raiz_kd.ponto # Exclui a raiz atual
    
    print("\n" + "="*40)
    print("TESTE DE EXCLUSÃO E RE-BALANCEAMENTO")
    print("="*40)
    raiz_kd_nova = excluir_ponto_e_rebalancear(raiz_kd, ponto_a_remover, k_dim)
    
    # ------------------ PLOTAGEM PÓS-EXCLUSÃO ------------------
    if raiz_kd_nova:
        plt.figure(figsize=(8, 8))
        plt.title("2. Árvore k-D Após Exclusão e Reconstrução (Re-balanceada)")
        plotar_kd_tree(raiz_kd_nova, (min_x, min_y), (max_x, max_y))
        plt.xlim(min_x, max_x)
        plt.ylim(min_y, max_y)
        plt.xlabel("Dimensão X (Corte Vermelho)")
        plt.ylabel("Dimensão Y (Corte Azul)")
        plt.grid(True)
        plt.show()