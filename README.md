PetFinder
O PetFinder é um projeto simples que nasceu com a ideia de ajudar a mapear e encontrar animais perdidos ou achados na rua. Desenvolvemos o sistema usando Python e o CustomTkinter
A ideia aqui é ter um fluxo rápido: você abre o app, consegue ver os animais que já foram registrados e, se precisar, adiciona um novo pet perdido ou encontrado através de um formulário direto.
---
O que você precisa e como rodar
Para fazer o projeto para funcionar na sua máquina, você só vai precisar do Python instalado.
O único pacote externo que o projeto usa é o customtkinter. Para instalar, abra o terminal e rode:
---

```
pip install customtkinter
```
---
Depois que a instalação terminar, é só entrar na pasta do projeto pelo terminal e puxar o arquivo principal para abrir a interface:
```
python main.py
```
---
O que o app faz
Cadastrar pets perdidos: para registrar um animal que sumiu
Cadastrar pets encontrados: para registrar um animal que encontrou na rua
Mural Inicial: A tela de início do programa, que puxa os dados e monta cards visuais para cada animal cadastrado, facilitando a navegação.
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
|   └── detalhes.py 
│
└── dados/
    └── pets.py          # Lista com os dados dos animais
```
---
Observação

Os dados estão sendo salvos apenas em memória. Se você fechar o programa, tudo o que foi cadastrado será apagado.
