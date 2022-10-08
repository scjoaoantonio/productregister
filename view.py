# importanto sqlite
import sqlite3 as lite


# criando conexão
con = lite.connect('dados.db')


# inserir dados
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventorio(nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES(?,?,?,?,?,?,?,?)"
        cur.execute(query, i)


# Atualizar dados
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = "UPDATE inventorio SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)


# Deletar dados
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventorio WHERE id=?"
        cur.execute(query, i)


# ver dados
def ver_form():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventorio"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados


# ver item individualmente
def ver_item(id):
    ver_dados_individual = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)

    return ver_dados_individual
