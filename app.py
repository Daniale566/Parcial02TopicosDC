from flask import Flask
import math

app = Flask(__name__)

@app.route('/')
def index():
    return "Pon un número en la URL para mostrar el factorial, por ejemplo: http://127.0.0.1:5000/5"

@app.route('/<int:numero>')
def home(numero):
    resultado = math.factorial(numero)  #Yo utilice una función de la librería math para calcular el factorial, sin embargo ↓
    return f"El factorial de {numero} es {resultado}" # se puede hacer de manera manual con un algoritmo de recursión :p

@app.route('/<path:other>') #Si se pone algo que no sea un número en la URL, se mostrará un mensaje de error
def handle_invalid_input(other):
    return "Solo se pueden poner números en la URL", 400


if __name__ == '__main__':
    app.run(debug=True)
    
#by Daniel Cruz