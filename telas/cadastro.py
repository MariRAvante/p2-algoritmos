# ============================================================
# ARQUIVO: telas/cadastro.py
# FUNÇÃO: Abre uma janela secundária com um formulário para
#         o usuário cadastrar um pet (perdido ou encontrado).
#         Após o cadastro, volta para a tela inicial atualizada.
# ============================================================

# tkinter é a biblioteca padrão do Python para criar interfaces gráficas
from tkinter import *

# ttk é uma extensão do tkinter com widgets com visual mais moderno
# Usamos para o Combobox (campo de seleção / dropdown)
from tkinter import ttk

# Importa a lista de pets de dados/pets.py
# É nela que vamos adicionar o novo pet quando o formulário for enviado
from dados.pets import pets


# Constantes de cor (hexadecimal)
FUNDO = "#f5f5f5"  # Cinza bem clarinho (fundo da janela)
AZUL  = "#4E92E3"  # Azul dos botões
CINZA = "#636E7A"  # Cinza dos textos


# ============================================================
# FUNÇÃO PRINCIPAL: ABRIR JANELA DE CADASTRO
# ============================================================

# Recebe dois parâmetros:
#   root   = a janela principal (para poder voltar pra ela depois)
#   status = "Perdido" ou "Encontrado" (depende de qual card foi clicado)
def abrir_cadastro(root, status):

    # ========================
    # NOVA JANELA (POPUP)
    # ========================

    # Toplevel cria uma janela secundária (separada da janela principal)
    # É como abrir uma nova aba, mas em forma de janela flutuante
    janela = Toplevel(root)

    janela.title("Cadastrar Pet")       # Título da barra da janela
    janela.geometry("500x650")          # Tamanho: 500px de largura x 650px de altura
    janela.configure(bg=FUNDO)          # Cor de fundo


    # ========================
    # TÍTULO DA JANELA
    # ========================

    # Label = elemento de texto (não editável)
    # Exibe o título com o status entre parênteses: ex: "Cadastrar Pet (Perdido)"
    titulo = Label(
        janela,
        text=f"Cadastrar Pet ({status})",  # f-string insere o valor de "status"
        bg=FUNDO,                           # bg = cor de fundo do label
        fg=CINZA,                           # fg = cor do texto (foreground)
        font=("Arial", 22, "bold")
    )

    titulo.pack(pady=20)  # 20px de espaço vertical


    # ========================
    # FRAME DO FORMULÁRIO
    # ========================

    # Frame que agrupa todos os campos do formulário
    frame_form = Frame(janela, bg=FUNDO)

    # padx=30 = 30px de margem lateral | fill="both" = ocupa largura disponível
    frame_form.pack(padx=30, pady=10, fill="both")


    # ========================
    # CAMPO: NOME
    # ========================

    # Label acima do campo (rótulo)
    Label(
        frame_form,
        text="Nome do Pet",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 12, "bold")
    ).pack(anchor="w")  # anchor="w" = encosta à esquerda (west)

    # Entry = campo de texto onde o usuário digita
    # Guardamos na variável "entry_nome" para ler o valor depois
    entry_nome = Entry(frame_form, font=("Arial", 12))
    entry_nome.pack(fill="x", pady=5)  # fill="x" = ocupa toda a largura


    # ========================
    # CAMPO: TIPO
    # ========================

    Label(
        frame_form,
        text="Tipo do Pet",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(15, 0))  # pady=(15, 0) = 15px acima, 0 abaixo

    # Combobox = campo de seleção (dropdown / lista suspensa)
    # values define as opções disponíveis para o usuário escolher
    combo_tipo = ttk.Combobox(
        frame_form,
        values=["Cachorro", "Gato"],  # Lista de opções — uma lista Python!
        font=("Arial", 12)
    )

    combo_tipo.pack(fill="x", pady=5)


    # ========================
    # CAMPO: COR
    # ========================

    Label(
        frame_form,
        text="Cor",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(15, 0))

    entry_cor = Entry(frame_form, font=("Arial", 12))
    entry_cor.pack(fill="x", pady=5)


    # ========================
    # CAMPO: RAÇA
    # ========================

    Label(
        frame_form,
        text="Raça",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(15, 0))

    entry_raca = Entry(frame_form, font=("Arial", 12))
    entry_raca.pack(fill="x", pady=5)


    # ========================
    # CAMPO: BAIRRO
    # ========================

    Label(
        frame_form,
        text="Bairro",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(15, 0))

    entry_bairro = Entry(frame_form, font=("Arial", 12))
    entry_bairro.pack(fill="x", pady=5)


    # ========================
    # CAMPO: DESCRIÇÃO
    # ========================

    Label(
        frame_form,
        text="Descrição",
        bg=FUNDO,
        fg=CINZA,
        font=("Arial", 12, "bold")
    ).pack(anchor="w", pady=(15, 0))

    # Text = área de texto multilinha (diferente de Entry, que é uma linha só)
    # height=5 define a altura em número de linhas visíveis
    texto_descricao = Text(
        frame_form,
        height=5,
        font=("Arial", 12)
    )

    texto_descricao.pack(fill="x", pady=5)


    # ============================================================
    # FUNÇÃO INTERNA: CADASTRAR PET
    # ============================================================

    # Função definida DENTRO de abrir_cadastro — isso se chama "função aninhada".
    # Ela tem acesso às variáveis do escopo externo (entry_nome, combo_tipo, etc.)
    # porque está no mesmo bloco.
    def cadastrar_pet():

        # Importa a função de tela para recriar a tela inicial após o cadastro
        # (importado aqui dentro para evitar importação circular entre arquivos)
        from telas.inicio import criar_tela_inicio

        # ========================
        # LÊ OS VALORES DOS CAMPOS
        # ========================

        # .get() lê o texto digitado pelo usuário em cada campo Entry
        nome   = entry_nome.get()
        tipo   = combo_tipo.get()
        cor    = entry_cor.get()
        raca   = entry_raca.get()
        bairro = entry_bairro.get()

        # Para o widget Text (multilinha), usamos .get("1.0", END)
        # "1.0" = linha 1, coluna 0 (início do texto)
        # END = constante do tkinter que representa o fim do texto
        descricao = texto_descricao.get("1.0", END)


        # ========================
        # DEFINE O ÍCONE (DECISÃO)
        # ========================

        # ESTRUTURA DE DECISÃO: escolhe o emoji com base no tipo do animal
        if tipo == "Cachorro":
            icone = "🐶"
        else:
            icone = "😺"


        # ========================
        # CRIA O DICIONÁRIO DO PET
        # ========================

        # Monta um dicionário com todos os dados do formulário
        # Mesmo formato dos pets já existentes em dados/pets.py
        pet = {
            "nome":      nome,
            "tipo":      tipo,
            "icone":     icone,
            "status":    status,   # "Perdido" ou "Encontrado" — veio como parâmetro
            "cor":       cor,
            "raca":      raca,
            "bairro":    bairro,
            "descricao": descricao
        }

        # ========================
        # ADICIONA À LISTA
        # ========================

        # pets.append(pet) adiciona o novo dicionário ao final da lista "pets"
        # É o mesmo .append() que você aprendeu com listas em aula!
        pets.append(pet)

        # Exibe o pet cadastrado no terminal (útil para testar/depurar)
        print("PET CADASTRADO:")
        print(pet)


        # ========================
        # VOLTA PARA A TELA INICIAL
        # ========================

        # Recria a tela inicial passando o "root" (janela principal)
        # Isso vai redesenhar todos os cards, incluindo o pet recém cadastrado
        criar_tela_inicio(root)

        # Fecha a janela de cadastro (o popup some)
        janela.destroy()


    # ========================
    # BOTÃO CADASTRAR
    # ========================

    # Botão que, ao ser clicado, chama a função cadastrar_pet definida acima.
    # "command=cadastrar_pet" conecta o clique à função — SEM parênteses,
    # pois não queremos executar agora, só quando clicar.
    Button(
        janela,
        text="Cadastrar",
        bg=AZUL,
        fg="white",
        font=("Arial", 14, "bold"),
        relief="flat",   # Sem borda em relevo (visual mais moderno)
        padx=20,         # Espaço interno horizontal
        pady=10,         # Espaço interno vertical
        command=cadastrar_pet  # Função chamada ao clicar
    ).pack(pady=25)
