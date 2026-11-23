
def cadastrar_edital():
    print("\n[EDITAIS] Cadastro ainda não implementado.")
    # pedir os dados do edital e salvar o cadastro.


def listar_editais():
    print("\n[EDITAIS] Listagem ainda não implementada.")
    # mostrar todos os editais cadastrados.


def editar_edital():
    print("\n[EDITAIS] Edição ainda não implementada.")
    # localizar um edital e alterar seus dados.


def excluir_edital():
    print("\n[EDITAIS] Exclusão ainda não implementada.")
    # localizar um edital e excluir seu cadastro.


def menu_editais():
    while True:
        print("\n--- MENU DE EDITAIS ---")
        print("1 - Cadastrar edital")
        print("2 - Listar editais")
        print("3 - Editar edital")
        print("4 - Excluir edital")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_edital()
        elif opcao == "2":
            listar_editais()
        elif opcao == "3":
            editar_edital()
        elif opcao == "4":
            excluir_edital()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
