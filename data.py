import sqlite3

def titulo (n, s):
    print("="*n)
    print(f'{s}'.center(n))
    print("="*n)

def mensagem(a):
    print(f"Item {a} cadastrado com sucesso")

path = r"/home/romulo/Documentos/SQL/Perfumes"
perfumedb = sqlite3.connect(path + r"/dbperfume.db")
cursor =perfumedb.cursor()

#Inserir dados
titulo(40, "MENU")
escolha = ''
while escolha not in ('S', 'N'):
    escolha = input("Cadastrar algum item? [S/N] ").upper()
if escolha == 'S':
    while True:
        escolha = ''
        while escolha not in ('1', '2', '3', '4', '5'):
            print ("\n1 - Marcas  2 - Fixações 3 - Perfumes 4 - Volumes 5 - Essencias\n")
            escolha = input ("O que deseja cadastrar?  ")
            if escolha == '1':
                id = int(input('Informe o ultimo Id: '))
                id +=1
                nome = input('Insira o nome da marca: ')
                cursor.execute(f"INSERT INTO Marcas VALUES({id}, '{nome}')")
                perfumedb.commit()
                mensagem(nome)
            elif escolha == '2':
                id = int(input('Informe o ultimo Id: '))
                id +=1
                nome = input('Insira o nome da fixação: ')
                cursor.execute(f"INSERT INTO Fixacoes VALUES({id}, '{nome}')")
                perfumedb.commit()
                mensagem(nome)
            elif escolha == '3':
                id = int(input('Informe o ultimo Id: '))
                id +=1
                nome = input('Insira o nome do perfume: ')
                quant = int(input("Informe a quantidade: "))
                idVol = int(input("Informe o id Volume: "))
                idMarca = int(input("Informe o id Marca: "))
                idFix = int(input("Informe o id Fixação: "))
                cursor.execute(f"INSERT INTO Perfumes VALUES({id}, '{nome}', {quant}, {idVol}, {idMarca}, {idFix})")
                perfumedb.commit()
                mensagem(nome)
                mensagem(quant)
            elif escolha == '4':
                id = int(input('Informe o ultimo Id: '))
                id +=1
                nome = input('Insira o nome do volume: ')
                cursor.execute(f"INSERT INTO Volumes VALUES({id}, '{nome}')")
                perfumedb.commit()
                mensagem(nome)
            elif escolha == '5':
                id = int(input('Informe o ultimo Id: '))
                id +=1 
                nome = input('Insira o nome da essência: ')
                cursor.execute(f"INSERT INTO Essencias VALUES({id}, '{nome}')")
                perfumedb.commit()
                mensagem(nome)
        escolha = ''
        while escolha not in ('S', 'N'):
            escolha = input("Cadastrar algum item? [S/N] ").upper()
        if escolha == 'N':
            print ("Obrigado. Até a próxima")
            break
else:
    print ("Obrigado. Até a próxima")