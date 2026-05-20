PetFinder
Sistema para registrar e localizar animais perdidos ou encontrados, desenvolvido em Python com interface gráfica.
---
Requisitos
Python 3.10 ou superior
customtkinter
---
Instalação
1. Clone ou baixe o projeto
2. Instale a dependência:
```
pip install customtkinter
```
---
Como rodar

Dentro da pasta do projeto, execute:
```
python main.py
```
---
Funcionalidades
Registrar pet perdido
Registrar pet encontrado
Visualizar animais cadastrados na tela inicial
---
Estrutura do projeto
```
petfinder/
│
├── main.py              # Ponto de entrada — inicia a janela
│
├── telas/
│   ├── inicio.py        # Tela principal com os cards de pets
│   └── cadastro.py      # Formulário de cadastro de pet
│
└── dados/
    └── pets.py          # Lista com os dados dos animais
```
---
Observação
Os dados são armazenados em memória enquanto o programa está aberto. Ao fechar, os cadastros feitos durante a sessão são perdidos.
