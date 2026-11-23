
def mostrar_resumo():
    print("\n[COMPARAÇÃO] Relatório ainda não implementado.")
    # apresentar os dados e indicadores.


def mostrar_comparacao():
    print("\n[COMPARAÇÃO] Comparação ainda não implementada.")
    # mostrar semelhanças, diferenças e limitações do produto.


def menu_comparacao():
    while True:
        print("\n--- COMPARAÇÃO E RELATÓRIOS ---")
        print("1 - Resumo dos cadastros")
        print("2 - Comparar com o Alecrim")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_resumo()
        elif opcao == "2":
            mostrar_comparacao()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
