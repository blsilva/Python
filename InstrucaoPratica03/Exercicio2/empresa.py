import json

class Empresa:
    def __init__(self, arquivo_dados):
        self.arquivo_dados = arquivo_dados
        self.empregados = self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo_dados, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Arquivo '{self.arquivo_dados}' não encontrado. Criando uma lista vazia.")
            return []

    def salvar_dados(self):
        with open(self.arquivo_dados, 'w') as file:
            json.dump(self.empregados, file, indent=2)

    def reajusta_dez_porcento(self):
        for empregado in self.empregados:
            empregado['salario'] *= 1.1 

    def listar_empregados(self):
        for empregado in self.empregados:
            print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, "
                  f"Ano de Nascimento: {empregado['ano_nascimento']}, "
                  f"RG: {empregado['rg']}, "
                  f"Ano de Admissão: {empregado['ano_admissao']}, "
                  f"Salário: R${empregado['salario']:.2f}")
