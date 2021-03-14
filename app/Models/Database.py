from sqlalchemy import create_engine

class Database:

    # RESPONSÁVEL POR INICIAR UMA CONEXÃO COM O BANCO DE DADOS
    def __init__(self):
        self.host = 'localhost'
        self.user = 'postgres'
        self.pswd = 'password'
        self.name = 'adde_clima'
        self.port = '5432'
        self.connection = create_engine('postgres://{}:{}@{}:{}/{}'.format(self.user, self.pswd, self.host, self.port, self.name))

    # RESPONSÁVEL POR EXECUTAR UMA AÇÃO NO BANCO DE DADOS
    def execute(self, cmd):
        return self.connection.execute(cmd)
