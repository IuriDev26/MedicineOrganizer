import psycopg2



class DbAccess():

    def Conectar(self):
        self.connection = psycopg2.connect( dbname="medicineorganizer", user="postgres", password="", host="localhost", port="5432" )
        self.cursor = self.connection.cursor()


    def Desconectar(self):
        self.connection.close()


    def CriarUsuario(self, DadosUsuario):

        usuario = DadosUsuario[0]
        senha   = DadosUsuario[1]
        cpf     = DadosUsuario[2]

        Query = f"INSERT INTO USUARIO (USUARIO, SENHA, CPF) VALUES('{usuario}', {senha}, '{cpf}')"

        self.Conectar()
        self.cursor.execute(Query)
        self.connection.commit()
        self.Desconectar()

        return ( True )
