
def cadastrar_produtor():
    print("\n[PRODUTORES] Cadastro ainda não implementado.")
    # pedir os dados do produtor e salvar o cadastro.


def listar_produtores():
    print("\n[PRODUTORES] Listagem ainda não implementada.")
    # mostrar todos os produtores cadastrados.


def editar_produtor():
    print("\n[PRODUTORES] Edição ainda não implementada.")
    # localizar um produtor e alterar seus dados.


def excluir_produtor():
    print("\n[PRODUTORES] Exclusão ainda não implementada.")
    # localizar um produtor e excluir seu cadastro.


def menu_produtores():
    while True:
        print("\n--- MENU DE PRODUTORES ---")
        print("1 - Cadastrar produtor")
        print("2 - Listar produtores")
        print("3 - Editar produtor")
        print("4 - Excluir produtor")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_produtor()
        elif opcao == "2":
            listar_produtores()
        elif opcao == "3":
            editar_produtor()
        elif opcao == "4":
            excluir_produtor()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
