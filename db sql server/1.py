import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-JEFSBJ1\TEST2019;'
                      'Database=DbPython;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()
def insertdata():
    sql_command="insert into branchs values('مشهد 3')"
    cursor.execute(sql_command)
    conn.commit()
insertdata()

def update():
    sql_command="update  branchs set city=('مشهد75') where id=(101)"
    cursor.execute(sql_command)
    conn.commit()
update()

def delete():
    sql_command = "delete from  branchs  where id in (101)"
    cursor.execute(sql_command)
    conn.commit()
delete()

j=0
cursor.execute('SELECT * FROM branchs order by id')
for i in cursor:
    j=j+1
    print(f"row{j}={i}")
