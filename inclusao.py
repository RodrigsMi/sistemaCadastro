from incrementar import incrementar

def incluir(bd):
    print("Cadastro de Produto: ")
    nome=input("Digite o Nome do Produto: ")
    qt=input("Digite a Quantidade do Produto: ")
    preco=input("Digite o Preço do Produto (. -> decimal): ")
    qtMin=input("Digite Quantidade Mínima de Segurança: ")
    
    bd[incrementar(bd)] = [nome, qt, preco, qtMin]
    p = input("Pressione qualquer tecla p/ continuar...")