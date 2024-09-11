import sqlite3
from modelo import Pessoa, Marca, Veiculo
banco = sqlite3.connect("database.db")
banco.execute("PRAGMA foreign_keys=on")
cursor = banco.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Pessoa(cpf INTEGER PRIMARY KEY,
              nome TEXT NOT NULL,
               nascimento DATE NOT NULL,
                oculos BOOLEAN NOT NULL);
''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Marca(
               id INTEGER NOT NULL,
               nome TEXT NOT NULL,
               sigla CHARACTER(2) NOT NULL,
               PRIMARY KEY(id)
               );''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Veiculo(
               placa CHARACTER(7) NOT NULL,
               ano INTEGER NOT NULL,
               cor TEXT NOT NULL,
               proprietario INTEGER NOT NULL,
               marca INTEGER NOT NULL,
               PRIMARY KEY(placa),
               FOREIGN KEY(proprietario) REFERENCES Pessoa(cpf),
               FOREIGN KEY(marca) REFERENCES Marca(id)
               );
''')
#cursor.execute('''ALTER TABLE Veiculo ADD motor REAL;''')
#insersão de dados - query dinâmicas
"""comando = '''INSERT INTO Pessoa(cpf,nome, nascimento, oculos) VALUES (?,?,?,?)'''"""
"""pessoa = Pessoa(92345678900,"Pedro", "2000-01-31", True)
#print(pessoa.usa_oculos)
cursor.execute(comando,(pessoa.cpf, pessoa.nome, pessoa.nascimento, pessoa.usa_oculos) )"""
#criar uma lista de objetos Pessoa
"""pessoas = [Pessoa(12345678900,"Joao", "200-01-31",True),
Pessoa(98765432100,"Cynhtia", "1995-03-10", False)]
cursor.executemany(comando,[(i.cpf, i.nome,i.nascimento, i.usa_oculos) for i in pessoas])"""

#outra forma de inserir
#pessoa = Pessoa(30345676900,"Carlos","2000-01-31", True)
comando = '''INSERT INTO Pessoa(cpf,nome,nascimento,oculos) VALUES(:cpf, :nome, :nascimento,:usa_oculos)'''
"""cursor.execute(comando,{"cpf":pessoa.cpf,"nome":pessoa.nome,"nascimento":pessoa.nascimento,"usa_oculos":pessoa.usa_oculos})"""
"""pessoa = Pessoa(60345676900,"Joao","2000-01-31",False)
cursor.execute(comando, vars(pessoa))
print(vars(pessoa))"""

#adicionar marca

comando1 = '''INSERT INTO Marca(nome,sigla) VALUES (:cpf, :nome, :sigla)
marcaA = Marca("MarcaA", "MA")
cursor.execute(comando1, vars(marcaA))
marcaA.id = cursor.lastrowid #armazenar o id da linha do ultimo registro do banco''' 

marcaB = Marca("marcaB", "MB")
cursor.execute(comando1, vars(marcaB))
marcaB.id = cursor.lastrowid
#adicionar veiculo
comando2 = '''INSERT INTO Veiculo(placa,ano,cor,motor,propietario,marca) VALUES(:placa, :ano, :cor, :motor,
 :propietario, :marca))

veiculo1 = Veiculo("AABB001", "2001", "Prata", 1.0, 12345678900,1)
veiculo2 = Veiculo("BABB001", "2002", "Preto", 1.4, 98765432100,2)
cursor.execute(comando2,vars(veiculo1))
cursor.execute(comando2,vars(veiculo2))'''

comando3 = '''SELECT Pessoa.nome, Marca.nome FROM Pessoa JOIN Marca.id = Veiculo.marca WHERE Marca.nome = :nome;'''
cursor.execute(comando3,{"nome": "marcaB"})
registros = cursor.fetchall()
print(registros)
banco.commit()
#fehcamento do cursor e da conexao 
cursor.close()
banco.close()
