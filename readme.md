Referência: https://github.com/addesistemas/ADDE-teste

Recuros: Utilizei Python 3 + Database PostgreSQL + Framework Flask + API HGBrasil para os recurosos de clima.

Utilização: O endereço padrão é: "http://localhost:5000/{{ cidade }}".

O parametro cidade é opcional, caso ele não seja informado a aplicação requisita o ip da requisição para continuar com o processo.

Observação: Sou iniciante com composer, então caso o container não suba, vou deixar aqui registrados os requisitos:
* sqlalchemy (Recurso de comunicação com o banco de dados)
* Flask==0.10.1 (Framework de estruturação da API)
* flask_cors (Recurso para liberação do cors para as requisições vindas do frontend)
* Para o Banco de dados deixei a estrutura em ./database/create_fixtures.sql
