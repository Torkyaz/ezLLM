<div align="center">
  <h1>
    ezLLM
  </h1>
</div>

<div align="center">
  <p dir="auto">Español | <a href="https://github.com/Torkyaz/ezLLM/blob/main/README_es.md">Inglés</a></p>
</div>

## Descripción

Este repositorio contiene una API de Flask que se comunica con el servicio DuckDuckGo Chat para enviar mensajes y obtener respuestas. Utiliza la biblioteca `aiohttp` para realizar solicitudes HTTP asincrónicas y manejar las respuestas de la API de DuckDuckGo.

### Características

- API RESTful construida con **Flask**.
- Interacción con **GPT 4o Mini**, **Claude 3 Hiaku**, **Llama 3.1 70B** y **Mixtral 8x7B**.
- Respuestas generadas a partir de entradas de scripts en Luau.

## Requisitos

- Python 3.9 o superior
- Flask
- aiohttp
- asyncio

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu máquina local.

1. **Clona el repositorio**:

   ```bash
   git clone https://github.com/Torkyaz/ezLLM/
   ```

2. **Crea un entorno virtual**:

   En Linux/Mac:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   En Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para ejecutar la API de Flask que interactúa con System AI, ejecuta el siguiente comando:

```bash
python [nombre_archivo].py
```

Esto iniciará un servidor Flask en `http://0.0.0.0:5000`.

**Ejemplo de solicitud**:
- Envía una solicitud POST con el siguiente comando `curl`:

  ```json
  curl -X POST http://localhost:5000/gpt_response \
    -H "Content-Type: application/json" \
    -d '{"messages": [{"role": "user", "content": "Hola, ¿cómo estás?"}]}'
  ```

## Contribuciones
- Las contribuciones son bienvenidas. Si tienes alguna sugerencia o encuentras algún problema, no dudes en abrir un problema o enviar una solicitud de pull.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver el texto completo de la licencia en el archivo [LICENSE](./LICENSE).

## Contacto

Si tienes alguna pregunta o necesitas ayuda, no dudes en abrir un **problema** en el repositorio o contactarme a través de Discord: **`torkyaz`**.

# LUAU
El uso del código de Luau se encuentra publicado en: https://devforum.roblox.com/t/open-source-ezllm-integrating-an-ai-system-into-roblox/3353748?u=compressedbyte
