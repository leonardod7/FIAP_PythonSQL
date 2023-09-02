from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory

class CategoriaDAO:

    def __init__(self):
        self.__categorias: list[Categoria] = list() # desse jeitos, os dados são armazenados em memória. Dessa forma, não precisamos mais dela
        self.__conexao_factory = ConexaoFactory() # Abrindo conexão

    def listar(self) -> list[Categoria]:
        categorias = list()
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"SELECT id, nome FROM categorias") # as posicoes da chamada precisam estar conforme as posicoes do construtor init em categoria.py
        resultados = cursor.fetchall() # ele retorna os itens que está dentro do SELECT
        # print(resultados)
        for resultado in resultados:
            # ID e Nome da tupla (quantidade de atributos da tabela no SQL) lembrando que o ID precisa ir por último,
            # pois ele é uma chave artificial criada automaticamente pelo SQL. Outra observação é que os valores são referentes
            # à posição dos atributos da tabela, que no caso, como são retornados no python, começam em 0
            cat = Categoria(resultado[0], resultado[1])
            categorias.append(cat)

        cursor.close()
        conexao.close()
        return categorias

    def adicionar(self, categoria: Categoria) -> None:
        conexao = self.__conexao_factory.get_conexao() # Pedir conexão
        cursor = conexao.cursor() # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"INSERT INTO categorias (nome) VALUES ('{categoria.nome}')")
        conexao.commit() # ele guarda as informações no banco de dados. Usamos o commit em alguns momentos apenas.Apenas quando estamos mandando algo para o banco de dados (operações de escrita)
        cursor.close() # fechando o cursor
        conexao.close() # fechando a conexão

    def remover(self, categoria_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute("DELETE FROM categorias WHERE id = %s", (categoria_id))
        categorias_removidas = cursor.rowcount # só um status que o postgres retorna para a gente com o registro dos comandos feitos nele
        conexao.commit()
        cursor.close()  # fechando o cursor
        conexao.close()  # fechando a conexão

        if (categorias_removidas == 0):
            return False

        return True

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"SELECT id, nome FROM categorias WHERE id = %s", (categoria_id)) # o %s é uma das formas de construir string dentro do python
        resultado = cursor.fetchone()
        if (resultado):
            cat = Categoria(resultado[1], resultado[0])
        cursor.close()
        conexao.close()

        return cat



# poderíamos por exemplo criar uma nova classe para instanciar a conexão com o banco, ou um método separado dentro da classe categoriaDAO
# o DAO ficou com a prerrogativa de inserir o código SQL

# Os comandos acima estão sendo feitos manualmente para entendermos como funciona por de baixo dos panos. o Django por exemplo, faz isso de forma automática.
        # Em alguns momentos é interessante fazer comandos manuais para que seja mais performático.