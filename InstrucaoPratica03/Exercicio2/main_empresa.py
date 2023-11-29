from empresa import Empresa
import os

def menu():
    print("1. Carregar dados dos empregados")
    print("2. Reajustar salários em 10%")
    print("3. Listar empregados")
    print("0. Sair")

def main():

    caminho_arquivo = os.path.join(os.path.dirname(__file__), 'dados_empregados.json')

    empresa = Empresa(arquivo_dados=caminho_arquivo)

    while True:
        menu()
        opcao = input("Escolha uma opção (0-3): ")

        if opcao == "1":
         
            print(f"Arquivo '{empresa.arquivo_dados}' carregado.")

        elif opcao == "2":
            empresa.reajusta_dez_porcento()
            print("Salários reajustados em 10%.")

        elif opcao == "3":
            empresa.listar_empregados()

        elif opcao == "0":
            empresa.salvar_dados()
            print(f"Dados salvos no arquivo '{empresa.arquivo_dados}'. Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
