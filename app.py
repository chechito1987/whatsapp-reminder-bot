from flask import Flask, request
import requests
import os

app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")


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
        numero = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

                print("Mensaje recibido:", mensaje)

        if "hola" in mensaje.lower():
            print("Responder: Hola Sergio 👋")

        if "recordar" in mensaje.lower():
            respuesta = f"✅ Recordatorio guardado: {mensaje}"
            print(respuesta)
        requests.post(
            f"https://graph.facebook.com/v25.0/{PHONE_NUMBER_ID}/messages",
            headers={
                "Authorization": f"Bearer {WHATSAPP_TOKEN}",
                "Content-Type": "application/json"
            },
            json={
                "messaging_product": "whatsapp",
                "to": numero,
                "type": "text",
                "text": {"body": respuesta}
            }
        )

        print("Mensaje enviado")

    except Exception as e:
        print("Error:", e)

    return "OK", 200
