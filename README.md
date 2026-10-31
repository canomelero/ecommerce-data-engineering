# Ecommerce Data Engineering

Proyecto de ingeniería de datos para recopilar información de distintas fuentes,
transformarla y dejarla preparada para el análisis de un negocio de comercio
electrónico.

## Estado actual

Hasta ahora se ha configurado la base de datos que servirá como punto de partida
del proyecto:

- PostgreSQL 16 ejecutándose en un contenedor Docker.
- Orquestación del servicio mediante Docker Compose.
- Persistencia de los datos mediante un volumen de Docker.
- Comprobación de disponibilidad de PostgreSQL mediante un *healthcheck*.
- Gestión y consulta de la base de datos desde DBeaver.

## Tecnologías

- **Docker** y **Docker Compose**: ejecución y orquestación de servicios.
- **PostgreSQL 16**: almacenamiento de los datos.
- **DBeaver**: cliente para conectarse y trabajar con PostgreSQL.

## Requisitos

- Docker instalado y en ejecución.
- Docker Compose disponible mediante `docker compose`.
- DBeaver (opcional).

## Configuración

Las credenciales y el nombre de la base de datos se definen mediante variables
de entorno en el archivo `.env`, que no debe subirse al repositorio si contiene
credenciales reales.

Las variables utilizadas son:

```env
POSTGRES_DB=<nombre_de_la_base_de_datos>
POSTGRES_USER=<usuario>
POSTGRES_PASSWORD=<contraseña>
```

## Ejecución

Desde la raíz del proyecto, inicia el servicio con:

```bash
docker compose up -d
```

Para comprobar la configuración antes de iniciar los contenedores:

```bash
docker compose config
```

Para consultar el estado de los servicios:

```bash
docker compose ps
```

Para detener los contenedores:

```bash
docker compose down
```

Los datos se conservan en el volumen `postgres_data` aunque se detengan los
contenedores. Para eliminar también el volumen y sus datos:

```bash
docker compose down -v
```

> Ejecuta este último comando únicamente si quieres borrar la base de datos.

## Conexión desde DBeaver

En DBeaver, crea una conexión PostgreSQL con estos valores:

| Parámetro | Valor |
|---|---|
| Host | `localhost` |
| Puerto | `5432` |
| Base de datos | El valor de `POSTGRES_DB` |
| Usuario | El valor de `POSTGRES_USER` |
| Contraseña | El valor de `POSTGRES_PASSWORD` |

## Próximos pasos

- Incorporar las fuentes de datos del negocio.
- Diseñar el modelo de datos.
- Implementar los procesos de extracción, transformación y carga (ETL).
- Automatizar la ejecución de los procesos.
- Añadir validaciones y documentación de los datos.
