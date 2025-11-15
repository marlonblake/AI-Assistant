from flask import Flask, request, jsonify
from llama_cpp import Llama
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

llm = Llama(
    model_path=os.getenv("MODEL_PATH"),
    n_ctx=2048
)

@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json["prompt"]
    system_prompt = "Answer briefly and directly, like a human would in conversation."
    full_prompt = f"{system_prompt}\n\nQ: {user_prompt}\nA:"
    result = llm(
        full_prompt,
        max_tokens=50,
        temperature=0.7,
        stop=["\n\n"]
    )
    reply = result["choices"][0]["text"].strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=5000)
