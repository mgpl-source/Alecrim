import mysql.connector

ARQUIVO_TXT = "produtores.txt"

CAMPOS = ("nome", "cpf", "cidade")


def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fazenda"
    )


def criar_tabela():
    try:
        con = mysql.connector.connect(host="localhost", user="root", password="sua_senha")
        cursor = con.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS fazenda")
        cursor.execute("USE fazenda")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                cpf VARCHAR(14) NOT NULL,
                cidade VARCHAR(50) NOT NULL
            )
        """)
        con.commit()
        con.close()
    except mysql.connector.Error as erro:
        print("Erro ao preparar o banco:", erro)


def buscar_todos():
    con = conectar()
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, cpf, cidade FROM produtores")
    produtores = cursor.fetchall()
    con.close()
    return produtores


def salvar_txt(produtores):
    with open(ARQUIVO_TXT, "w", encoding="utf-8") as arquivo:
        for p in produtores:
            arquivo.write(f"{p['id']};{p['nome']};{p['cpf']};{p['cidade']}\n")

def cadastrar_produtor():
    print("\n[PRODUTORES] Cadastro")
    try:
        dados = {}
        for campo in CAMPOS:  # repetição sobre a tupla
            valor = input(f"{campo.capitalize()}: ").strip()
            if valor == "":
                print("O campo não pode ficar vazio.")
                return
            dados[campo] = valor

        con = conectar()
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO produtores (nome, cpf, cidade) VALUES (%s, %s, %s)",
            (dados["nome"], dados["cpf"], dados["cidade"])
        )
        con.commit()
        con.close()

        salvar_txt(buscar_todos())
        print("Produtor cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print("Erro no banco de dados:", erro)


def listar_produtores():
    print("\n[PRODUTORES] Listagem")
    try:
        produtores = buscar_todos()
        if len(produtores) == 0:
            print("Nenhum produtor cadastrado.")
            return
        for p in produtores:
            print(f"ID: {p['id']} | Nome: {p['nome']} | CPF: {p['cpf']} | Cidade: {p['cidade']}")
    except mysql.connector.Error as erro:
        print("Erro no banco de dados:", erro)


def editar_produtor():
    print("\n[PRODUTORES] Edição")
    try:
        id_produtor = int(input("ID do produtor a editar: "))

        con = conectar()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtores WHERE id = %s", (id_produtor,))
        produtor = cursor.fetchone()

        if produtor is None:
            print("Produtor não encontrado.")
            con.close()
            return

        print("Deixe em branco para manter o valor atual.")
        for campo in CAMPOS:
            novo = input(f"{campo.capitalize()} ({produtor[campo]}): ").strip()
            if novo != "":
                produtor[campo] = novo

        cursor.execute(
            "UPDATE produtores SET nome = %s, cpf = %s, cidade = %s WHERE id = %s",
            (produtor["nome"], produtor["cpf"], produtor["cidade"], id_produtor)
        )
        con.commit()
        con.close()

        salvar_txt(buscar_todos())
        print("Produtor atualizado com sucesso!")
    except ValueError:
        print("ID inválido. Digite apenas números.")
    except mysql.connector.Error as erro:
        print("Erro no banco de dados:", erro)

def excluir_produtor():
    print("\n[PRODUTORES] Exclusão")
    try:
        id_produtor = int(input("ID do produtor a excluir: "))

        con = conectar()
        cursor = con.cursor()
        cursor.execute("DELETE FROM produtores WHERE id = %s", (id_produtor,))
        con.commit()

        if cursor.rowcount == 0:
            print("Produtor não encontrado.")
        else:
            print("Produtor excluído com sucesso!")
        con.close()

        salvar_txt(buscar_todos())
    except ValueError:
        print("ID inválido. Digite apenas números.")
    except mysql.connector.Error as erro:
        print("Erro no banco de dados:", erro)



def menu_produtores():
    while True:
        print("\n--- MENU DE PRODUTORES ---")
        print("1 - Cadastrar produtor")
        print("2 - Listar produtores")
        print("3 - Editar produtor")
        print("4 - Excluir produtor")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        match opcao:
            case "1":
                cadastrar_produtor()
            case "2":
                listar_produtores()
            case "3":
                editar_produtor()
            case "4":
                excluir_produtor()
            case "0":
                break
            case _:
                print("Opção inválida.")

criar_tabela()
menu_produtores()