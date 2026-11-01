import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

st.set_page_config(page_title="Control de la Cava", page_icon="🍷")

# ------------------------------------------------------------------
# TEMA "CONTROL DE LA CAVA" (solo estilos CSS; la lógica y los inputs no cambian)
# ------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@600;700&family=Nunito:wght@400;600;700&display=swap');

:root{
  --vino:#6b1e2e;
  --vino-oscuro:#3f0f1a;
  --dorado:#c9a45c;
  --dorado-claro:#f3e7cc;
  --crema:#faf6ef;
  --piedra:#efe7da;
  --tinta:#1f1a17;
}

/* Fondo: muro de piedra clara de la cava */
.stApp{
  background:
    repeating-linear-gradient(0deg, transparent 0 58px, rgba(140,110,80,.07) 58px 60px),
    var(--piedra);
  background-attachment: fixed;
}
header[data-testid="stHeader"]{ background: transparent; }

/* Panel central: etiqueta de botella */
[data-testid="stMainBlockContainer"], .block-container{
  background:var(--crema);
  border-radius:20px;
  border:1px solid rgba(201,164,92,.55);
  box-shadow:0 20px 50px rgba(63,15,26,.14);
  margin-top:2rem;
  margin-bottom:4rem;
  padding:1.6rem 2.2rem 2.4rem !important;
  max-width:780px;
}
@media (max-width:640px){
  [data-testid="stMainBlockContainer"], .block-container{
    padding:1.1rem 1rem 1.8rem !important;
  }
}

/* Encabezado: placa de la cava */
.cava-hero{
  border-radius:16px;
  padding:1.8rem 1.8rem 1.6rem;
  margin-bottom:.6rem;
  background:linear-gradient(135deg, var(--vino-oscuro) 0%, var(--vino) 100%);
  box-shadow: inset 0 0 0 1px rgba(201,164,92,.5), inset 0 0 0 6px var(--vino-oscuro), inset 0 0 0 7px rgba(201,164,92,.35);
}
.cava-tag{
  display:inline-block;
  font-family:'Nunito', sans-serif;
  font-weight:700; font-size:.78rem; letter-spacing:.16em; text-transform:uppercase;
  color:var(--vino-oscuro);
  background:var(--dorado);
  padding:.3rem .8rem; border-radius:999px;
}
.cava-title{
  font-family:'Cormorant Garamond', serif;
  font-weight:700; font-size:3rem; line-height:1.05;
  color:var(--dorado-claro);
  margin:.8rem 0 .4rem;
}
.cava-sub{
  font-family:'Nunito', sans-serif;
  font-size:1.05rem; line-height:1.55;
  color:#f5ece6;
  max-width:540px;
}
.cava-ideal{ display:flex; flex-wrap:wrap; gap:.5rem; margin-top:1.1rem; }
.cava-ideal span{
  font-family:'Nunito', sans-serif; font-weight:700; font-size:.9rem;
  color:#ffffff;
  background:rgba(255,255,255,.1);
  border:1px solid rgba(201,164,92,.55);
  padding:.35rem .85rem; border-radius:999px;
}
@media (max-width:640px){
  .cava-title{ font-size:2.2rem; }
}

/* Títulos y textos del contenido */
h2, h3{
  font-family:'Cormorant Garamond', serif !important;
  font-weight:700 !important;
  color:var(--vino) !important;
}
h1 a, h2 a, h3 a{ display:none !important; }
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li{
  font-family:'Nunito', sans-serif;
  line-height:1.6;
}
.stApp hr{ border-color: rgba(201,164,92,.45); }

/* Barra lateral: piedra cálida */
section[data-testid="stSidebar"]{
  background:var(--crema);
  border-right:3px solid var(--vino);
}
section[data-testid="stSidebar"] h3{ font-size:1.3rem !important; }

/* Textos sobre fondos claros: siempre en negro (también si Streamlit usa el tema oscuro) */
.stApp [data-testid="stWidgetLabel"] p,
.stApp [data-testid="stWidgetLabel"] label,
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp [data-testid="stCaptionContainer"],
.stApp [data-testid="stSliderThumbValue"],
.stApp [data-testid="stSliderTickBarMin"],
.stApp [data-testid="stSliderTickBarMax"],
.stApp [data-testid="caption"],
.stApp [data-testid="stAlert"] [data-testid="stMarkdownContainer"] *{
  color:#1a1a1a !important;
}

/* Botones: conservan los colores originales de Streamlit (contraste) */
.stApp button [data-testid="stMarkdownContainer"],
.stApp button [data-testid="stMarkdownContainer"] *,
.stApp button [data-testid="stMarkdownContainer"] p{
  color:inherit !important;
  font-family:inherit !important;
}
</style>
""", unsafe_allow_html=True)

# Muestra la versión de Python junto con detalles adicionales
st.write("Versión de Python:", platform.python_version())

values = 0.0
act1="OFF"

def on_publish(client,userdata,result):             #create function for callback
    print("el dato ha sido publicado \n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received=str(message.payload.decode("utf-8"))
    st.write(message_received)

        


broker="157.230.214.127"
port=1883
client1= paho.Client("tamarindo")
client1.on_message = on_message



st.markdown("""
<div class="cava-hero">
  <span class="cava-tag">🍷 Control de cava</span>
  <div class="cava-title">Control de la Cava</div>
  <div class="cava-sub">Enciende la luz y ajusta la ventilación de tu cava a distancia, sin abrir la puerta ni cambiar la temperatura.</div>
  <div class="cava-ideal"><span>💡 Luz de la cava</span><span>🌬️ Compuerta de ventilación</span></div>
</div>
""", unsafe_allow_html=True)

st.subheader("💡 Luz de la cava")

if st.button('💡 Encender luz'):
    act1="ON"
    client1= paho.Client("tamarindo")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_a", message)
 
    #client1.subscribe("Sensores")
    
    
else:
    st.write('')

if st.button('🌑 Apagar luz'):
    act1="OFF"
    client1= paho.Client("tamarindo")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)  
    message =json.dumps({"Act1":act1})
    ret= client1.publish("cmqtt_a", message)
  
    
else:
    st.write('')

st.subheader("🌬️ Ventilación")
values = st.slider('Apertura de la compuerta de ventilación (%)',0.0, 100.0)
st.write('Apertura seleccionada (%):', values)

if st.button('🍷 Ajustar ventilación'):
    client1= paho.Client("tamarindo")                           
    client1.on_publish = on_publish                          
    client1.connect(broker,port)   
    message =json.dumps({"Analog": float(values)})
    ret= client1.publish("cmqtt_s", message)
    
 
else:
    st.write('')




