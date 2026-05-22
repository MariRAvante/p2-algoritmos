# ARQUIVO: telas/inicio.py
# CONCEITOS: for (repetição), if/else (condição), dicionários
# O tkinter aqui serve apenas para "pintar" a tela.
# A lógica (percorrer a lista, escolher cor) é Python puro.
# ============================================================
 
import customtkinter as ctk
from dados.pets import pets
from telas.cadastro import abrir_cadastro
 
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
 
# Constantes de cor — variáveis do tipo string com código hex
FUNDO     = "#F7F9FC"
BRANCO    = "#FFFFFF"
AZUL      = "#4E92E3"
LARANJA   = "#FF916F"
VERDE     = "#16A34A"
CINZA     = "#53687A"
SUBTITULO = "#8CA0B3"
 
 
def criar_tela_inicio(root):
 
    # Limpa a tela antes de redesenhar
    # Estrutura de repetição: for widget in lista_de_widgets
    for widget in root.winfo_children():
        widget.destroy()
 
    container = ctk.CTkFrame(root, fg_color=FUNDO, corner_radius=0)
    container.pack(fill="both", expand=True)
 
    # --- NAVBAR ---
    navbar = ctk.CTkFrame(container, fg_color=BRANCO, height=80, corner_radius=0)
    navbar.pack(fill="x")
    ctk.CTkLabel(navbar, text="🐾 PetFinder",
                 text_color=CINZA, font=("Segoe UI", 28, "bold")).pack(side="left", padx=30, pady=20)
 
    # --- TÍTULOS ---
    # print("Bem-Vindo ao PetFinder")  ←  equivalente ao Label abaixo
    ctk.CTkLabel(container, text="Bem-Vindo ao PetFinder",
                 text_color=CINZA, font=("Segoe UI", 38, "bold")).pack(pady=(40, 10))
    ctk.CTkLabel(container, text="Ajude a reunir famílias com seus pets.",
                 text_color=SUBTITULO, font=("Segoe UI", 18)).pack()
 
    # --- CARDS DE AÇÃO (Perdi / Encontrei) ---
    cards_frame = ctk.CTkFrame(container, fg_color=FUNDO)
    cards_frame.pack(pady=40)
 
    for texto, cor_card, cor_texto, status_acao in [
        ("Perdi meu pet",    AZUL,    "#E9F1FB", "Perdido"),
        ("Encontrei um pet", LARANJA, "#FFF3EE", "Encontrado")
    ]:
        card = ctk.CTkFrame(cards_frame, fg_color=cor_card,
                            corner_radius=25, width=350, height=200)
        card.pack(side="left", padx=20)
        card.pack_propagate(False)
 
        ctk.CTkLabel(card, text=texto,
                     text_color="white", font=("Segoe UI", 28, "bold")).pack(pady=(40, 10))
        ctk.CTkLabel(card, text=f"Registrar animal {status_acao.lower()}",
                     text_color=cor_texto, font=("Segoe UI", 15)).pack()
        ctk.CTkButton(card, text="Registrar",
                      fg_color="white", text_color=cor_card,
                      hover_color="#F1F1F1", corner_radius=15,
                      width=140, height=40, font=("Segoe UI", 14, "bold"),
                      command=lambda s=status_acao: abrir_cadastro(root, s)).pack(pady=25)
 
    # --- LISTA DE PETS RECENTES ---
    ctk.CTkLabel(container, text="Animais Recentes",
                 text_color=CINZA, font=("Segoe UI", 30, "bold")).pack(pady=(20, 30))
 
    pets_frame = ctk.CTkFrame(container, fg_color=FUNDO)
    pets_frame.pack()
 
    # -------------------------------------------------------
    # ESTRUTURA DE REPETIÇÃO: for
    # Percorre cada dicionário da lista "pets"
    # Equivale a:
    #   for pet in pets:
    #       print(pet['nome'], pet['status'])
    # -------------------------------------------------------
    for pet in pets:
 
        # ESTRUTURA DE CONDIÇÃO: if / else
        # Escolhe a cor da etiqueta com base no valor de pet['status']
        if pet["status"] == "Encontrado":
            cor_status = VERDE    # verde
        else:
            cor_status = "#E53935"  # vermelho
 
        # Cria o card visual para este pet
        card = ctk.CTkFrame(pets_frame, fg_color=BRANCO,
                            corner_radius=25, width=260, height=260)
        card.pack(side="left", padx=15)
        card.pack_propagate(False)
 
        # Etiqueta de status (Perdido / Encontrado)
        ctk.CTkLabel(card, text=pet["status"],
                     fg_color=cor_status, text_color="white",
                     corner_radius=20, width=100, height=35,
                     font=("Segoe UI", 13, "bold")).pack(anchor="ne", padx=15, pady=15)
 
        # Acesso ao dicionário: pet["icone"], pet["nome"], pet["bairro"]
        ctk.CTkLabel(card, text=pet["icone"],
                     font=("Segoe UI Emoji", 45)).pack(pady=(5, 0))
 
        ctk.CTkLabel(card, text=pet["nome"],
                     text_color=CINZA, font=("Segoe UI", 24, "bold")).pack()
 
        # f-string: mistura texto fixo com valor do dicionário
        ctk.CTkLabel(card, text=f"📍 {pet['bairro']}",
                     text_color=SUBTITULO, font=("Segoe UI", 15)).pack(pady=5)
 
        ctk.CTkButton(card, text="Ver detalhes",
                      fg_color=AZUL, hover_color="#3F7FD0",
                      corner_radius=15, height=42,
                      font=("Segoe UI", 14, "bold")).pack(padx=20, pady=20, fill="x")