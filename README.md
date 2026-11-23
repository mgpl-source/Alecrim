# Sistema Alecrim — Projeto-base

Protótipo acadêmico em Python, executado pelo terminal, para a disciplina de Fundamentos da Programação.

## Objetivo

Criar uma representação simplificada de funcionalidades relacionadas a:

- Produtores
- Laboratórios
- Editais
- Comparação e relatórios

Este repositório é um **esqueleto de projeto**: os menus e a integração já estão prontos. Cada integrante deve implementar a lógica das funções do seu módulo.

## Como executar

É necessário ter Python 3 instalado.

No terminal, dentro da pasta do projeto:

```bash
python3 main.py
```

Não é necessário instalar bibliotecas externas.

## Organização dos arquivos

```text
alecrim/
├── main.py
├── produtores.py
├── laboratorios.py
├── editais.py
├── comparacao.py
├── dados/
└── README.md
```

- `main.py`: menu principal e integração dos módulos.
- `produtores.py`: menu e funções de produtores.
- `laboratorios.py`: menu e funções de laboratórios.
- `editais.py`: menu e funções de editais.
- `comparacao.py`: relatórios e comparação.
- `dados/`: local reservado para os arquivos de dados, caso o grupo opte por salvar informações em JSON.

## Divisão sugerida

| Parte | Responsabilidade |
|---|---|
| Produtores | Implementar cadastro, listagem, edição e exclusão |
| Laboratórios | Implementar cadastro, listagem, edição e exclusão |
| Editais | Implementar cadastro, listagem, edição e exclusão |
| Comparação | Implementar resumo e comparação |
| Integração | Testar os módulos e resolver problemas de integração |

## Contrato entre os arquivos

**Não renomeie as funções abaixo**, pois o `main.py` e os menus já chamam esses nomes.

### produtores.py
- `cadastrar_produtor()`
- `listar_produtores()`
- `editar_produtor()`
- `excluir_produtor()`
- `menu_produtores()`

### laboratorios.py
- `cadastrar_laboratorio()`
- `listar_laboratorios()`
- `editar_laboratorio()`
- `excluir_laboratorio()`
- `menu_laboratorios()`

### editais.py
- `cadastrar_edital()`
- `listar_editais()`
- `editar_edital()`
- `excluir_edital()`
- `menu_editais()`

### comparacao.py
- `mostrar_resumo()`
- `mostrar_comparacao()`
- `menu_comparacao()`

## O que é CRUD?

- **Create:** criar/cadastrar um registro.
- **Read:** ler/listar/consultar registros.
- **Update:** atualizar/editar um registro.
- **Delete:** excluir um registro.

## Regras simples para trabalhar em equipe

1. Cada integrante deve trabalhar principalmente no arquivo da sua parte.
2. Não apague nem renomeie funções que já existem.
3. Antes de integrar, teste seu módulo separadamente.
4. Use nomes de variáveis claros e mantenha o código simples.
5. Combine com o grupo quais campos cada cadastro terá antes de implementar.
6. Use dados fictícios na demonstração.

## Fluxo Git básico

Depois de clonar o repositório:

```bash
git pull
```

Após editar os arquivos:

```bash
git add .
git commit -m "Implementa módulo de produtores"
git push
```

Se várias pessoas forem trabalhar ao mesmo tempo, é melhor cada uma usar uma branch própria e abrir um Pull Request para revisão antes de juntar as alterações.
