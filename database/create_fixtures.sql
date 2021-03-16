CREATE DATABASE adde_clima;

CREATE TABLE IF NOT EXISTS clima_historico (
    id BIGINT,
    cidade VARCHAR(250),
    response TEXT,
    data_consulta TIMESTAMP,
    PRIMARY KEY (id)
);
