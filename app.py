
    from flask import Flask, render_template, url_for, request, jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Obtenha a entrada de texto do requisição POST 
    input_text=request.json.get("text")
    
    if not input_text:
        # Resposta a enviar se o input_text for indefinido
        response={
            "status":"erro",
            "message":"digiti um texto para usa bola de cristal nas emoções"
        }
        return jsonify(response)
        # Resposta a enviar se o input_text não for indefinido
    else:
        predicted_emotion,predicted_emotion_img_url=predict(input_text)
        # Enviar resposta         
        response={
            "status":"sucesso",
            "data":{
                "predicted_emotion":predicted_emotion,
                "predicted_emotion_img_url":predicted_emotion_img_url
            }
        }
        return jsonify(response)
app.run(debug=True)

