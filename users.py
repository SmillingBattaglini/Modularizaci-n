from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id  = data['id'] #data = {"id": 1, "first_name":"Elena", "last_name":"De Troya", "email":"elena@cd.com", "created_at":"2022-09-26", "updated_at":"2022-09-26"}
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, formulario):
        #formulario = {"first_name":"Juana", "last_name":"De Arco", "email":"juana@cd.com"}
        query = "INSERT INTO users(first_name, last_name, email) VALUES ( %(first_name)s, %(last_name)s, %(email)s )" #->INSERT INTO users(first_name, last_name, email) VALUES('Juana', 'De Arco', 'juana@codingdojo.com')
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('esquema_usuarios').query_db(query)
        # [
        #     {"id": "1", "first_name": "Elena", "last_name":"De Troya"..},
        #     {"id": "2", "first_name": "Juana", "last_name":"De Arco"..}
        # ]
        users = []
        for u in results: #en u voy a estar guardando mi diccionario y lo quiero transformar en una instancia de usuario
            #u =  {"id": "2", "first_name": "Juana", "last_name":"De Arco"..}
            user = cls(u) #user = User(u) y ahi le estoy mandando con la (u) -> {"id": "2", "first_name": "Juana", "last_name":"De Arco"..}, este diccionario se recibe en 'data'
            users.append(user)
        return users

    @classmethod
    def borrar(cls, formulario):
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result

    @classmethod
    def mostrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "SELECT * FROM users WHERE id = %(id)s" #Select siempre RESGRESA una lista
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        #  result = [ { "id": "1", "fisrt_nam2": "De Troya"...}]
        diccionario = result[0] #diccionario = [ { "id": "1", "fisrt_nam2": "De Troya"...}] - Instancia del usuario
        usuario = cls(diccionario) #usuario = Use(diccionario)
        return usuario

    @classmethod
    def actualizar(cls, formulario):
        # formulario = { "id": "1", "fisrt_name": "De Troya"...}
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s "
        result = connectToMySQL('esquema_usuarios').query_db(query, formulario)
        return result
