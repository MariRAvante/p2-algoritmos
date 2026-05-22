# ============================================================
# ARQUIVO: telas/cadastro.py
# CONCEITOS: variáveis, input (Entry.get), if/else, dicionários, append
# ============================================================
 
from tkinter import *
from tkinter import ttk
from dados.pets import pets
 
FUNDO = "#f5f5f5"
AZUL  = "#4E92E3"
CINZA = "#636E7A"
 
 
def abrir_cadastro(root, status):
 
    janela = Toplevel(root)
    janela.title("Cadastrar Pet")
    janela.geometry("500x650")
    janela.configure(bg=FUNDO)
 
    Label(janela, text=f"Cadastrar Pet ({status})",
          bg=FUNDO, fg=CINZA, font=("Arial", 22, "bold")).pack(pady=20)
 
    frame_form = Frame(janela, bg=FUNDO)
    frame_form.pack(padx=30, pady=10, fill="both")
 
    # -------------------------------------------------------
    # CAMPOS DO FORMULÁRIO
    # Cada Entry funciona igual a um input() do terminal:
    #   entry_nome.get()  ←→  input("Nome do Pet: ")
    # -------------------------------------------------------
 
    Label(frame_form, text="Nome do Pet",
          bg=FUNDO, fg=CINZA, font=("Arial", 12, "bold")).pack(anchor="w")
    entry_nome = Entry(frame_form, font=("Arial", 12))
    entry_nome.pack(fill="x", pady=5)
 
    Label(frame_form, text="Tipo do Pet",
          bg=FUNDO, fg=CINZA, font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 0))
    combo_tipo = ttk.Combobox(frame_form,
                              values=["Cachorro", "Gato"],  # lista de opções
                              font=("Arial", 12))
    combo_tipo.pack(fill="x", pady=5)
 
    Label(frame_form, text="Cor",
          bg=FUNDO, fg=CINZA, font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 0))
    entry_cor = Entry(frame_form, font=("Arial", 12))
    entry_cor.pack(fill="x", pady=5)
 
    Label(frame_form, text="Raça",
          bg=FUNDO, fg=CINZA, font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 0))
    entry_raca = Entry(frame_form, font=("Arial", 12))
    entry_raca.pack(fill="x", pady=5)
 
    Label(frame_form, text="Bairro",
          bg=FUNDO, fg=CINZA, font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 0))
    entry_bairro = Entry(frame_form, font=("Arial", 12))
    entry_bairro.pack(fill="x", pady=5)
 
    Label(frame_form, text="Descrição",
          bg=FUNDO, fg=CINZA, font=("Arial", 12, "bold")).pack(anchor="w", pady=(15, 0))
    texto_descricao = Text(frame_form, height=5, font=("Arial", 12))
    texto_descricao.pack(fill="x", pady=5)
 
 
    # -------------------------------------------------------
    # FUNÇÃO: cadastrar_pet
    # É chamada quando o usuário clica em "Cadastrar"
    # -------------------------------------------------------
    def cadastrar_pet():
        from telas.inicio import criar_tela_inicio
 
        # --- LEITURA DOS CAMPOS (equivale a variavel = input("...")) ---
        nome      = entry_nome.get()
        tipo      = combo_tipo.get()
        cor       = entry_cor.get()
        raca      = entry_raca.get()
        bairro    = entry_bairro.get()
        descricao = texto_descricao.get("1.0", END)
 
        # --- ESTRUTURA DE CONDIÇÃO: if / else ---
        # Mesma lógica que você usa no terminal:
        #   if tipo == "Cachorro":
        #       icone = "🐶"
        #   else:
        #       icone = "😺"
        if tipo == "Cachorro":
            icone = "🐶"
        else:
            icone = "😺"
 
        # --- DICIONÁRIO do novo pet ---
        # Igual ao formato já usado em dados/pets.py
        novo_pet = {
            "nome":      nome,
            "tipo":      tipo,
            "icone":     icone,
            "status":    status,    # "Perdido" ou "Encontrado"
            "cor":       cor,
            "raca":      raca,
            "bairro":    bairro,
            "descricao": descricao
        }
 
        # --- APPEND: adiciona o dicionário ao final da lista ---
        # Igual a:  lista.append(item)  que você viu em aula
        pets.append(novo_pet)
 
        # --- PRINT de confirmação no terminal (para testar) ---
        print("=== PET CADASTRADO ===")
        print("Nome:   ", novo_pet["nome"])
        print("Tipo:   ", novo_pet["tipo"])
        print("Status: ", novo_pet["status"])
        print("Bairro: ", novo_pet["bairro"])
        print("Total de pets cadastrados:", len(pets))
 
        # Volta para a tela inicial e fecha o popup
        criar_tela_inicio(root)
        janela.destroy()
 
 
    Button(janela, text="Cadastrar",
           bg=AZUL, fg="white", font=("Arial", 14, "bold"),
           relief="flat", padx=20, pady=10,
           command=cadastrar_pet).pack(pady=25)