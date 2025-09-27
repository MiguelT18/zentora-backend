# zentora-backend
El backend de Zentora organiza la lógica central de la plataforma, con una estructura modular que incluye gestión de usuarios, autenticación segura, manejo de datos, esquemas bien definidos, migraciones de base de datos y plantillas de correo, todo orientado a soportar el asistente de trading inteligente Nexa

## Levantar entorno de desarollo
`uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## Levantar entorno de producción
`uvicorn app.main:app --host 0.0.0.0 --port 8000`