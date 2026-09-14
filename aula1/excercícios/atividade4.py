notas = "notas.txt"
while True:
    seu_nome = input("digite seu nome (digite sair para terminar): ").lower()
    if seu_nome == "sair":
        break
    sua_nota = int (input("digite sua nota: "))
    with open (notas, "a") as arquivo:
        arquivo.write (f" {seu_nome} = {sua_nota}\n")
