CREATE DATABASE adde_clima;

CREATE TABLE public.clima_historico (
	id int8 NOT NULL,
	cidade varchar(250) NULL,
	response text NULL,
	data_consulta timestamp(0) NULL,
	CONSTRAINT "primary" PRIMARY KEY (id)
);
