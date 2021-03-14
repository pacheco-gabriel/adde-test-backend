from Models.Database import Database
from datetime import datetime,timedelta
import json

class ModelClima:

    def __init__(self):
        self.database  = Database()
        self.cacheTime = 15

    # RESPONSÁVEL POR BUSCAR UM CLIMA NO BANCO
    def select(self, cidade):
        agora       = datetime.now()
        print(datetime)
        tempoLimite = (agora - timedelta(minutes = self.cacheTime)).strftime("%H:%M:%S")
        result      = self.database.execute('SELECT response FROM clima_historico;')

        print(result)

        if result.response is None:
            return False

        return result.response.json()

    # RESPONSÁVEL POR INSERIR UM RETORNO DE CLIMATE
    def insert(self, climate):
        city         = climate.results.city
        jsonResponse = json.dumps(climate)
        agora        = datetime.now().strftime("%H:%M:%S")
        return self.database.execute('INSERT INTO clima_historico (cidade, response, data_consulta) VALUES ("'+city+'", "'+jsonResponse+'", "'+agora+'" );')
