FROM postgres:latest
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=adde_clima
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
