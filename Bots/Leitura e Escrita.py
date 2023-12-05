#Exeplo de leitura de arquivo
with open("document.txt") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

#Exemplo de escrita de arquivo
with open("document.txt", "w") as arquivo:
    conteudo = arquivo
    conteudo_novo = arquivo + "Olá pessoal!!!"
    arquivo.write(conteudo_novo)
    print(arquivo)
