def criar_lista_de_compras():
    print("Bem-vindo à sua lista de compras!")
    lista_de_compras = []

    while True:
        item = input("Digite o nome do item que deseja adicionar à lista (ou 'sair' para encerrar): ").strip().lower()

        if item == 'sair':
            break

        if item:
            lista_de_compras.append(item)
            print(f"'{item}' foi adicionado à sua lista de compras.")

    return lista_de_compras

def exibir_lista_de_compras(lista):
    print("\nSua lista de compras:")
    for index, item in enumerate(lista, start=1):
        print(f"{index}. {item}")
    print()

def main():
    lista_de_compras = criar_lista_de_compras()
    exibir_lista_de_compras(lista_de_compras)

if __name__ == "__main__":
    main()