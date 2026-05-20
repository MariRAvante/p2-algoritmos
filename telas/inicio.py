# ============================================================
# ARQUIVO: telas/inicio.py
# FUNÇÃO: Monta e exibe a tela inicial do PetFinder.
#         Contém a navbar, os cards de ação ("Perdi"/"Encontrei")
#         e a lista de pets recentes cadastrados.
# ============================================================

import customtkinter as ctk

# Importa a lista de pets do arquivo dados/pets.py
# Usaremos essa lista para exibir os cards de animais na tela
from dados.pets import pets

# Importa a função que abre a janela de cadastro (telas/cadastro.py)
from telas.cadastro import abrir_cadastro


# ========================
# CONFIGURAÇÕES VISUAIS
# ========================

# Define o tema geral: "light" = fundo claro, "dark" = fundo escuro
ctk.set_appearance_mode("light")

# Define a paleta de cores padrão dos botões e componentes
ctk.set_default_color_theme("blue")

# Constantes de cor (hexadecimal). Usar constantes evita repetir
# o mesmo valor em vários lugares — se quiser mudar a cor, muda só aqui!
FUNDO    = "#F7F9FC"  # Cor de fundo da tela
BRANCO   = "#FFFFFF"  # Branco puro (cards, navbar)
AZUL     = "#4E92E3"  # Azul principal (botões, card "Perdi")
LARANJA  = "#FF916F"  # Laranja (card "Encontrei")
VERDE    = "#16A34A"  # Verde (status "Encontrado")
CINZA    = "#53687A"  # Cinza escuro (títulos)
SUBTITULO = "#8CA0B3" # Cinza claro (subtítulos, bairro)


# ============================================================
# FUNÇÃO PRINCIPAL DA TELA
# ============================================================

