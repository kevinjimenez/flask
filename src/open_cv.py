# from flask import send_from_directory
# import uuid
import cv2
from flask_cors import CORS
from flask import Flask, render_template, Response, jsonify, send_from_directory

# al realizar el build en angular esta variale es importan static_url_path 

app = Flask(__name__, static_url_path="", static_folder="dist/")
CORS(app)
camara = cv2.VideoCapture(0)

# Si tienes varias cámaras puedes acceder a ellas en 1, 2, etcétera (en lugar de 0)


# Una función generadora para stremear la cámara
# https://flask.palletsprojects.com/en/1.1.x/patterns/streaming/
def generador_frames():
    while True:
        ok, imagen = obtener_frame_camara()
        if not ok:
            break
        else:
            # Regresar la imagen en modo de respuesta HTTP
            # yield b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + imagen + b"\r\n"
            return imagen


def obtener_frame_camara():
    ok, frame = camara.read()
    if not ok:
        return False, None
    # Codificar la imagen como JPG
    _, bufer = cv2.imencode(".jpg", frame)
    imagen = bufer.tobytes()
    return True, imagen


# Cuando visiten la ruta
@app.route("/streaming_camara")
def streaming_camara():
    print('valor')
    print(generador_frames())
    return Response(generador_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


# Cuando toman la foto
# @app.route("/tomar_foto_descargar")
# def descargar_foto():
#     ok, frame = obtener_frame_camara()
#     if not ok:
#         abort(500)
#         return
#     respuesta = Response(frame)
#     respuesta.headers["Content-Type"] = "image/jpeg"
#     respuesta.headers["Content-Transfer-Encoding"] = "Binary"
#     respuesta.headers["Content-Disposition"] = "attachment; filename=\"foto.jpg\""
#     return respuesta


# @app.route("/tomar_foto_guardar")
# def guardar_foto():
#     nombre_foto = str(uuid.uuid4()) + ".jpg"
#     ok, frame = camara.read()
#     if ok:
#         cv2.imwrite(nombre_foto, frame)
#     return jsonify({
#         "ok": ok,
#         "nombre_foto": nombre_foto,
#     })


# Cuando visiten /, servimos el index.html
@app.route('/')
def index():
    return send_from_directory("dist", "index.html") 
    # return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")