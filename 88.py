import pyrebase
import os
from colorama import init, Fore

# Inicializa o colorama
init(autoreset=True)

# Configuração do Firebase
firebase_config = {
    "apiKey": "AIzaSyDctAPkUDUhR7xsVdnoheWStquekVOuWDM",
    "authDomain": "shit-10f15.firebaseapp.com",
    "databaseURL": "https://shit-10f15-default-rtdb.firebaseio.com/",
    "projectId": "shit-10f15",
    "storageBucket": "shit-10f15.appspot.com",
    "messagingSenderId": "1087100999816",
    "appId": "1:1087100999816:web:57ea5780357e99be06e73d",
    "measurementId": "G-MCFG8C05LY"
}

# Inicializando a aplicação Firebase
firebase = pyrebase.initialize_app(firebase_config)
auth = firebase.auth()
db = firebase.database()

# Função para fazer login automaticamente
def login():
    username = "sistema"
    email = f"{username}@gmail.com"
    password = "sistema"
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(Fore.GREEN + "Sistema iniciado com sucesso!")
        return user
    except Exception as e:
        print(Fore.RED + f"Erro ao iniciar o sistema: {e}")
        return None

# Função para criar um novo usuário apenas no banco de dados
def criar_usuario():
    username = input(Fore.CYAN + "Digite o novo usuário: ")
    password = input(Fore.CYAN + "Senha do novo usuário: ")
    try:
        user_data = {"username": username, "password": password}
        db.child("users").push(user_data)
        print(Fore.GREEN + "Usuário criado com sucesso no banco de dados!")
    except Exception as e:
        print(Fore.RED + f"Erro ao criar usuário no banco de dados: {e}")

# Função para listar todos os dados (usuários e avisos)
def listar_dados():
    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir_banner()
            print(Fore.MAGENTA + "Listagem de Dados")
            print(Fore.MAGENTA + "Escolha uma opção:")
            print(Fore.MAGENTA + "1 - Usuários")
            print(Fore.MAGENTA + "2 - Avisos")
            print(Fore.MAGENTA + "3 - Voltar ao Menu Principal")
            opcao = input(Fore.CYAN + "Opção: ")
            if opcao == '1':
                listar_usuarios()
            elif opcao == '2':
                listar_avisos()
            elif opcao == '3':
                break
            else:
                print(Fore.RED + "Opção inválida, tente novamente.")
                input(Fore.CYAN + "Pressione 'Enter' para continuar.")
    except KeyboardInterrupt:
        pass

# Função para listar todos os usuários com opção de deletar
def listar_usuarios():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_banner()
        print(Fore.MAGENTA + "Listagem de Usuários")
        usuarios = db.child("users").get()
        if usuarios.each():
            index = 100
            for user in usuarios.each():
                print(Fore.YELLOW + f"{index} - {user.key()}: {user.val()}")
                index += 1
        else:
            print(Fore.YELLOW + "Nenhum usuário encontrado.")
        print(Fore.MAGENTA + "\nPressione 'Enter' para voltar.")
        input()
    except Exception as e:
        print(Fore.RED + f"Erro ao listar usuários: {e}")
        input(Fore.CYAN + "Pressione 'Enter' para continuar.")

# Função para listar todos os avisos
def listar_avisos():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_banner()
        print(Fore.MAGENTA + "Listagem de Avisos")
        avisos = db.child("config").child("aviso").get().val()
        if avisos:
            print(Fore.YELLOW + "Aviso: " + avisos)
        else:
            print(Fore.YELLOW + "Nenhum aviso encontrado.")
        print(Fore.MAGENTA + "\nPressione 'Enter' para voltar.")
        input()
    except Exception as e:
        print(Fore.RED + f"Erro ao listar avisos: {e}")
        input(Fore.CYAN + "Pressione 'Enter' para continuar.")

# Função para atualizar o aviso no banco de dados
def atualizar_aviso():
    aviso = input(Fore.CYAN + "Digite o novo aviso: ")
    try:
        db.child("config").child("aviso").set(aviso)
        print(Fore.GREEN + "Aviso atualizado com sucesso!")
    except Exception as e:
        print(Fore.RED + f"Erro ao atualizar aviso: {e}")

# Função para deletar o aviso do banco de dados
def deletar_aviso():
    try:
        db.child("config").child("aviso").remove()
        print(Fore.GREEN + "Aviso deletado com sucesso!")
    except Exception as e:
        print(Fore.RED + f"Erro ao deletar aviso: {e}")
    input(Fore.MAGENTA + "\nPressione 'Enter' para continuar.")

# Função para exibir o banner
def exibir_banner():
    banner = """
     _______   __                __   ________  ________  
    /       \ /  |              /  | /        |/        | 
    $$$$$$$  |$$ |  _______  ____$$ | $$$$$$$$/ $$$$$$$$/  
    $$ |__$$ |$$ | /       |/    $$ | $$ |__    $$ |__    
    $$    $$/ $$ |/$$$$$$$/ $$$$$$$ | $$    |   $$    |   
    $$$$$$$/  $$ |$$ |      $$ |  $$ | $$$$$/    $$$$$/    
    $$ |      $$ |$$ \_____ $$ \__$$ | $$ |_____ $$ |_____ 
    $$ |      $$ |$$       |$$    $$ | $$       |$$       |
    $$/       $$/  $$$$$$$/  $$$$$$$/  $$$$$$$$/ $$$$$$$$/ 
    """
    print(Fore.GREEN + banner)

# Menu principal
def menu():
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            exibir_banner()
            print(Fore.MAGENTA + "Painel 88")
            print(Fore.MAGENTA + "Escolha uma opção:")
            print(Fore.MAGENTA + "1 - Criar Usuário")
            print(Fore.MAGENTA + "2 - Listar Dados")
            print(Fore.MAGENTA + "3 - Atualizar Aviso")
            print(Fore.MAGENTA + "4 - Deletar Aviso")
            print(Fore.MAGENTA + "5 - Sair")
            opcao = input(Fore.CYAN + "Opção: ")
            if opcao == '1':
                criar_usuario()
            elif opcao == '2':
                listar_dados()
            elif opcao == '3':
                atualizar_aviso()
            elif opcao == '4':
                deletar_aviso()
            elif opcao == '5':
                break
            else:
                print(Fore.RED + "Opção inválida, tente novamente.")
                input(Fore.CYAN + "Pressione 'Enter' para continuar.")
        except KeyboardInterrupt:
            pass

# Executando o login automático e exibindo o menu
if __name__ == "__main__":
    user = login()
    if user:
        menu()
    else:
        print(Fore.RED + "Falha no sistema, encerrando o programa.")
