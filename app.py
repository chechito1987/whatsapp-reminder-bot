from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "sergio2026"


@app.route("/", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Token incorrecto", 403


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()

    try:
        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

        print("Mensaje recibido:", mensaje)

        if "hola" in mensaje.lower():
            print("Responder: Hola Sergio 👋")

        if "recordar" in mensaje.lower():
            print("Crear recordatorio")

    except Exception as e:
        print("Error:", e)

    return "OK", 200


@app.route("/health", methods=["GET"])
def health():
    return "Bot activo", 200
