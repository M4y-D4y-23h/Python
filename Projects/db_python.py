import pyodbc

def conecta_ao_banco(driver='ODBC Driver 17 for SQL Server', server=r'DISPOSITIVO\SQLEXPRESS', database='pythonSQL', username=None, password=None, trusted_connection = 'yes'):

  string_conexao = f"DRIVER={driver};SERVER={server};DATABASE={database};USERNAME={username};PASSWORD={password};TRUSTED_CONNECTION={trusted_connection};"
  conexao = pyodbc.connect(string_conexao)
  cursor = conexao.cursor()
  return conexao, cursor

conexao, cursor = conecta_ao_banco()
length = cursor.execute('select * from vendas').fetchall()
conexao.close()
