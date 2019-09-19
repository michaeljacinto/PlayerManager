import sqlite3

conn = sqlite3.connect('team_members.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE team_members
          (id INTEGER PRIMARY KEY ASC, 
           first_name VARCHAR(100) NOT NULL,
           last_name VARCHAR(100) NOT NULL,
           annual_salary INTEGER(12) NOT NULL,
           member_num VARCHAR(10) NOT NULL,
           contract_years_length INTEGER(2) NOT NULL,
           last_team VARCHAR(100) NOT NULL,
           type VARCHAR(100) NOT NULL,
           specialization VARCHAR(100),
           is_former_player VARCHAR(1),
           jersey_num INTEGER(2),
           position VARCHAR(100)
           )
          ''')

conn.commit()
conn.close()