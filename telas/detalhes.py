# ============================================================
# ARQUIVO: telas/detalhes.py
# Tela de detalhes do pet
# ============================================================

import customtkinter as ctk

FUNDO     = "#F7F9FC"
BRANCO    = "#FFFFFF"
AZUL      = "#4E92E3"
VERDE     = "#16A34A"
CINZA     = "#53687A"
SUBTITULO = "#8CA0B3"


def abrir_detalhes(root, pet):

    # ========================================================
    # LIMPA A TELA ATUAL
    # ========================================================
    for widget in root.winfo_children():
        widget.destroy()

    # ========================================================
    # CONTAINER PRINCIPAL
    # ========================================================
    container = ctk.CTkFrame(
        root,
        fg_color=FUNDO
    )

    container.pack(fill="both", expand=True)

    # ========================================================
    # NAVBAR SIMPLES
    # ========================================================
    navbar = ctk.CTkFrame(
        container,
        fg_color=BRANCO,
        height=70,
        corner_radius=0
    )

    navbar.pack(fill="x")
    navbar.pack_propagate(False)

    ctk.CTkLabel(
        navbar,
        text="🐾 PetFinder",
        text_color=CINZA,
        font=("Segoe UI", 28, "bold")
    ).pack(side="left", padx=30)

    # ========================================================
    # CONTEÚDO
    # ========================================================
    content = ctk.CTkFrame(
        container,
        fg_color=FUNDO
    )

    content.pack(fill="both", expand=True, padx=40, pady=30)

    # ========================================================
    # BOTÃO VOLTAR
    # ========================================================
    from telas.inicio import criar_tela_inicio

    ctk.CTkButton(
        content,
        text="← Voltar",
        fg_color="transparent",
        hover_color="#E9EEF5",
        text_color=SUBTITULO,
        font=("Segoe UI", 18, "bold"),
        width=120,
        height=40,
        command=lambda: criar_tela_inicio(root)
    ).pack(anchor="w", pady=(0, 25))

    # ========================================================
    # CARD PRINCIPAL
    # ========================================================
    card_principal = ctk.CTkFrame(
        content,
        fg_color=BRANCO,
        corner_radius=30
    )

    card_principal.pack(fill="both", expand=True)

    # ========================================================
    # STATUS
    # ========================================================
    if pet["status"] == "Encontrado":
        cor_status = VERDE
    else:
        cor_status = "#E53935"

    status_frame = ctk.CTkFrame(
        card_principal,
        fg_color=FUNDO,
        corner_radius=0
    )

    status_frame.pack(fill="x", padx=30, pady=30)

    ctk.CTkLabel(
        status_frame,
        text=pet["status"],
        fg_color=cor_status,
        text_color="white",
        corner_radius=20,
        width=120,
        height=40,
        font=("Segoe UI", 14, "bold")
    ).pack(anchor="ne")

    # ========================================================
    # NOME E BAIRRO
    # ========================================================
    ctk.CTkLabel(
        card_principal,
        text=pet["icone"],
        font=("Segoe UI Emoji", 55)
    ).pack(anchor="w", padx=40)

    ctk.CTkLabel(
        card_principal,
        text=pet["nome"],
        text_color=CINZA,
        font=("Segoe UI", 36, "bold")
    ).pack(anchor="w", padx=40)

    ctk.CTkLabel(
        card_principal,
        text=f"📍 {pet['bairro']}",
        text_color=SUBTITULO,
        font=("Segoe UI", 18)
    ).pack(anchor="w", padx=40, pady=(5, 30))

    # ========================================================
    # ÁREA DOS CARDS
    # ========================================================
    cards = ctk.CTkFrame(
        card_principal,
        fg_color=BRANCO
    )

    cards.pack(fill="x", padx=40, pady=(0, 40))

    # ========================================================
    # CARD INFORMAÇÕES
    # ========================================================
    card_info = ctk.CTkFrame(
        cards,
        fg_color="#EEF2F6",
        corner_radius=25,
        width=450,
        height=220
    )

    card_info.pack(side="left", padx=(0, 20), fill="both", expand=True)
    card_info.pack_propagate(False)

    ctk.CTkLabel(
        card_info,
        text="Informações",
        text_color=CINZA,
        font=("Segoe UI", 24, "bold")
    ).pack(anchor="w", padx=25, pady=(25, 20))

    ctk.CTkLabel(
        card_info,
        text=f"Cor: {pet['cor']}",
        text_color=CINZA,
        font=("Segoe UI", 18, "bold")
    ).pack(anchor="w", padx=25, pady=5)

    ctk.CTkLabel(
        card_info,
        text=f"Raça: {pet['raca']}",
        text_color=CINZA,
        font=("Segoe UI", 18, "bold")
    ).pack(anchor="w", padx=25, pady=5)

    ctk.CTkLabel(
        card_info,
        text=f"Tipo: {pet['tipo']}",
        text_color=CINZA,
        font=("Segoe UI", 18, "bold")
    ).pack(anchor="w", padx=25, pady=5)

    # ========================================================
    # CARD DESCRIÇÃO
    # ========================================================
    card_desc = ctk.CTkFrame(
        cards,
        fg_color="#EEF2F6",
        corner_radius=25,
        width=450,
        height=220
    )

    card_desc.pack(side="left", fill="both", expand=True)
    card_desc.pack_propagate(False)

    ctk.CTkLabel(
        card_desc,
        text="Descrição",
        text_color=CINZA,
        font=("Segoe UI", 24, "bold")
    ).pack(anchor="w", padx=25, pady=(25, 20))

    ctk.CTkLabel(
        card_desc,
        text=pet["descricao"],
        text_color=SUBTITULO,
        font=("Segoe UI", 18),
        wraplength=350,
        justify="left"
    ).pack(anchor="w", padx=25)