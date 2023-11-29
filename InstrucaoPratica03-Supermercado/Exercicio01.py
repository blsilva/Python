class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco


class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} inserido com sucesso!")

    def excluir_produto(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                self.produtos.remove(produto)
                print(f"Produto {produto.nome} removido com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R${produto.preco:.2f}")

    def consultar_preco(self, codigo):
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(f"O preço do produto {produto.nome} é R${produto.preco:.2f}")
                return
        print("Produto não encontrado.")

    def listar_produtos_paginados(self, pagina):
        inicio = (pagina - 1) * 10
        fim = inicio + 10
        produtos_paginados = sorted(self.produtos, key=lambda x: x.preco)[inicio:fim]

        for produto in produtos_paginados:
            print(f"Código: {produto.codigo} | Nome: {produto.nome} | Preço: R${produto.preco:.2f}")


def main():
    supermercado = Supermercado()

    while True:
        print("\nMenu:")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto por código")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            codigo = input("Digite o código do produto: ")
            nome = input("Digite o nome do produto: ").capitalize()
            preco = float(input("Digite o preço do produto: "))
            produto = Produto(codigo, nome, preco)
            supermercado.inserir_produto(produto)

        elif opcao == '2':
            codigo = input("Digite o código do produto a ser excluído: ")
            supermercado.excluir_produto(codigo)

        elif opcao == '3':
            pagina = int(input("Digite o número da página: "))
            supermercado.listar_produtos_paginados(pagina)

        elif opcao == '4':
            codigo = input("Digite o código do produto: ")
            supermercado.consultar_preco(codigo)

        elif opcao == '5':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
