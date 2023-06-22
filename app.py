from flask import Flask
app=Flask(__name__)

@app.get("/")
def index():
    return "Hola."

if __name__ == "__main__":
    #Al iniciar el servidor se iniciara 
    # el comando run

    #Numero de localhost 127.0.0.1 
    #Puerto 5000 
    #
    #
    app.run(host="127.0.0.1", port=5000)