import psycopg2



class DbAccess():

    def Conectar(self):
        self.connection = psycopg2.connect( dbname="medicineorganizer", user="postgres", password="Iuricrbtyuio123@#", host="localhost", port="5432" )
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
    
    def CriarLogin(self, DadosUsuario):

        usuario = DadosUsuario[0]
        senha = DadosUsuario[1]

        self.Conectar()
        Consultar= f"select * from usuario where usuario = '{usuario}' and senha = '{senha}'"
        self.cursor.execute(Consultar)

        QuantiRegistros= len(self.cursor.fetchall()) 
        
        if QuantiRegistros == 0:
            LoginSucesso = False
        else:
            LoginSucesso = True

        return LoginSucesso
    
    def CriarPaciente(self, paciente):

        nome = paciente[0]
        cpf  = paciente[1]

        query = f"INSERT INTO PACIENTE (NOME, CPF) VALUES( '{nome}', '{cpf}' )"

        self.Conectar()
        self.cursor.execute(query)
        self.connection.commit()
        self.Desconectar()
    
    def CriarMedicamento(self, medicamento):

        query = f"INSERT INTO REMEDIO(DESCRICAO) VALUES('{medicamento}')"

        self.Conectar()
        self.cursor.execute(query)
        self.connection.commit()
        self.Desconectar()

    
        

    
