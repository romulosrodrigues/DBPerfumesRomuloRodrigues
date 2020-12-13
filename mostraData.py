import sqlite3

def titulo (n, s):
    print("="*n)
    print(f'{s}'.center(n))
    print("="*n)

path = r"/home/romulo/Documentos/SQL/Perfumes"
perfumedb = sqlite3.connect(path + r"/dbperfume.db")
cursor =perfumedb.cursor()

#PERFUMES
cursor.execute("SELECT * FROM Perfumes")
tabela = cursor.fetchall()
titulo(78, "PERFUMES")
print("ID".ljust(5)+"Nome".ljust(21)+"Quant".ljust(10)+"Volume".ljust(10)+"Marca".ljust(10)+"Fixacoes".ljust(10))
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(21), end="")
    print(str(linha[2]).ljust(10), end="")
    print(str(linha[3]).ljust(10), end="")
    print(str(linha[4]).ljust(10), end="")
    print(str(linha[5]).ljust(10))

#VOLUMES
cursor.execute("SELECT * FROM Volumes")
tabela = cursor.fetchall()
titulo(78, "VOLUMES")
print("ID".ljust(5)+"Vol".ljust(21))
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(21))

#MARCAS
cursor.execute("SELECT * FROM Marcas")
tabela = cursor.fetchall()
titulo(78, "MARCAS")
print("ID".ljust(5)+"Nome".ljust(21))
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(21))

#ESSENCIAS
cursor.execute("SELECT * FROM Essencias")
tabela = cursor.fetchall()
titulo(78, "ESSENCIAS")
print("ID".ljust(5)+"Nome".ljust(21))
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(21))

#FIXAÇÕES
cursor.execute("SELECT * FROM Fixacoes")
tabela = cursor.fetchall()
titulo(78, "FIXAÇÕES")
print("ID".ljust(5)+"Nome".ljust(21))
for linha in tabela:
    print(str(linha[0]).ljust(5),end="")
    print(linha[1].ljust(21))