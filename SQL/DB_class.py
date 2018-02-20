import sqlite3 as sql

class data:
    def __init__(self, db, tab, num):
    # Указываем реквизиты подключаемых
        self.db = db #'tt.db'
        self.tab= tab #'tab2'
        self.num = num #4

        with sql.connect(db) as conn:
            c = conn.cursor()
            c.execute('SELECT id, value FROM {0} WHERE id = {1}'.format(tab, num))
            r = (c.fetchall())
            for row in r:
                return (row)
                #conn.close()
#print (10)


