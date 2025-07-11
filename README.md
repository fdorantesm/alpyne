# Alpyne Worker

Este proyecto es un ejemplo de worker en Python siguiendo DDD y arquitectura
hexagonal. Incluye reinicio automático con `watchgod`, adaptadores HTTP con
FastAPI, soporte para Kafka y Redis y un contenedor de inyección de
dependencias inspirado en `pynversify`.

Para ejecutar el proyecto en modo de desarrollo:

```bash
python -m src
```

Es necesario instalar las dependencias declaradas en `pyproject.toml`.
