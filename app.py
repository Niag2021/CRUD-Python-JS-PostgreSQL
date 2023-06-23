from flask import Flask, jsonify, request
import routes
app=Flask(__name__)

@app.get("/api/tareas")
def getTareas():
    data=routes.listadoTareas()
    return jsonify(data)

@app.get("/api/tareas/<id>")
def getTarea(id):
    data=routes.listarTarea(id)
    return jsonify(data)

@app.post("/api/tareas")
def postTarea():
    if request.method == "POST":
        titulo = tarea["titulo"]
        contexto = tarea["contexto"]
        autor = tarea["autor"]
    data = routes.guardarTarea(titulo, contexto,autor)
    return jsonify(data)
        
@app.put("/api/tareas/<id>")
def putTarea(id):
    if request.method == "PUT":
        titulo = tarea["titulo"]
        contexto = tarea["contexto"]
        autor = tarea["autor"]
    data = routes.actualizarTarea(id, titulo, contexto, autor)
    return jsonify(data)

@app.delete("/api/tareas/<id>")
def deleteTarea(id):
    data=routes.eliminarTarea(id)
    return jsonify(data)


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