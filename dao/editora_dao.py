from model.editora import Editora
from database.conexao_factory import ConexaoFactory

class EditoraDAO:

    def __init__(self):
        self.__editoras: list[Editora] = list()
        self.__conexao_factory = ConexaoFactory()  # Abrindo conexão

    def listar(self) -> list[Editora]:
        editoras = list()
        conexao = self.__conexao_factory.get_conexao()  # Pedir conexão
        cursor = conexao.cursor()  # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor.execute(f"SELECT id, nome, endereco, telefone FROM editoras")
        resultados = cursor.fetchall() # ele retorna os itens que está dentro do SELECT
        for resultado in resultados:
            # ID e Nome da tupla (quantidade de atributos da tabela no SQL) lembrando que o ID precisa ir por último,
            # pois ele é uma chave artificial criada automaticamente pelo SQL. Outra observação é que os valores são referentes
            # à posição dos atributos da tabela, que no caso, como são retornados no python, começam em 0
            editora = Editora(resultado[1], resultado[2], resultado[3], resultado[0])
            editoras.append(editora)
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
        cursor.execute(f"SELECT id, nome, endereco, telefone FROM editoras WHERE id = %s", (editora_id))  # o %s é uma das formas de construir string dentro do python
        resultado = cursor.fetchone()
        if (resultado):
            edt = Editora(resultado[1],resultado[2],resultado[3], resultado[0])
        cursor.close()
        conexao.close()

        return edt
    
    def ultimo_id(self) -> int:
        index = len(self.__editoras) -1
        if (index == -1):
            id = 0
        else:
            id = self.__editoras[index].id
        return id
    