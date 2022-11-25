def listar(d:dict):
    print('*' * 30)
    print("Listando dados...")
    print('*' * 30)
    for k in d:
        print(f"{d[k][0]} - {d[k][1]} - R${d[k][2]} - {d[k][3]}")
    p = input("Pressione qualquer tecla p/ continuar...")