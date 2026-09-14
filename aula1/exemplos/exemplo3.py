nome_do_arquivo = "exemplo.txt"
with open(nome_do_arquivo, "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)