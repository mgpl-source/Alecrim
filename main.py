from produtores import menu_produtores
from laboratorios import menu_laboratorios
from editais import menu_editais
from comparacao import menu_comparacao


def menu_principal():
    while True:
        print("\n" + "=" * 42)
        print("             SISTEMA ALECRIM")
        print("=" * 42)
        print("1 - Produtores")
        print("2 - Laboratórios")
        print("3 - Editais")
        print("4 - Comparação e relatórios")
        print("0 - Sair")
        print("=" * 42)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            menu_produtores()
        elif opcao == "2":
            menu_laboratorios()
        elif opcao == "3":
            menu_editais()
        elif opcao == "4":
            menu_comparacao()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()
