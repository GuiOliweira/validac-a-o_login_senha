import mysql.connector

# Função para conectar ao banco de dados


def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="admin123",
        database="validar_login"
    )

# Função do menu de opções


def menu():
    while True:
        print("1- Criar Login\n2- Entrar\n3- Sair\n")
        escolha_user = input("Escolha uma das opções: ")
        if escolha_user == "1":
            print("-"*40)
            criar_login()
            break
        elif escolha_user == "2":
            print("-"*40)
            main()
            break
        elif escolha_user == "3":
            print("Saindo...")
            break
        else:
            print("\nOpção inválida, tente novamente...\n")

# Função para criar usuário e senha


def criar_login():
    connection = conectar_bd()
    cursor = connection.cursor()

    usuario = input("Digite o nome de usuário que deseja criar: ")
    senha = input("Digite a senha que deseja criar: ")

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cursor.execute(query, (usuario, senha))
    connection.commit()

    cursor.close()
    connection.close()

    print("\nUsuário criado com sucesso!\n")
    main()

# Função para validar login


def validar_login(usuario, senha):
    connection = conectar_bd()
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (usuario, senha))

    result = cursor.fetchone()
    cursor.close()
    connection.close()

    if result:
        return True
    else:
        return False

# Função principal


def main():
    while True:
        usuario = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        break

    if validar_login(usuario, senha):
        print("\nLogin bem-sucedido!\n")
        menu()

    while True:
        print("\nNome de usuário ou senha incorretos.\n")
        nova_tentativa_user = input(
            "Deseja tentar novamente?  S/N    : ").upper().split()[0]
        if nova_tentativa_user == "S":
            print("-"*40)
            main()
            break
        elif nova_tentativa_user == "N":
            print("-"*40)
            menu()
        else:
            print("\nOpção inválida, tente novamente...\n")


if __name__ == "__main__":
    menu()
