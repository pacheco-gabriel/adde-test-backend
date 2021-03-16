#BIBLIOTECA DE REQUISIÇÕES
import requests
import json
from flask import Flask, jsonify
from Models.Clima import ModelClima;


class Clima:

    def __init__(self, cidade, ip):
        self.cidade  = cidade
        self.ip      = ip
        self.model   = ModelClima();

    # ÉTODO PRINCIPAL POR EFETUAR A BUSCA DO CLIMA
    def search(self):

        # BUSCANDO REGISTRO NO BANCO
        weather = self.getWeather()
        if(len(weather) > 0):
            return self.getReturn(weather)

        weather = self.consultWeather()

        return self.save(weather)

    #RESPONSÁVEL POR FORMATAR O RETORNO
    def getReturn(self, retorno):
        return jsonify(retorno['results'])

    # RESPONSÁVEL POR BUSCAR O CLIMA NO BANCO
    def getWeather(self):
        return self.model.select(self.cidade) if(len(self.cidade)) else {}

    # RESPONSÁVEL POR INSERIR UM RETORNO NO BANCO
    def save(self, weather):
        self.model.insert(weather)
        return self.getReturn(weather)

    # RESPONSÁVEL POR BUSCAR O CLIMA NO WEBSERVICE
    def consultWeather(self):
        key       = '7c026697'
        condition = 'city_name='+self.cidade if(len(self.cidade)) else 'user_ip='+self.ip
        response  = requests.get('https://api.hgbrasil.com/weather?key='+key+'&'+condition)
        return response.json()
