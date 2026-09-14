txt_nomes = "tres_nomes.txt"
for i in range (3):
    nomes = input ("seu nome: ")
    with open(txt_nomes, "a") as arquivo:
        arquivo.write(f"{nomes}\n")  