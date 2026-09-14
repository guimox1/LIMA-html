nome_do_arquivo = "exemplo.txt"
with open(nome_do_arquivo, "w") as arquivo:
    arquivo.write("primeira\n")
    arquivo.write("Segunda\n")
    arquivo.write("terceira\n")
with open(nome_do_arquivo, "r") as arquivo:
    linha = arquivo.readline()
    print(f"1:{linha}")
    linha = arquivo.readline(5)
    print(f"2:{linha}")
    linha = arquivo.readline(10)
    print(f"3:{linha}")
    linha = arquivo.readline(10)
    print(f"4:{linha}")