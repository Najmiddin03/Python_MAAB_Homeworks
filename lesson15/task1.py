import sqlite3

conn = sqlite3.connect('data.db')
cursor = conn.cursor()
# 1
cursor.execute('create table if not exists Roster('
               'Name text,'
               'Species text,'
               'Age integer'
               ')')
# 2
cursor.execute('insert into Roster values("Benjamin Sisko","Human",40)')
cursor.execute('insert into Roster values("Jadzia Dax","Trill",300)')
cursor.execute('insert into Roster values("Kira Nerys","Bajoran",29)')
# 3
cursor.execute('update Roster set Name="Ezri Dax" where Name="Jadzia Dax"')
# 4
cursor.execute('select Name, Age from Roster where Species="Bajoran"')
for row in cursor.fetchall():
    print(row)
conn.commit()
conn.close()
