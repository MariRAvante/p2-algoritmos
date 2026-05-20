# ============================================================
# ARQUIVO: main.py
# FUNÇÃO: Ponto de entrada do programa. É o primeiro arquivo
#         que roda quando você executa o projeto.
#         Ele cria a janela principal e chama a tela inicial.
# ============================================================

# "import" traz funcionalidades de outros arquivos/bibliotecas
# customtkinter é uma versão moderninha do tkinter padrão
import customtkinter as ctk

# Importa a função criar_tela_inicio do arquivo telas/inicio.py
# Isso nos permite usar a função aqui sem reescrever o código
from telas.inicio import criar_tela_inicio


# ========================
# JANELA PRINCIPAL
# ========================

# ctk.CTk() cria a janela principal do programa
# (como se fosse o "esqueleto" onde tudo vai ser desenhado)
root = ctk.CTk()

# Define o texto que aparece na barra de título da janela
root.title("PetFinder")

# Define o tamanho inicial da janela: largura x altura (em pixels)
root.geometry("1000x700")

# Define a cor de fundo da janela (código hexadecimal de cor)
root.configure(bg="#f5f5f5")


# ========================
# CHAMADA DA TELA INICIAL
# ========================

# Chama a função que desenha todos os elementos visuais
# da tela inicial dentro da janela "root"
criar_tela_inicio(root)


# ========================
# LOOP PRINCIPAL
# ========================

# root.mainloop() mantém a janela aberta e "escutando" eventos
# (cliques, digitação, etc.). Sem isso, a janela abriria e fecharia
# imediatamente. É o coração do programa — fica rodando até o usuário fechar.
root.mainloop()
