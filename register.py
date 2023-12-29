import os
from time import sleep
from receive_data import *

def ImprimeOpcoes():
    print("1 - Cadastrar novo usuário.")
    print("2 - Remover usuário.")
    print("3 - Listar usuários cadastrados.")
    print("4 - Sair.")


while True:
    # abre um arquivo .json, onde tem as informações sobre os usuários cadastrados
    with open("data_base.json") as file_json:
        data_base = json.load(file_json) # ususario recebe um dicionário correspondente ao conteúdo do .json
    
    #limpando o terminal para estética
    os.system('cls' if os.name == 'nt' else 'clear')
    #lendo o que o usuário deseja fazer
    ImprimeOpcoes()
    acao = int(input("Digite um número:\n"))
    
    if acao == 1:
        new_user = Get_user(data_base["users"])
        if new_user:
            Add_user_data(new_user)
            sleep(2)
        else:
            #limpando o terminal para estética
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n\033[0;31mNão foi possível realizar o cadastro\033[m\n")
            sleep(2)

    elif acao == 2:
        email_remove = input("Digite o email do usuário a ser removido:\n")
        Remove_user_data(email_remove)
        sleep(2)

    elif acao == 3:
        if data_base["quantity"] == 0:
            print("Não há ninguém cadastrado\n")
            
        for c in range(data_base["quantity"]):
            nome = data_base["users"][c]["name"]
            email = data_base["users"][c]["email"]
            print(f"{nome}:{email}")
            sleep(0.5)
        
        acao_stop = input("\nAperte qualquer tecla para sair da listagem:\n")
        
    elif acao == 4:
        break
    
    else:
        print("\n\033[0;31mOpcao invalida\033[m\n")
        sleep(2)