from Models.Database import Database
import datetime as dt
import json

class ModelClima:

    def __init__(self):
        self.database  = Database()
        self.cacheTime = 15

    # RESPONSÁVEL POR BUSCAR UM CLIMA NO BANCO
    def select(self, cidade):
        tempoLimite = dt.datetime.now() - dt.timedelta(minutes = self.cacheTime);
        tempoLimite = tempoLimite.strftime("%Y-%m-%d %H:%M:%S")
        cidade      = cidade.lower()+'%%'
        result      = self.database.execute('SELECT response FROM clima_historico WHERE lower(cidade) ILIKE \''+cidade+'\' AND data_consulta >= \''+tempoLimite+'\' ORDER BY id DESC LIMIT 1;')

        retorno     = []
        while True:
            rows = result.fetchmany(10000)
            if not rows:
                break
            for row in rows:
                retorno.append(row[0])
                pass

        if retorno == []:
            return []

        return json.loads(retorno[0])

    # RESPONSÁVEL POR INSERIR UM RETORNO DE CLIMA
    def insert(self, weather):
        city         = weather['results']['city']
        jsonResponse = json.dumps(weather)
        return self.database.execute("INSERT INTO clima_historico (id, cidade, response, data_consulta) VALUES ( nextval('clima_sequence'), '"+city+"', '"+jsonResponse+"', current_timestamp);")
