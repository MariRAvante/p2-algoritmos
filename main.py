# ARQUIVO: main.py
# ============================================================
 
import customtkinter as ctk
from telas.inicio import criar_tela_inicio
from dados.pets import pets
 

 
print("=== PETFINDER INICIADO ===")
print(f"Pets cadastrados no momento: {len(pets)}")
print()
 
for pet in pets:
    # Acesso ao dicionário pela chave: pet['nome']
    print(f"  {pet['icone']}  {pet['nome']} ({pet['tipo']}) — {pet['status']} — {pet['bairro']}")
 
print()
 
# --- JANELA PRINCIPAL (tkinter) ---
root = ctk.CTk()
root.title("PetFinder")
root.geometry("1000x700")
root.configure(bg="#f5f5f5")
 
criar_tela_inicio(root)
root.mainloop()