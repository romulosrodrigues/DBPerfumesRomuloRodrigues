import sqlite3

path = r"/home/romulo/Documentos/SQL/Perfumes"
perfumedb = sqlite3.connect(path + r"/dbperfume.db")
cursor =perfumedb.cursor()

#Criando as tabelas
cursor.execute("CREATE TABLE IF NOT EXISTS Perfumes (id integer, nome text, quantidade integer, Volumes_FK integer, Marcas_FK integer, Fixacoes_FK integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Marcas (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Fixacoes (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Volumes (id integer, nome text)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencias_Perfumes(Essencias_FK integer, Perfumes_FK integer)")
cursor.execute("CREATE TABLE IF NOT EXISTS Essencias(id integer, nome text)")