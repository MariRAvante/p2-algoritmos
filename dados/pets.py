# ============================================================
# ARQUIVO: dados/pets.py
# FUNÇÃO: Armazena a lista de pets cadastrados no sistema.
#         É aqui que ficam os dados que aparecem na tela inicial.
#         Pense nesse arquivo como o nosso "banco de dados" por enquanto.
# ============================================================

# "pets" é uma LISTA (estrutura que você já viu em aula!)
# Cada item da lista é um DICIONÁRIO (parecido com uma lista,
# mas os valores têm um "nome"/chave para identificá-los).
# Formato do dicionário: { 'chave': 'valor', 'chave2': 'valor2' }

pets = [

    # --- PRIMEIRO PET ---
    # Cada bloco entre { } é um dicionário representando um animal.
    # As chaves (nome, tipo, icone...) serão usadas em outros arquivos
    # para exibir as informações na tela.
    {
        'nome': 'Mel',           # Nome do pet (string/texto)
        'tipo': 'Cachorro',      # Tipo do animal
        'icone': '🐶',           # Emoji usado como ícone no card
        'status': 'Perdido',     # Status: 'Perdido' ou 'Encontrado'
        'bairro': 'Centro'       # Bairro onde foi visto/perdido
    },

    # --- SEGUNDO PET ---
    {
        'nome': 'Pipoca',
        'tipo': 'Gato',
        'icone': '😺',
        'status': 'Encontrado',
        'bairro': 'Vila Nova'
    }

    # Quando o usuário cadastra um novo pet pela tela de cadastro,
    # ele é adicionado aqui com pets.append(novo_pet) — veja cadastro.py
]
