#Projeto: Sistema de Livros Clássicos com Resumos e Monitoramento de Acessos

#Tecnologias utilizadas: Python puro (sem frameworks externos), persistência via arquivos JSON (simulando banco de dados CRUD)

import json 
import os
from datetime import datetime

#Caminhos para os arquivos simulando banco de dados

LIVROS_PATH = 'livros.json'
ACESSOS_PATH = 'acessos.json'

#--------------------- Funções CRUD ---------------------

def carregar_dados(caminho):
    if not os.path.exists(caminho):
        with open(caminho, 'w') as f:
            json.dump({}, f)
    with open(caminho, 'r') as f:
        return json.load(f)

def salvar_dados(caminho, dados):
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=4)

#CRUD de Livros

def criar_livro(titulo, resumo):
    livros = carregar_dados(LIVROS_PATH) 
    livros[titulo] = resumo
    salvar_dados(LIVROS_PATH, livros)
    print(f"Livro '{titulo}' adicionado com sucesso.")

def ler_livro(titulo):
     livros = carregar_dados(LIVROS_PATH)
     if titulo in livros:
         registrar_acesso(titulo)
         return livros[titulo]
         return "Livro não encontrado."

def atualizar_livro(titulo, novo_resumo):
    livros = carregar_dados(LIVROS_PATH)
    if titulo in livros:
        livros[titulo] = novo_resumo
        salvar_dados(LIVROS_PATH, livros)
        print(f"Resumo do livro '{titulo}' atualizado.")
    else:
            print("Livro não encontrado.")

def deletar_livro(titulo):
    livros = carregar_dados(LIVROS_PATH)
    if titulo in livros:
        del livros[titulo]
        salvar_dados(LIVROS_PATH, livros)
        print(f"Livro '{titulo}' removido.")
    else:
        print("Livro não encontrado.")

#Registro de acessos

def registrar_acesso(titulo):
    acessos = carregar_dados(ACESSOS_PATH)
    data = datetime.now().isoformat()
    if titulo not in acessos:
        acessos[titulo] = []
    acessos[titulo].append(data)
    salvar_dados(ACESSOS_PATH, acessos)

#Visualizar estatísticas de acesso

def visualizar_acessos():
    acessos = carregar_dados(ACESSOS_PATH)
    for titulo, datas in acessos.items():
        print(f"Livro: {titulo} - Total de acessos: {len(datas)}")

#--------------------- Interface de Usuário ---------------------

def menu():
    while True:
        print("\n--- Sistema de Livros Clássicos ---")
        print("1. Adicionar Livro")
        print("2. Ler Livro")
        print("3. Atualizar Livro")
        print("4. Deletar Livro")
        print("5. Ver Estatisticas Ao Acesso")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Titulo do livro:")
            resumo = input("Resumo do livro:")
            criar_livro(titulo, resumo)

        elif escolha == '2':
            titulo +input("Titulo do livro a ler: ")
            print(ler_livro(titulo))

        elif escolha == '3':
            titulo +input("Titulo do livro a atualizar: ")
            novo_resumo = input("Novo resumo: ")
            atualizar_livro(titulo< novo_resumo)

        elif escolha == '4':
            titulo +input("Titulo do livro a deletar: ")
            deletar_livro(titulo)

        elif escolha == '5':
            visualizar_acessos()

        elif escolha == '6':
            print("Encerrando sistema...")
            break
        else:
            print("Opção invalida, Tente novamente.")

# Executar o menu se este arquivo for executado diretamente
if __name__ == '__main__':
    menu()
    



        