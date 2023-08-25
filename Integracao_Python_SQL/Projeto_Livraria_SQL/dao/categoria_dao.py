from model.categoria import Categoria
from database.conexao_factory import ConexaoFactory

class CategoriaDAO:

    def __init__(self):
        self.__categorias: list[Categoria] = list()
        self.__conexao_factory = ConexaoFactory()

    def listar(self) -> list[Categoria]:
        return self.__categorias

    def adicionar(self, categoria: Categoria) -> None:
        # self.__categorias.append(categoria)
        conexao = self.__conexao_factory.get_conexao()
        # o cursor é o ponteiro que sabe navegar e inserir dados no meu banco de dados
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO categorias (nome) VALUES ('{categoria.nome}')")

        # Os comandos acima estão sendo feitos manualmente para entendermos como funciona por de baixo dos panos. o Django por exemplo, faz isso de forma automática.
        # Em alguns momentos é interessante fazer comandos manuais para que seja mais performático.

    def remover(self, categoria_id: int) -> bool:
        encontrado = False
        
        for c in self.__categorias:
            if (c.id == categoria_id):
                index = self.__categorias.index(c)
                self.__categorias.pop(index)
                encontrado = True
                break
        return encontrado

    def buscar_por_id(self, categoria_id) -> Categoria:
        cat = None
        for c in self.__categorias:
            if (c.id == categoria_id):
                cat = c
                break
        return cat
    
    def ultimo_id(self) -> int:
        index = len(self.__categorias) -1
        if (index == -1):
            id = 0
        else:
            id = self.__categorias[index].id
        return id
    