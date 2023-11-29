from supermercado.supermercado import Supermercado

def menu():
    print("1. Inserir um novo produto")
    print("2. Excluir um produto cadastrado")
    print("3. Listar todos os produtos")
    print("4. Consultar o preço de um produto")
    print("0. Sair")

def main():
    supermercado = Supermercado()

    while True:
        menu()
        opcao = input("Escolha uma opção (0-4): ")

        if opcao == "1":
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            supermercado.inserir_produto(codigo, nome, preco)

        elif opcao == "2":
            codigo = input("Digite o código do produto a ser excluído: ")
            supermercado.excluir_produto(codigo)

        elif opcao == "3":
            supermercado.listar_produtos()

        elif opcao == "4":
            codigo = input("Digite o código do produto a ser consultado: ")
            preco = supermercado.consultar_preco(codigo)
            if preco is not None:
                print(f"O preço do produto com código {codigo} é R${preco:.2f}")
            else:
                print(f"Produto com código {codigo} não encontrado.")

        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
