from dao.categoria_dao import CategoriaDAO
from model.categoria import Categoria

categoria = Categoria("Terror")
dao = CategoriaDAO()

dao.adicionar(categoria)
