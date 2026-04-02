from flask import Flask, request, jsonify
import unicodedata

app = Flask(__name__)

def normalizar(texto):
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

@app.route("/")
def home():
    return """
    <h2>🤖 Bot Inteligente</h2>
    <form method="post" action="/chat">
        <input name="msg" placeholder="Digite sua mensagem"/>
        <button type="submit">Enviar</button>
    </form>
    """

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.form["msg"]
    msg = normalizar(msg)

    if "fone" in msg:
        resposta = "Temos fone por R$50 😎"
    elif "carrinho" in msg:
        resposta = "Seu carrinho está vazio 😢"
    else:
        resposta = "Não entendi 🤔"

    return f"""
    <p>Você: {msg}</p>
    <p>Bot: {resposta}</p>
    <a href="/">Voltar</a>
    """

app.run(host="0.0.0.0", port=5000)
