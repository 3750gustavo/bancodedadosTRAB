import pyodbc
server = 'localhost\sqlexpress' # for a named instance
database = 'bringmeaction' 
cnxn = pyodbc.connect(driver='{SQL Server}', server='(local)', database='bringmeaction',               
               trusted_connection='yes')
cursor = cnxn.cursor()
print("abrimos a conexao com sqlserver 2018")
while True:
    print("1-Tela de Login com credenciais do SqlServer ")
    print("2-Listar os bancos existentes")
    print("3-Listar as tabelas do banco selecionado")
    print("4-Criar usuáros para o banco selecionado")
    print("5-Alterar permissões dos usuários selecionados (GRANT, DENY e REVOKE)")
    opcao = input("digite o numero da opcao desejada:")
    if opcao == '1':
        cursor.execute("select * from sys.sql_logins")
        while row:
            print(row)
            row = cursor.fetchone()
    if opcao == '2':
        cursor.execute("select name from sys.databases")
        rows = cursor.fetchall()
        for row in rows:    
            print(row[0])    
    if opcao == '3':
        cursor.execute("select name from sys.tables")
        rows = cursor.fetchall()
        for row in rows:    
            print(row[0])
    if opcao == '4':
        nome = input("nome do usuário")
        senha = input("digite a senha")
        inicio = """create login """
        continua = """ with password= '"""
        continua2 = """',default_database=bringmeaction,check_expiration=off,
        check_policy=off"""
        statement = (inicio + nome + continua + senha + continua2)
        #print(statement)
        senha = "'" + senha + "'"
        print(senha)
        cursor.execute('''CREATE LOGIN teste with password= 'senha' ,Default_database=bringmeaction, check_expiration=off,check_policy= off''')
        row = cursor.fetchone() 
        while row:
            print(row)
            row = cursor.fetchone()
        cnxn.commit()       


cursor.execute("SELECT * FROM teste")
row = cursor.fetchone() 
while row:
    print(row)
    row = cursor.fetchone()
cnxn.close()