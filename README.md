# FileGenerator API Service

## Descripción

FileGenerator API Service es un microservicio diseñado para la gestión, optimización y almacenamiento de archivos. Está construido utilizando el framework FastAPI, proporcionando una interfaz sencilla y rápida para la generación y manipulación de archivos a través de solicitudes HTTP. Este servicio es ideal para aplicaciones que requieren la generación dinámica de documentos, reportes, o cualquier tipo de archivo, permitiendo una integración fácil y eficiente con otros sistemas.

## Características

- Generación de Archivos: Permite la creación de diversos tipos de archivos (PDF, Excel, etc.) de manera dinámica.
- Optimización de Archivos: Optimiza archivos para reducir su tamaño sin perder calidad.
- Almacenamiento de Archivos: Gestiona el almacenamiento seguro y eficiente de archivos generados.
- API RESTful: Proporciona una API RESTful fácil de usar para interactuar con el servicio.
- Documentación Integrada: Documentación automática de la API utilizando Swagger y Redoc.

## Requisitos

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic
- SQLAlchemy (opcional, para almacenamiento en base de datos)
- Dependencias adicionales según los tipos de archivos soportados (p.ej., reportlab para PDF, openpyxl para Excel)

#Copiar .env.example a un nuevo archivo .env
# test branch dev