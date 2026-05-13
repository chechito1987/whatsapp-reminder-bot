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
