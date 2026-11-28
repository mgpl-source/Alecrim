import json

def carregar_dados():
    try:

        with open("laboratorios.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:

        dados = {
            "ultimo_codigo": 0,
            "laboratorios": {}
        }

    return dados

def salvar_dados(dados):

    with open("laboratorios.json", "w", encoding="UTF-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def gerar_codigo(dados):

    dados["ultimo_codigo"] += 1

    numero = dados["ultimo_codigo"]

    codigo = f"LAB{numero:03d}"

    return codigo
    
def cadastrar_laboratorio(dados):

    print( "\n Cadastro de Laboratórios \n")

    rzsocial = input("Digite a Razão Social: ")
    cnpj = int(input("Digite o CNPJ do laboratório: "))
    responsavel = input("Digite o Nome do Resposável pelo CNPJ: ")
    cpf_responsavel = input("Digite o CPF do responsável do CPNJ: ")
    telefone = input("Digite um Telefone de Contato: ")

    codigo = gerar_codigo(dados)

    dados["laboratorios"][codigo] = {
        "razao_social": rzsocial,
        "cnpj": cnpj,
        "responsavel": responsavel,
        "cpf": cpf_responsavel,
        "telefone": telefone
    }

    salvar_dados(dados)

    print("-" * 30)
    print("LABORATÓRIOS CASDASTRADO!")
    print(f"Código: {codigo}")

def listar_laboratorios(dados):
    print("\nLista de Laboratórios ")

    if len(dados["laboratorios"]) == 0:
        print("Nenhum Laboratório Cadastrado!")

    else:
        for chave, valor in dados["laboratorios"].items():

            print(f"Código: {chave}")
            print(f"Razão Social: {valor['nome']}")
            print(f"CNPJ: {valor['cnpj']}")
            print(f"Responsável: {valor['responsavel']}")
            print(f"Telefone para contato: {valor['telefone']}")
            print("-" * 10)

def editar_laboratorio(dados):
    print("\n Editar laboratório ")

    # Lê a lista de laboratórios salva no arquivo
    with open("dados/laboratorios.json", "r", encoding="utf-8") as arquivo:
        laboratorios = json.load(arquivo)

    nome = input("Nome do laboratório a editar: ").strip()

    # Procura o laboratório pelo nome
    for laboratorio in laboratorios:
        if laboratorio["nome"].lower() == nome.lower():
            print("Deixe em branco para manter o valor atual.")

            # Pede um novo valor para cada dado do laboratório (nome, cidade...)
            for dado in laboratorio:
                novo_valor = input(f"{dado} ({laboratorio[dado]}): ").strip()
                if novo_valor != "":
                    laboratorio[dado] = novo_valor

            salvar_dados(dados)

            print("Laboratório editado com sucesso!")
            return

    print("Laboratório não encontrado.")

def excluir_laboratorio(dados):
    print("\nExcluir Laboratório ")

    nome = input("Nome do laboratório a excluir: ").strip()

    # Procura o laboratório pelo nome e remove da lista
    for laboratorio in laboratorio:
        if laboratorio["nome"].lower() == nome.lower():
            laboratorio.remove(laboratorio)

            salvar_dados(dados)

            print("Laboratório excluído com sucesso!")
            return

    print("Laboratório não encontrado.")


def menu_laboratorios(dados):

    while True:
        print("\n--- MENU DE LABORATÓRIOS ---")
        print("1 - Cadastrar laboratório")
        print("2 - Listar laboratórios")
        print("3 - Editar laboratório")
        print("4 - Excluir laboratório")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_laboratorio(dados)
        elif opcao == "2":
            listar_laboratorios(dados)
        elif opcao == "3":
            editar_laboratorio(dados)
        elif opcao == "4":
            excluir_laboratorio(dados)
        elif opcao == "0":
            print("\nSistema Encerrado!\n")
            break
        else:
            print("Opção inválida.")
