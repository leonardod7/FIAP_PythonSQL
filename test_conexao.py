import psycopg2

if __name__ == '__main__':
    conexao = psycopg2.connect(host='silly.db.elephantsql.com',
                                database='xdyfjsoa',
                                user='xdyfjsoa',
                                password='cG0TJOndDJATCseRbtVaVWy8b4NDwPkH')

    print("Conexão OK!")
    conexao.close()