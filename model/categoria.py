class Categoria:

    # Fizemos um ajuste no parâmetro id: int, onde será criado automaticamente. O Postgree vai criar o ID, artificialmente.
    def __init__(self, nome: str, id: int=0): # precisamos passar primeiro os parâmetros com valores definidos.
        self.__id: int = id
        self.__nome: str = nome

    @property
    def id(self) -> int:
        return f'{self.__id} | {self.__nome}'
    
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @staticmethod # usando o static permite que não seja preciso instanciar o objeto
    def depositar():
        return "Opa"