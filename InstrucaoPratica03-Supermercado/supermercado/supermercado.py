class Supermercado:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, codigo, nome, preco):
        produto = {"codigo": codigo, "nome": nome, "preco": preco}
        self.produtos.append(produto)

    def excluir_produto(self, codigo):
        self.produtos = [produto for produto in self.produtos if produto["codigo"] != codigo]

    def listar_produtos(self):
        for produto in self.produtos:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

    def consultar_preco(self, codigo):
        for produto in self.produtos:
            if produto["codigo"] == codigo:
                return produto["preco"]
        return None

    def listar_produtos_paginados(self, pagina):
        produtos_pagina = self.produtos[pagina * 10:(pagina + 1) * 10]
        for produto in produtos_pagina:
            print(f"Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")
