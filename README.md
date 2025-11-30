# 🌳 Implementação de Árvores Balanceadas em Python

Este repositório contém implementações completas de duas estruturas de dados de árvores balanceadas: **Árvore Rubro-Negra** e **Árvore 2-3-4**.

---

## 📁 Estrutura do Projeto

```
Grafos/
├── arvore-rubro-negra/
│   ├── rubro_negra.py                    # Implementação da árvore rubro-negra
│   ├── teste_adicao_visualizacao.py      # Demonstração de inserção com visualização
│   ├── teste_busca.py                    # Demonstração de busca
│   └── teste_remocao.py                  # Demonstração de remoção com rebalanceamento
│
└── arvore-2-3-4/
    ├── main.py                           # Implementação da árvore 2-3-4
    └── implementaçao.py                  # Demonstração de uso
```

---

## 🔴⚫ Árvore Rubro-Negra (Red-Black Tree)

### 📖 Descrição

Uma árvore rubro-negra é uma árvore binária de busca balanceada onde cada nó possui uma cor (vermelho ou preto). A estrutura mantém propriedades específicas que garantem balanceamento automático, resultando em operações O(log n).

### ✨ Características

- **Estrutura de nós**: Similar a listas duplamente encadeadas com ponteiros para pai, filho esquerdo e direito
- **Coloração**: Cada nó é vermelho ou preto
- **Balanceamento automático**: Através de rotações e recolorações
- **Complexidade**: O(log n) para inserção, remoção e busca

### 🔧 Funcionalidades Implementadas

- ✅ Inserção com balanceamento (`insert`)
- ✅ Remoção com balanceamento (`delete`)
- ✅ Busca de elementos (`search`)
- ✅ Travessia inorder (`inorder`)
- ✅ Rotações (esquerda e direita)
- ✅ Visualização gráfica com Matplotlib

### 🚀 Como Executar

#### Pré-requisitos

```bash
pip install matplotlib
```

#### 1. Visualização de Inserção (21 nós)

```bash
cd arvore-rubro-negra
python teste_adicao_visualizacao.py
```

**O que faz:**
- Insere 21 valores na árvore
- Mostra a árvore em ordem (inorder)
- Gera visualização gráfica da árvore completa
- Realiza testes de busca

#### 2. Teste de Busca Simples

```bash
python teste_busca.py
```

**O que faz:**
- Cria uma árvore com 11 valores
- Demonstra o processo de inserção
- Executa buscas de valores existentes e inexistentes

#### 3. Demonstração de Remoção

```bash
python teste_remocao.py
```

**O que faz:**
- Cria árvore com 21 nós
- Remove o nó 20 (nó interno)
- Mostra estatísticas antes e depois
- Visualiza a árvore após rebalanceamento

### 📊 Exemplo de Uso Programático

```python
from rubro_negra import RedBlackTree

# Criar árvore
rbt = RedBlackTree()

# Inserir valores
valores = [50, 20, 70, 10, 30, 60, 80]
for v in valores:
    rbt.insert(v)

# Buscar valor
resultado = rbt.search(rbt.root, 30)
if resultado != rbt.NULL:
    print(f"Valor 30 encontrado! Cor: {resultado.color}")

# Remover valor
rbt.delete(20)

# Imprimir árvore em ordem
rbt.inorder(rbt.root)
```

### 🎨 Visualização

A biblioteca **Matplotlib** é utilizada para criar visualizações hierárquicas da árvore:
- Nós vermelhos são exibidos em vermelho
- Nós pretos são exibidos em preto
- Layout hierárquico mostra a estrutura real da árvore
- Legenda clara identifica as cores

---

## 🔢 Árvore 2-3-4

### 📖 Descrição

Uma árvore 2-3-4 é uma árvore balanceada onde cada nó pode conter 1, 2 ou 3 chaves e ter 2, 3 ou 4 filhos respectivamente. Todos os nós folha estão no mesmo nível, garantindo balanceamento perfeito.

### ✨ Características

- **Nós flexíveis**: Cada nó pode ter 1-3 chaves
- **Balanceamento perfeito**: Todas as folhas no mesmo nível
- **Split automático**: Nós cheios são divididos durante inserção
- **Complexidade**: O(log n) para todas as operações

### 🔧 Funcionalidades Implementadas

- ✅ Inserção com split automático (`insert`)
- ✅ Busca de elementos (`search`)
- ✅ Impressão estruturada da árvore (`print_tree`)
- ✅ Verificação de nó cheio (`is_full`)
- ✅ Verificação de folha (`is_leaf`)

