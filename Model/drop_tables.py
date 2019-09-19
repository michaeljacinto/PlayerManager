import sqlite3

conn = sqlite3.connect('team_members.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE team_members
          ''')

conn.commit()
conn.close()