from flask import Flask, render_template
import requests
from flask import Flask, render_template, request, jsonify
import os
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    response = chat_gpt(message)
    return jsonify(response=response)




def chat_gpt(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": message}],
        "temperature": 0.7
    }


    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    print(response_json)
    response_message = response_json['choices'][0]['message']['content']
    # print(response_message)
    return response_message.strip()

if __name__ == '__main__':
    app.run(debug=True)
