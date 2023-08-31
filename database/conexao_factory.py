# Fazendo conexão com o banco de dados Postgres SQL
# Fonte das informações: https://api.elephantsql.com/console/3446ac2a-6467-4bae-842a-1c0f207bb50b/details
# é importante colocarmos o fechamento da conexão, pois o banco de dados possui um número limite de conexões. conexao.close()

import psycopg2


# Criando as conexões que serão utilizadas na camada DAO. Para o DAO, model e service, cada um deles utilizaremos a ConexãoFactory
class ConexaoFactory:
    def get_conexao(self):
        return psycopg2.connect(host='silly.db.elephantsql.com',
                                database='xdyfjsoa',
                                user='xdyfjsoa',
                                password='cG0TJOndDJATCseRbtVaVWy8b4NDwPkH')



