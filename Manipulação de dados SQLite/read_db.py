import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

'''
cursor.execute(
    """
        SELECT * FROM estudantes
    """
)
'''

cursor.execute(
    """
        SELECT * FROM disciplinas
    """
)

conn.commit()

#estudantes = cursor.fetchall()
disciplinas = cursor.fetchall()

conn.close()

'''
for estudante in estudantes:
    print(disciplina)
'''

for disciplina in disciplinas:
    print(disciplina)