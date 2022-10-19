from flask import Flask, render_template, request, redirect
from users import User #Se importa la clase User para poder utilicar sus funciones

#IMPORTANDO la clase de USUARIO

app = Flask(__name__)

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template('index.html', usuarios=users)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['post'])
def create():
    #Recibimos el formulario a través de una variable llamada requests.form y se recibe la información como un diccionario
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    formulario ={"id": id} #diccionario que le ponemos como nombre de variable de diccionario
    User.borrar(formulario)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    formulario ={"id": id}
    user = User.mostrar(formulario) #Instancua de usuario basado en el identificador en la URL
    return render_template('edit.html', usuario = user)

@app.route('/update', methods=['POST'])
def update():
    #request.form = diccionario con el formulario de edit.html
    User.actualizar(request.form)
    return redirect('/')











if __name__=="__main__":
    app.run(debug=True)