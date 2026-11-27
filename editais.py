editais = {}
contador_id = 1 

def cadastrar_edital():
    global contador_id
    
    print("\n=== CADASTRO DE EDITAL ===")
    nome = input("Nome do edital: ")
    instituicao = input("Instituição responsável: ")
    prazo = input("Prazo de inscrição: ")
    valor = float(input("Valor do edital: "))
    
    editais[contador_id] = {"nome": nome, "instituicao": instituicao, "prazo": prazo, "valor": valor}
    contador_id += 1
    print("\nEdital cadastrado com sucesso!")
    # pedir os dados do edital e salvar o cadastro.


def listar_editais():
    print("\n=== EDITAIS CADASTRADOS ===")
    if not editais:
        print("Nenhum edital cadastrado")
        return
    for id_edital, dados in editais.items(): 
        print(f"\nID: {id_edital}")
        print(f"Nome: {dados['nome']}")
        print(f"Instituição: {dados['instituicao']}")
        print(f"Prazo: {dados['prazo']}")
        print(f"Valor: R$ {dados['valor']}")
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
