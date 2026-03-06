from flask import Flask, render_template, request
from twilio.rest import Client

from dotenv import load_dotenv
import os

load_dotenv()

ACCOUNT_SID = os.getenv('TWILIO_SID')
AUTH_TOKEN = os.getenv('TWILIO_TOKEN')
app = Flask(__name__)

ACCOUNT_SID = 'AC4bf79078b0d3b837d9ac307db1ae9a88'
AUTH_TOKEN = 'ecd289363b3509db9c81991d85c19559'
TWILIO_NUMBER = 'whatsapp:+14155238886'
MI_NUMERO = 'whatsapp:+527774403046'

def enviar_whatsapp(para, mensaje):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        from_=TWILIO_NUMBER,
        to=para,
        body=mensaje
    )

@app.route('/')
def index():
    try:
        enviar_whatsapp(MI_NUMERO, 
        '🔔 *Nuevo visitante en tu página!*\n'
        '📍 itsystems.solutions\n'
        '🕐 Ahora mismo')
    except:
        pass
    return render_template('index.html')

@app.route('/webhook/whatsapp', methods=['POST'])
def webhook():
    mensaje = request.form.get('Body', '').strip()
    numero = request.form.get('From')
    
    if mensaje == '1':
        respuesta = '🌐 *Desarrollo Web*\nSitios profesionales desde $6,000 MXN\n\nEscribe *menu* para volver'
    elif mensaje == '2':
        respuesta = '📱 *Apps Móviles*\nAndroid e iOS con React Native desde $8,000 MXN\n\nEscribe *menu* para volver'
    elif mensaje == '3':
        respuesta = '💬 *WhatsApp Automático*\nChatbots y recordatorios desde $3,000 MXN\n\nEscribe *menu* para volver'
    elif mensaje == '4':
        respuesta = '🔌 *IoT & Hardware*\nSoluciones con ESP32 desde $5,000 MXN\n\nEscribe *menu* para volver'
    elif mensaje == '5':
        respuesta = '☁️ *Hosting Profesional*\nDesde $10 USD/mes con SSL incluido\n\nVisita: borealwolfhosting.com'
    else:
        respuesta = (
            '👋 Hola! Soy el asistente de *IT Systems Solutions*\n\n'
            '¿En qué te puedo ayudar?\n\n'
            '1️⃣ Desarrollo Web\n'
            '2️⃣ Apps Móviles\n'
            '3️⃣ WhatsApp Automático\n'
            '4️⃣ IoT & Hardware\n'
            '5️⃣ Hosting Profesional\n\n'
            '_Responde con el número de tu opción_'
        )
    
    enviar_whatsapp(numero, respuesta)
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)