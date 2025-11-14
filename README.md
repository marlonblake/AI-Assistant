# AI-Assistant
## Simple Llama 2 Chatbot

A lightweight chatbot using **Llama 2** and **Flask** with a simple web interface. Designed to give short, direct answers.

---

## Features

- Uses Llama 2 (7B) locally — no API needed.
- Short and simple responses for quick Q&A.
- Works with a simple frontend (HTML/JS) via HTTP requests.
- CORS enabled for local web projects.

---

## Requirements

- Python 3.10+
- Flask
- flask_cors
- llama_cpp
- A quantized Llama 2 model (GGUF format recommended, e.g., `llama-2-7b-chat.Q4_K_M.gguf`)

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/marlonblake/AI-Assistant.git
cd AI-Assistant
