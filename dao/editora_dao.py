from model.editora import Editora
from database.conexao_factory import ConexaoFactory

class EditoraDAO:

    def __init__(self):
        self.__conexao_factory = ConexaoFactory()  # Abrindo conexão

    def listar(self) -> list[Editora]:
        editoras = list()
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"SELECT nome, endereco, telefone, id FROM editoras")
        resultados = cursor.fetchall() # ele retorna os itens que está dentro do SELECT
        for resultado in resultados:
            # ID e Nome da tupla (quantidade de atributos da tabela no SQL) lembrando que o ID precisa ir por último,
            # pois ele é uma chave artificial criada automaticamente pelo SQL. Outra observação é que os valores são referentes
            # à posição dos atributos da tabela, que no caso, como são retornados no python, começam em 0
            editora = Editora(resultado[0], resultado[1], resultado[2], resultado[3])
            editoras.append(editora)

        cursor.close()
        conexao.close()

        return self.__editoras

    def adicionar(self, editora: Editora) -> None:
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"INSERT INTO editoras (nome, endereco, telefone) VALUES ('{editora.nome}, {editora.endereco}, {editora.telefone}')")
        conexao.commit()  # ele guarda as informações no banco de dados. Usamos o commit em alguns momentos apenas.Apenas quando estamos mandando algo para o banco de dados (operações de escrita)
        cursor.close()  # fechando o cursor
        conexao.close()  # fechando a conexão


    def remover(self, editora_id: int) -> bool:
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute("DELETE FROM editoras WHERE id = %s", (editora_id))
        editoras_removidas = cursor.rowcount # só um status que o postgres retorna para a gente com o registro dos comandos feitos nele
        conexao.commit()
        cursor.close()  # fechando o cursor
        conexao.close()  # fechando a conexão

        if (editoras_removidas == 0):
            return False

        return False

    def buscar_por_id(self, editora_id) -> Editora:
        edt = None
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"SELECT nome, endereco, telefone, id FROM editoras WHERE id = %s", (editora_id))  # o %s é uma das formas de construir string dentro do python
        resultado = cursor.fetchone()
        if (resultado):
            edt = Editora(resultado[0],resultado[1],resultado[2], resultado[3])
        cursor.close()
        conexao.close()

        return edt
    

    