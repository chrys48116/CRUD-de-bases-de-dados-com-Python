import sqlite3

class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def create(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS agenda\
                             (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
                             nome TEXT, \
                            telefone TEXT)")

    def insert(self, nome, telefone):
        consulta = "INSERT INTO agenda (nome, telefone) VALUES (?, ?)"
        self.conn.execute(consulta, (nome, telefone))
        self.conn.commit()
    
    def update(self, nome, telefone, id):
        consulta = "UPDATE agenda SET nome=?, telefone=? WHERE id=?"
        self.conn.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def delete(self, id):
        consulta = "DELETE FROM agenda WHERE id=?"
        self.conn.execute(consulta, (id,))
        self.conn.commit()

    def list(self):
        self.cursor.execute("SELECT * FROM agenda")

        for linha in self.cursor.fetchall():
            print(linha)

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == "__main__":
    agenda = AgendaDB("app/PythonSQL/agenda.db")
    agenda.create()
    agenda.update("Maria", "9999-9999", 2)
    agenda.delete(3)
    agenda.list()
    agenda.close()