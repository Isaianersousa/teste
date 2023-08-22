




listaclientes = []

while True:

    nome = input("Digite o nome do cliente:")

    if nome.lower() == "Sair":
        print("Você está saindo...")
        break
    else:
        listaclientes.append(nome.capitalize())
listaclientes.sort()

for cliente in listaclientes:
    print(cliente)

for i in range(len(listacliente)):
    print(i, listaclietes[i])

for i, clinte in enumerate(listaclientes):
    print(i, cliente[i])