txt_nomes = "tres_nomes.txt"
with open(txt_nomes, "r") as arquivo:
    linha = arquivo.readline()
    print(f"1:{linha}")
    linha = arquivo.readline()
    print(f"2:{linha}")
    linha = arquivo.readline()
    print(f"3:{linha}")