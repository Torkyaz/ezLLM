#-. .- - ..- .-. . / .. ... / -. --- - / -.-. .-. ..- . .-.. .-.-.#

from flask import Flask, request, jsonify
import asyncio
from modelDDG import systemai

app = Flask(__name__)

@app.route('/gpt_response', methods=['POST'])
def gpt_response():
    try:
        # Get the users input from the POST request
        user_input = request.json.get('messages')
        if not user_input:
            return jsonify({"error": "Text not provided"}), 400

        response = asyncio.run(systemai(messages=user_input))

        # Return the response
        return jsonify({"response": response})

    except Exception as e:
        print("Error occurred: ", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
