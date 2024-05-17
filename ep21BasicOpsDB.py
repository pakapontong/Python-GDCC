import pyodbc

constr = ("Driver={SQL Server Native Client 11.0};"
                        "Server=ONDE;"
                        "Database=SampleDB;"
                        "Trusted_Connection=yes;")

conn = pyodbc.connect(constr)

sql_cmd = '''SELECT * FROM Books'''
cursor = conn.cursor()
cursor.execute(sql_cmd)

for row in cursor:
    print(row)