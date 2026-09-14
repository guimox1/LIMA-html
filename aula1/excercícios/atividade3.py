txt_nomes = "tres_nomes.txt"
with open(txt_nomes, "r") as arquivo:
    conteudo = arquivo.read()

copia = "copia.txt"
with open(copia, "w") as arquivo:
    arquivo.write(conteudo)