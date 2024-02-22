import pandas as pd
import matplotlib.pyplot as plt

def carregar_dados(arquivo_csv):
    try:
        dados = pd.read_csv(arquivo_csv)
        return dados
    except FileNotFoundError:
        print("O arquivo não foi encontrado.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
        return None

def visualizar_dados(dados):
    if dados is not None:
        print("Visualização das primeiras linhas do conjunto de dados:")
        print(dados.head())

        colunas_numericas = dados.select_dtypes(include=['int', 'float']).columns
        if not colunas_numericas.empty:
            coluna = colunas_numericas[0]
            plt.figure(figsize=(8, 6))
            plt.hist(dados[coluna], bins=20, color='skyblue', edgecolor='black')
            plt.xlabel(coluna)
            plt.ylabel('Frequência')
            plt.title(f'Histograma de {coluna}')
            plt.grid(True)
            plt.show()
        else:
            print("Não há colunas numéricas para plotar histograma.")

def main():
    print("Bem-vindo ao programa de análise e visualização de dados para o seu TCC!")
    arquivo_csv = input("Digite o caminho do arquivo CSV contendo os dados: ").strip()

    dados = carregar_dados(arquivo_csv)
    if dados is not None:
        visualizar_dados(dados)

if __name__ == "__main__":
    main()