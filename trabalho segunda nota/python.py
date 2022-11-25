from os import O_SEQUENTIAL
import pyodbc
server = '(local)' # for a named instance
comparador = 'local'
database = 'bringmeaction'
banco_atual = 'bringmeaction'
serv = input("digite local se quiser uma conexao local,caso contrario digite o endereço ip")
if serv != comparador:
    server = serv
#serv = "'(" + serv + ")'" 
#print(serv)
cnxn = pyodbc.connect(driver='{SQL Server}', server=server, database='bringmeaction',           
               trusted_connection='yes')
cursor = cnxn.cursor()
print("abrimos a conexao com sqlserver 2018")
banco_de_dados_selecionado = "bringmeaction"
def listarusuarios():
    cursor.execute("select * from sys.sql_logins")
    rows = cursor.fetchall()
    i = 1
    for row in rows:    
        print(str(i) + ' : ' + row[0])
        i = i + 1
def listabancos():
    cursor.execute("select name from sys.databases")
    rows = cursor.fetchall()
    for row in rows:    
        print(row[0])    
while True:
    print("1-Tela de Login com credenciais do SqlServer ")
    print("2-Listar os bancos existentes")
    print("3-Listar as tabelas do banco selecionado")
    print("4-Criar usuáros para o banco selecionado")
    print("5-Alterar permissões dos usuários selecionados (GRANT, DENY e REVOKE)")
    opcao = input("digite o numero da opcao desejada:")
    if opcao == '1':
        listarusuarios()
    if opcao == '2':
        listabancos()
    if opcao == '3':
        listabancos()
        novo_banco = input("qual o nome do banco de dados que vc quer?")
        if novo_banco != banco_atual:
            print("conectando a banco diferente do atual: " + novo_banco)
            cnxn = pyodbc.connect(driver='{SQL Server}', server='(local)', database=novo_banco,           
               trusted_connection='yes')
            cursor = cnxn.cursor()
            banco_atual = novo_banco
        else:
            print("este banco já esta conectado, seguindo com procedimento de exibir tabelas")       
        cursor.execute("select name from sys.tables")
        rows = cursor.fetchall()
        for row in rows:    
            print(row[0])    
    if opcao == '4':
        listabancos()
        novo_banco = input("qual o nome do banco de dados que vc quer?")
        if novo_banco != banco_atual:
            print("conectando a banco diferente do atual: " + novo_banco)
            cnxn = pyodbc.connect(driver='{SQL Server}', server='(local)', database=novo_banco,           
               trusted_connection='yes')
            cursor = cnxn.cursor()
            banco_atual = novo_banco
        else:
            print("este banco já esta conectado, seguindo com procedimento de criar user e login")
        nome = input("nome do usuário")
        senha = input("digite a senha")
        inicio = """create login """
        continua = """ with password= '"""
        continua2 = """',default_database=bringmeaction,check_expiration=off,
        check_policy=off"""
        #statement = (inicio + nome + continua + senha + continua2)
        #print(statement)
        senha = "'" + senha + "'"
        print(senha)
        try:
            sql = "CREATE LOGIN " + nome + " WITH PASSWORD = " + senha + ";"
            cursor.execute(sql)
        finally:
            sql = "create user " + nome + " for login " + nome
            cursor.execute(sql)
        #rows = cursor.fetchall()
        #for row in rows:    
        #    print(row[0]) 
            cnxn.commit()
    if opcao == '5':
        print("1-Grant ")
        print("2-Deny")
        print("3-Revoke")
        acao = input("digite o numero da opcao desejada:")
        listarusuarios()
        user = input("digite o nome do usuario desejado")
        if acao == '1':
            OQ = input("oq vc vai dar permicao?")
            onde = input("onde essa permicao se aplica")
            sql = "grant " + OQ + " on " + onde + " to " + user + ";"
            print(sql)
            cursor.execute(sql)
            cnxn.commit()
        if acao == '2':
            OQ = input("oq vc vai negar permicao?")
            onde = input("onde essa des-permicao se aplica")
            sql = "deny " + OQ + " on " + onde + " to " + user + ";"
            print(sql)
            cursor.execute(sql)
            cnxn.commit()
        if acao == '3':
            OQ = input("oq vc vai tirar permicao?")
            onde = input("onde esse cancelamento se aplica")
            sql = "revoke " + OQ + " on " + onde + " to " + user + ";"
            print(sql)
            cursor.execute(sql)
            cnxn.commit()     






cursor.execute("SELECT * FROM teste")
row = cursor.fetchone() 
while row:
    print(row)
    row = cursor.fetchone()
cnxn.close()