### 🚀 Como Executar

#### Demonstração Básica

```bash
cd arvore-2-3-4
python implementaçao.py
```

**O que faz:**
- Insere os valores [10, 20, 30, 40, 50]
- Mostra a estrutura da árvore após cada inserção
- Realiza buscas de valores existentes e inexistentes

### 📊 Exemplo de Uso Programático

```python
from main import Tree234

# Criar árvore
tree = Tree234()

# Inserir valores
valores = [10, 20, 30, 40, 50]
for v in valores:
    tree.insert(v)

# Buscar valor
encontrado = tree.search(tree.root, 30)
print(f"Valor 30 encontrado: {encontrado}")

# Imprimir estrutura
tree.print_tree()
```

### 🎯 Estrutura de Nós

```
Nó 2: [K1] → 2 filhos
Nó 3: [K1, K2] → 3 filhos
Nó 4: [K1, K2, K3] → 4 filhos (será dividido)
```

---

## 🆚 Comparação: Rubro-Negra vs 2-3-4

| Aspecto | Árvore Rubro-Negra | Árvore 2-3-4 |
|---------|-------------------|--------------|
| **Estrutura** | Binária (2 filhos por nó) | Flexível (2-4 filhos por nó) |
| **Balanceamento** | Por coloração e rotações | Por splits de nós |
| **Chaves por nó** | 1 | 1-3 |
| **Altura** | ≤ 2 log₂(n+1) | log₄(n) a log₂(n) |
| **Complexidade espaço** | Menor | Maior |
| **Implementação** | Mais complexa | Mais intuitiva |
| **Uso prático** | std::map, TreeMap | B-Trees, Bancos de dados |

---

## 📚 Conceitos Técnicos

### Propriedades da Árvore Rubro-Negra

1. Cada nó é vermelho ou preto
2. A raiz é sempre preta
3. Nós vermelhos não podem ter filhos vermelhos
4. Todos os caminhos da raiz às folhas têm o mesmo número de nós pretos
5. Todas as folhas (NIL) são pretas

### Propriedades da Árvore 2-3-4

1. Todos os nós folha estão no mesmo nível
2. Nós podem ter 2, 3 ou 4 filhos
3. Nós com k chaves têm k+1 filhos
4. Chaves em cada nó estão ordenadas
5. Nós cheios (3 chaves) são divididos antes de inserção

---

## 🎓 Casos de Uso

### Árvore Rubro-Negra
- Implementação de mapas e conjuntos ordenados
- Java: `TreeMap`, `TreeSet`
- C++: `std::map`, `std::set`
- Linux: Completely Fair Scheduler

### Árvore 2-3-4
- Base conceitual para B-Trees
- Sistemas de arquivos
- Bancos de dados
- Cache de sistemas operacionais

---

## 🛠️ Requisitos do Sistema

### Software
- Python 3.7+
- Matplotlib (apenas para árvore rubro-negra)

### Instalação de Dependências

```bash
# Para visualização da árvore rubro-negra
pip install matplotlib
```

---

## 📈 Exemplos de Conjuntos de Testes

### Conjunto Mínimo (Árvore Rubro-Negra - 21 nós)
```python
valores = [50, 20, 70, 10, 30, 60, 80, 5, 15, 25, 35, 
          55, 65, 75, 85, 1, 7, 27, 37, 57, 67]
```

### Conjunto Básico (Árvore 2-3-4 - 5 nós)
```python
valores = [10, 20, 30, 40, 50]
```

---

## 🤝 Autor

**Felipe Brazão**
- GitHub: [@felipebrazao](https://github.com/felipebrazao)
- Repositório: [arvores-binarias](https://github.com/felipebrazao/arvores-binarias)

---

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais e está disponível sob licença MIT.

---

## 🎯 Notas Técnicas

### Sobre a Implementação Rubro-Negra

A implementação utiliza uma abordagem com ponteiros bidirecionais (similar a listas duplamente encadeadas), onde cada nó mantém referência ao pai. Isso facilita as operações de rotação e balanceamento durante correções algorítmicas.

### Sobre a Visualização

Optei por utilizar exclusivamente **Matplotlib** para visualização, abandonando **NetworkX** inicial que gerava layouts não-hierárquicos. O algoritmo customizado de posicionamento garante que a estrutura hierárquica real da árvore seja representada fielmente.

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Certifique-se de estar no diretório correto
3. Abra uma issue no repositório GitHub

---

**🌳 Estruturas de dados elegantes para operações eficientes! 🌳**
