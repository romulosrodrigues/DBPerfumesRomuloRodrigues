import sqlite3

def titulo (n, s):
    print("="*n)
    print(f'{s}'.center(n))
    print("="*n)

path = r"/home/romulo/Documentos/SQL/Perfumes"
perfumedb = sqlite3.connect(path + r"/dbperfume.db")
cursor =perfumedb.cursor()

titulo(40,  "MENU")
escolha = ''
while escolha not in ('S', 'N'):
    escolha = input('Excluir um registro? [S/N] ').upper()
if escolha == 'S':
    while True:
        escolha = ''
        while escolha not in ('1', '2', '3', '4', '5'):
            print ("\n1 - Marcas  2 - Fixações 3 - Perfumes 4 - Volumes 5 - Essencias\n")
            escolha = input ("O que deseja excluir?  ")
            if escolha == '1':
                id = int(input('Informe o Id: '))
                try:
                    cursor.execute(f"DELETE FROM Marcas WHERE id = {id}")
                    perfumedb.commit()
                    print(f"Registro nº {id} de Marcas foi excluido com sucesso.")
                except sqlite3.Error as erro:
                    print(f"Não foi possível excluir o registro Nº {id} de Marcas. Codigo de erro: {erro}")
            elif escolha == '2':
                id = int(input('Informe o Id: '))
                try:
                    cursor.execute(f"DELETE FROM Fixacoes WHERE id = {id}")
                    perfumedb.commit()
                    print(f"Registro nº {id} de Fixacoes foi excluido com sucesso.")
                except sqlite3.Error as erro:
                    print(f"Não foi possível excluir o registro Nº {id} de Fixacoes. Codigo de erro: {erro}")
            elif escolha == '3':
                id = int(input('Informe o Id: '))
                try:
                    cursor.execute(f"DELETE FROM Perfumes WHERE id = {id}")
                    perfumedb.commit()
                    print(f"Registro nº {id} de Perfumes foi excluido com sucesso.")
                except sqlite3.Error as erro:
                    print(f"Não foi possível excluir o registro Nº {id} de Perfumes. Codigo de erro: {erro}")
            elif escolha == '4':
                id = int(input('Informe o Id: '))
                try:
                    cursor.execute(f"DELETE FROM Volumes WHERE id = {id}")
                    perfumedb.commit()
                    print(f"Registro nº {id} de Volumes foi excluido com sucesso.")
                except sqlite3.Error as erro:
                    print(f"Não foi possível excluir o registro Nº {id} de Volumes. Codigo de erro: {erro}")
            elif escolha == '5':
                id = int(input('Informe o Id: '))
                try:
                    cursor.execute(f"DELETE FROM Essencias WHERE id = {id}")
                    perfumedb.commit()
                    print(f"Registro nº {id} de Essencias foi excluido com sucesso.")
                except sqlite3.Error as erro:
                    print(f"Não foi possível excluir o registro Nº {id} de Essencias. Codigo de erro: {erro}")
        escolha = ''
        while escolha not in ('S', 'N'):
            escolha = input("Excluir algum item? [S/N] ").upper()
        if escolha == 'N':
            print ("Obrigado. Até a próxima")
            break
else:
    print ("Obrigado. Até a próxima")