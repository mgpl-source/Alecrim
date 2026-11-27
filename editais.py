editais = {}
contador_id = 1 

def cadastrar_edital():
    global contador_id

    # pedir os dados do edital e salvar o cadastro.
    print("\n=== CADASTRO DE EDITAL ===")
    nome = input("Nome do edital: ")
    instituicao = input("Instituição responsável: ")
    prazo = input("Prazo de inscrição: ")
    valor = input("Valor do edital: ")
    
    editais[contador_id] = {"nome": nome, "instituicao": instituicao, "prazo": prazo, "valor": valor}
    contador_id += 1
    print("\nEdital cadastrado com sucesso!")

# mostrar todos os editais cadastrados.
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
    
# localizar um edital e alterar seus dados.
def editar_edital():
    print("\n=== EDITAR EDITAL ===")
    
    id_edital = int(input("Digite o ID do edital que deseja editar: "))
                    
    if id_edital not in editais:
        print("edital não encontrado")
        return
                    
    else:
        dados = editais[id_edital]

        print("\nDados atuais do edital: ")
        print(f"Nome: {dados['nome']}")
        print(f"Instituição: {dados['instituicao']}")
        print(f"Prazo: {dados['prazo']}")
        print(f"Valor: R$ {dados['valor']}")

        print("\nDigite os novos dados ou pressione Enter para manter o atual.")

        nome = input("Novo nome: ")
        instituicao = input("Nova instituição: ")
        prazo = input("Novo prazo: ")
        valor = input("Novo valor: ")

        if nome:
            dados["nome"] = nome

        if instituicao:
            dados["instituicao"] = instituicao

        if prazo:
            dados["prazo"] = prazo

        if valor:
            dados["valor"] = valor

        print("\nEdital atualizado com sucesso!")

# localizar um edital e excluir seu cadastro.
def excluir_edital():
    print("\n=== EXCLUIR EDITAL ===")

    id_edital = int(input("Digite o Id do edital que deseja excluir: "))

    if id_edital not in editais:
        print("Edital não encontrado")
        return
    else:
        del editais[id_edital]

    print("\nEdital excluído com sucesso!")


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
