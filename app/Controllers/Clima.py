#BIBLIOTECA DE REQUISIÇÕES
import requests
from Models.Clima import ModelClima;


class Clima:

    def __init__(self, cidade):
        self.cidade  = cidade
        self.model   = ModelClima();

    # ÉTODO PRINCIPAL POR EFETUAR A BUSCA DO CLIMA
    def search(self):

        # BUSCANDO REGISTRO NO BANCO
        climate = self.getClimate()
        if(climate):
            return climate

        city = self.getCity()

        # CASO A CIDADE NÃO TENHA CIDO ENCONTRADA
        if(city.woeid.isnumeric() == False):
            return False

        climate = self.consultClimate(city.woeid)

        return self.save(climate)

    # RESPONSÁVEL POR BUSCAR O CLIMA NO BANCO
    def getClimate(self):
        return self.model.select(self.cidade);

    # RESPONSÁVEL POR INSERIR UM RETORNO NO BANCO
    def save(self, climate):
        self.model.insert(climate)
        return self.getClimate();

    # RESPONSÁVEL POR BUSCAR O CLIMA NO WEBSERVICE
    def consultClimate(self, woeid):
        response = requests.get('https://api.hgbrasil.com/weather?woeid='+woeid)
        return response.json()

    # RESPONSÁVEL POR BUSCAR A CIDADE INFORMADA NO WEBSERVICE
    def getCity(self):
        key = '17284dd0'
        response = requests.get('https://api.hgbrasil.com/stats/find_woeid?key='+key+'&format=json-cors&sdk_version=console&city_name='+self.cidade)
        return response.json()
