# MÓDULO DE COMPARAÇÃO
# Responsável: ______________________
#
# Esta parte será adaptada aos critérios definidos pelo grupo
# para comparar o protótipo com o sistema Alecrim.


def mostrar_resumo():
    print("\n[COMPARAÇÃO] Relatório ainda não implementado.")
    # TODO: apresentar os dados e indicadores escolhidos pelo grupo.


def mostrar_comparacao():
    print("\n[COMPARAÇÃO] Comparação ainda não implementada.")
    # TODO: mostrar semelhanças, diferenças e limitações do protótipo.


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
