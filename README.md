<div align="center">
  <h1>
    ezLLM
  </h1>
</div>

<div align="center">
  <p dir="auto">English | <a href="https://github.com/Torkyaz/ezLLM/blob/main/README_es.md">Spanish</a></p>
</div>

## Description

This repository contains a Flask API that communicates with the DuckDuckGo Chat service to send messages and get responses. It uses the aiohttp library to make asynchronous HTTP requests and handle responses from the DuckDuckGo API.

### Features

- RESTful API built with **Flask**.
- Interaction with **GPT 4o Mini**, **Claude 3 Hiaku**, **Llama 3.1 70B** and **Mixtral 8x7B**
- Responses generated from script inputs in Luau.

## Requirements

- Python 3.9 or higher
- Flask
- aiohttp
- asyncio

## Installation

Follow these steps to install and run the project on your local machine.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Torkyaz/ezLLM/
   ```

2. **Create a virtual environment**:

   On Linux/Mac:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   On Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the Flask API that interacts with System AI, execute the following command:

```bash
python [name_file].py
```

This will start a Flask server at `http://0.0.0.0:5000`.


**Request example**:
- Send a POST request with the following curl command:

  ```json
  curl -X POST http://localhost:5000/gpt_response \
    -H "Content-Type: application/json" \
    -d '{"messages": [{"role": "user", "content": "Hello, how are you?"}]}'

  ```

## Contributing
- Contributions are welcome. If you have any suggestions or encounter any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.**. You can view the full text of the license in the [LICENSE](./LICENSE) file.

## Contact
If you have any questions or need help, feel free to open an **issue** on the repository or contact me through Discord: **`torkyaz`**.

# LUAU

The use of the Luau code is published at: https://devforum.roblox.com/t/open-source-ezllm-integrating-an-ai-system-into-roblox/3353748?u=compressedbyte