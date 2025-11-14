from flask import Flask, request, jsonify
from llama_cpp import Llama
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

llm = Llama(
    model_path="D:\myproject\models\llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=2048
)

@app.route("/chat", methods=["POST"])
def chat():
    prompt = request.json["prompt"]

    result = llm(
        prompt,
        max_tokens=50,
        stream=False
    )

    reply = result["choices"][0]["text"].strip()
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(port=5000)

