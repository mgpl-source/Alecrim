# MÓDULO DE LABORATÓRIOS
# Responsável: ______________________
#
# Implemente as funções CRUD abaixo.
# Não altere os nomes das funções: o menu principal depende deles.


def cadastrar_laboratorio():
    print("\n[LABORATÓRIOS] Cadastro ainda não implementado.")
    # TODO: pedir os dados do laboratório e salvar o cadastro.


def listar_laboratorios():
    print("\n[LABORATÓRIOS] Listagem ainda não implementada.")
    # TODO: mostrar todos os laboratórios cadastrados.


def editar_laboratorio():
    print("\n[LABORATÓRIOS] Edição ainda não implementada.")
    # TODO: localizar um laboratório e alterar seus dados.


def excluir_laboratorio():
    print("\n[LABORATÓRIOS] Exclusão ainda não implementada.")
    # TODO: localizar um laboratório e excluir seu cadastro.


def menu_laboratorios():
    while True:
        print("\n--- MENU DE LABORATÓRIOS ---")
        print("1 - Cadastrar laboratório")
        print("2 - Listar laboratórios")
        print("3 - Editar laboratório")
        print("4 - Excluir laboratório")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_laboratorio()
        elif opcao == "2":
            listar_laboratorios()
        elif opcao == "3":
            editar_laboratorio()
        elif opcao == "4":
            excluir_laboratorio()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
