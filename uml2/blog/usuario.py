class Usuario:
    def __init__(self, id: str, nome: str, login: str, senha: str) -> None:
        self.__id = id
        self.__nome = nome
        self.__login = login
        self.__senha = senha

    def __str__(self) -> str:
        return f"\n{'':=^40}ID = {self.id}\nNOME = {self.nome}\nLOGIN = {self.login}\nSENHA = {self.senha}\n"

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, other: int) -> None:
        self.__id = other

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, other: str) -> None:
        self.__nome = other

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, other: str) -> None:
        self.__login = other

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, other: str) -> None:
        self.__senha = other



        