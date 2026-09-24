import sqlite3

def conectar():
    conn = sqlite3.connect("loja.db")
    return conn

def criar_tabela_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS produtos(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                preco FLOAT
            )
        """
    )
    conn.commit()
    conn.close()

def criar_produto(nome, preco):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO produtos(nome, preco) \
            VALUES (?, ?)
        """, (nome, preco)
    )

    conn.commit()
    conn.close()

def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM produtos
        """
    )
    produtos = cursor.fetchall()

    for produto in produtos:
        print(produto)

    conn.commit()
    conn.close()
