# ============================================================
# ARQUIVO: dados/pets.py
# CONCEITOS: variáveis, listas, dicionários
# ============================================================

# Uma LISTA chamada "pets"
# Cada item da lista é um DICIONÁRIO: { 'chave': 'valor' }
pets = [

    {
        'nome':      'Mel',        # variável do tipo string
        'tipo':      'Cachorro',
        'icone':     '🐶',
        'status':    'Perdido',
        'bairro':    'Centro',
        'cor':       'Caramelo',
        'raca':      'Vira-lata',
        'descricao': 'Sumiu perto da praça central. Muito dócil e usa coleira vermelha.'
    },

    {
        'nome':      'Pipoca',
        'tipo':      'Gato',
        'icone':     '😺',
        'status':    'Encontrado',
        'bairro':    'Vila Nova',
        'cor':       'Branco e Cinza',
        'raca':      'Persa',
        'descricao': 'Encontrado próximo ao mercado. Muito calmo e parece estar perdido.'
    }

    # Novos pets são adicionados com:  pets.append(novo_dicionario)
    # Acessamos um valor com:          pets[0]['nome']  →  'Mel'
]