# "def" define uma função — um bloco de código que só roda
# quando chamado. "root" é a janela principal passada como parâmetro.
def criar_tela_inicio(root):

    # ========================
    # LIMPA A TELA
    # ========================

    # Antes de desenhar a tela, apaga todos os widgets existentes.
    # Isso é necessário quando voltamos da tela de cadastro,
    # para não empilhar elementos na janela.

    # root.winfo_children() retorna uma LISTA com todos os widgets
    # que estão dentro da janela principal.
    # O "for" percorre cada widget e o destrói — estrutura de repetição!
    for widget in root.winfo_children():
        widget.destroy()  # Remove o widget da janela


    # ========================
    # CONTAINER PRINCIPAL
    # ========================

    # CTkFrame é um "quadro" (retângulo) que agrupa outros elementos.
    # Usamos como base para organizar tudo dentro da janela.
    container = ctk.CTkFrame(
        root,                # Onde o frame vai ficar (dentro de root)
        fg_color=FUNDO,      # fg_color = cor de fundo do frame
        corner_radius=0      # Sem bordas arredondadas
    )

    # pack() posiciona o widget na janela.
    # fill="both" + expand=True faz o container ocupar todo o espaço disponível.
    container.pack(fill="both", expand=True)


    # ========================
    # NAVBAR (barra superior)
    # ========================

    # Frame que vai servir de barra de navegação no topo
    navbar = ctk.CTkFrame(
        container,
        fg_color=BRANCO,   # Fundo branco
        height=80,         # Altura fixa de 80 pixels
        corner_radius=0    # Sem arredondamento
    )

    navbar.pack(fill="x")  # fill="x" estica horizontalmente (só largura)

    # Logo do app — um simples texto com emoji
    logo = ctk.CTkLabel(
        navbar,
        text="🐾 PetFinder",
        text_color=CINZA,
        font=("Segoe UI", 28, "bold")  # (fonte, tamanho, estilo)
    )

    # side="left" encosta o logo no lado esquerdo da navbar
    # padx/pady adicionam espaço ao redor do elemento (padding)
    logo.pack(side="left", padx=30, pady=20)

    # Botão "Cadastrar Pet" no canto direito da navbar
    botao_nav = ctk.CTkButton(
        navbar,
        text="Cadastrar Pet",
        fg_color=AZUL,
        hover_color="#3F7FD0",   # Cor quando o mouse passa por cima
        corner_radius=15,        # Bordas arredondadas
        height=45,
        width=160,
        font=("Segoe UI", 14, "bold")
        # Sem "command=" aqui — esse botão não tem ação definida ainda
    )

    botao_nav.pack(side="right", padx=30)  # Encosta no lado direito


    # ========================
    # TÍTULOS DA TELA
    # ========================

    # Título principal
    titulo = ctk.CTkLabel(
        container,
        text="Bem-Vindo ao PetFinder",
        text_color=CINZA,
        font=("Segoe UI", 38, "bold")
    )

    # pady=(40, 10) = 40px de espaço acima e 10px abaixo
    titulo.pack(pady=(40, 10))

    # Subtítulo abaixo do título principal
    subtitulo = ctk.CTkLabel(
        container,
        text="Ajude a reunir famílias com seus pets.",
        text_color=SUBTITULO,
        font=("Segoe UI", 18)
    )

    subtitulo.pack()


    # ========================
    # FRAME DOS CARDS DE AÇÃO
    # ========================

    # Frame que vai conter os dois cards lado a lado ("Perdi" e "Encontrei")
    cards_frame = ctk.CTkFrame(
        container,
        fg_color=FUNDO  # Mesmo fundo da tela, fica invisível
    )

    cards_frame.pack(pady=40)  # Espaço de 40px acima e abaixo


    # ========================
    # CARD: "PERDI MEU PET"
    # ========================

    # Frame azul que representa o card de animal perdido
    card1 = ctk.CTkFrame(
        cards_frame,
        fg_color=AZUL,       # Fundo azul
        corner_radius=25,    # Bordas bem arredondadas
        width=350,
        height=200
    )

    # side="left" coloca ao lado do outro card
    # padx=20 dá espaço entre os cards
    card1.pack(side="left", padx=20)

    # pack_propagate(False) impede que o frame encolha para caber o conteúdo
    # — mantém o tamanho fixo definido acima (width=350, height=200)
    card1.pack_propagate(False)

    # Título do card
    ctk.CTkLabel(
        card1,
        text="Perdi meu pet",
        text_color="white",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(40, 10))  # 40px acima, 10px abaixo

    # Descrição do card
    ctk.CTkLabel(
        card1,
        text="Registrar animal perdido",
        text_color="#E9F1FB",  # Azul bem claro (quase branco)
        font=("Segoe UI", 15)
    ).pack()

    # Botão "Registrar" — chama a função abrir_cadastro quando clicado
    ctk.CTkButton(
        card1,
        text="Registrar",
        fg_color="white",     # Fundo branco (contraste com o card azul)
        text_color=AZUL,      # Texto azul
        hover_color="#F1F1F1",
        corner_radius=15,
        width=140,
        height=40,
        font=("Segoe UI", 14, "bold"),
        # "command" define o que acontece ao clicar.
        # "lambda" cria uma função anônima (sem nome) na hora —
        # usamos lambda pois precisamos passar argumentos (root e "Perdido")
        # para abrir_cadastro. Sem lambda, a função rodaria imediatamente.
        command=lambda: abrir_cadastro(root, "Perdido")
    ).pack(pady=25)


    # ========================
    # CARD: "ENCONTREI UM PET"
    # ========================

    # Mesmo esquema do card anterior, mas com cor laranja
    card2 = ctk.CTkFrame(
        cards_frame,
        fg_color=LARANJA,    # Fundo laranja
        corner_radius=25,
        width=350,
        height=200
    )

    card2.pack(side="left", padx=20)
    card2.pack_propagate(False)

    ctk.CTkLabel(
        card2,
        text="Encontrei um pet",
        text_color="white",
        font=("Segoe UI", 28, "bold")
    ).pack(pady=(40, 10))

    ctk.CTkLabel(
        card2,
        text="Registrar animal encontrado",
        text_color="#FFF3EE",  # Laranja bem claro
        font=("Segoe UI", 15)
    ).pack()

    ctk.CTkButton(
        card2,
        text="Registrar",
        fg_color="white",
        text_color=LARANJA,   # Texto laranja (contraste com o card)
        hover_color="#F1F1F1",
        corner_radius=15,
        width=140,
        height=40,
        font=("Segoe UI", 14, "bold"),
        # Mesmo uso de lambda, mas passa "Encontrado" como status
        command=lambda: abrir_cadastro(root, "Encontrado")
    ).pack(pady=25)


    # ========================
    # TÍTULO "ANIMAIS RECENTES"
    # ========================

    titulo_pets = ctk.CTkLabel(
        container,
        text="Animais Recentes",
        text_color=CINZA,
        font=("Segoe UI", 30, "bold")
    )

    titulo_pets.pack(pady=(20, 30))


    # ========================
    # LISTA DE CARDS DE PETS
    # ========================

    # Frame que vai conter os cards dos animais cadastrados
    pets_frame = ctk.CTkFrame(
        container,
        fg_color=FUNDO  # Fundo invisível
    )

    pets_frame.pack()

    # ESTRUTURA DE REPETIÇÃO: percorre cada pet da lista "pets"
    # importada de dados/pets.py. Para cada pet, cria um card na tela.
    for pet in pets:

        # ========================
        # DEFINE COR DO STATUS
        # ========================

        # ESTRUTURA DE DECISÃO: cor vermelha por padrão (Perdido)
        cor_status = "#E53935"  # Vermelho

        # Se o status do pet for "Encontrado", muda para verde
        if pet["status"] == "Encontrado":
            cor_status = VERDE  # Verde

        # Aqui acessamos o dicionário do pet pela chave "status" — ex: pet["status"]


        # ========================
        # CARD DO PET
        # ========================

        # Cria um frame branco para cada animal
        card = ctk.CTkFrame(
            pets_frame,
            fg_color=BRANCO,
            corner_radius=25,
            width=260,
            height=260
        )

        # side="left" coloca os cards um ao lado do outro
        card.pack(side="left", padx=15)
        card.pack_propagate(False)  # Mantém tamanho fixo


        # ETIQUETA DE STATUS (Perdido / Encontrado)
        # A cor muda conforme a variável cor_status definida acima
        status = ctk.CTkLabel(
            card,
            text=pet["status"],       # Pega o valor da chave "status" do dicionário
            fg_color=cor_status,      # Vermelho ou verde, dependendo do status
            text_color="white",
            corner_radius=20,
            width=100,
            height=35,
            font=("Segoe UI", 13, "bold")
        )

        # anchor="ne" = canto superior direito (north-east)
        status.pack(anchor="ne", padx=15, pady=15)


        # ÍCONE DO PET (emoji: 🐶 ou 😺)
        ctk.CTkLabel(
            card,
            text=pet["icone"],         # Pega o emoji da chave "icone" do dicionário
            font=("Segoe UI Emoji", 45) # Fonte grande para o emoji aparecer bem
        ).pack(pady=(5, 0))


        # NOME DO PET
        ctk.CTkLabel(
            card,
            text=pet["nome"],          # Pega o nome da chave "nome" do dicionário
            text_color=CINZA,
            font=("Segoe UI", 24, "bold")
        ).pack()


        # BAIRRO DO PET
        # f"..." é uma f-string: permite misturar texto fixo com variáveis
        # {pet['bairro']} insere o valor da chave "bairro" do dicionário
        ctk.CTkLabel(
            card,
            text=f"📍 {pet['bairro']}",
            text_color=SUBTITULO,
            font=("Segoe UI", 15)
        ).pack(pady=5)


        # BOTÃO "VER DETALHES"
        # Por enquanto não tem ação — seria a próxima funcionalidade a implementar!
        ctk.CTkButton(
            card,
            text="Ver detalhes",
            fg_color=AZUL,
            hover_color="#3F7FD0",
            corner_radius=15,
            height=42,
            font=("Segoe UI", 14, "bold")
        ).pack(padx=20, pady=20, fill="x")  # fill="x" = ocupa toda a largura do card
