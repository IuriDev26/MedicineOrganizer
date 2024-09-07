import psycopg2



class DbAccess():

    def Conectar(self):
        self.connection = psycopg2.connect( dbname="medicineorganizer", user="postgres", password="558922", host="localhost", port="5432" )
        self.cursor = self.connection.cursor()


    def Desconectar(self):
        self.connection.close()


    def CriarUsuario(self, DadosUsuario):

        usuario = DadosUsuario[0]
        senha   = DadosUsuario[1]
        cpf     = DadosUsuario[2]
        nome    = DadosUsuario[3]

        Query = f"INSERT INTO ENFERMEIRO (USUARIO, SENHA, CPF, NOME) VALUES('{usuario}', {senha}, '{cpf}', '{nome}')"

        self.Conectar()
        self.cursor.execute(Query)
        self.connection.commit()
        self.Desconectar()

        return ( True )

    def CriarLogin(self, DadosUsuario):

        usuario = DadosUsuario[0]
        senha = DadosUsuario[1]

        self.Conectar()
        Consultar= f"select * from ENFERMEIRO where usuario = '{usuario}' and senha = '{senha}'"
        self.cursor.execute(Consultar)

        usuarios = self.cursor.fetchall()
        QuantiRegistros= len(usuarios)

        if QuantiRegistros == 0:
            LoginSucesso = False
        elif QuantiRegistros == 1:
            LoginSucesso = True
            cpf = usuarios[0][1]

        self.Desconectar()

        return LoginSucesso, cpf

    def CriarPaciente(self, paciente):

        nome = paciente[0]
        cpf  = paciente[1]

        query = f"INSERT INTO PACIENTE (NOME, CPF) VALUES( '{nome}', '{cpf}' )"

        self.Conectar()
        self.cursor.execute(query)
        self.connection.commit()
        self.Desconectar()

    def CriarMedicamento(self, medicamento):

        query = f"INSERT INTO REMEDIO (DESCRICAO) VALUES('{medicamento}')"

        self.Conectar()
        self.cursor.execute(query)
        self.connection.commit()
        self.Desconectar()

    def GetPacientes(self):

        pacientes = []

        query = f"SELECT * FROM PACIENTE"

        self.Conectar()
        self.cursor.execute(query)

        pacientesDatabase = self.cursor.fetchall()

        for paciente in pacientesDatabase:

            pacientes.append( paciente[1] + " - " +  paciente[0] )

        return pacientes

    def GetRemedios(self):


        query = "SELECT * FROM REMEDIO"

        self.Conectar()
        self.cursor.execute(query)

        remedios = self.cursor.fetchall()

        return remedios


    def GetPacientes(self):

        pacientes = []

        query = f"SELECT * FROM PACIENTE"

        self.Conectar()
        self.cursor.execute(query)

        pacientesDatabase = self.cursor.fetchall()

        for paciente in pacientesDatabase:
            pacientes.append( paciente[::-1] )

        return pacientes


    def GetPacientesAtivos(self, cpf_enfermeiro):

       query = ""
       query += "SELECT"
       query += "    PC.CPF       AS CPF ,                    "
       query += "    PC.NOME      AS NOME,                    "
       query += "    RM.DESCRICAO AS REMEDIO,                 "
       query += "    AG.HORARIO   AS HORARIO,                 "
       query += "    RM.CODIGO    AS CODREMEDIO               "
       query += " FROM PACIENTE AS PC                         "
       query += " INNER JOIN AGENDAMENTO AS AG                "
       query += "     ON AG.cpfpaciente = PC.cpf              "
       query += " INNER JOIN REMEDIO AS RM                    "
       query += "     ON RM.codigo = AG.codigoremedio         "
       query += f" WHERE AG.CPFENFERMEIRO = '{cpf_enfermeiro}'"

       self.Conectar()
       self.cursor.execute(query)
       agendamentos = self.cursor.fetchall()
       self.Desconectar()

       return agendamentos

    def CriarAgendamento( self, dados ):

        cpf_paciente = dados[0]
        horario = dados[1]
        codigo_remedio = dados[2]
        cpf_enfermeiro = dados[3]

        query = f" INSERT INTO AGENDAMENTO (CPFENFERMEIRO, CPFPACIENTE, CODIGOREMEDIO, HORARIO) VALUES( '{cpf_enfermeiro}', '{cpf_paciente}', '{codigo_remedio}', '{horario}') "

        self.Conectar()
        self.cursor.execute(query)
        self.connection.commit()
        self.Desconectar()

    def delete_medicamento(self, codigo_medicamento):

        sucesso = True
        description_error = ""

        query = f" DELETE FROM REMEDIO WHERE CODIGO = {codigo_medicamento} "

        try:
            self.Conectar()
            self.cursor.execute(query)
            self.connection.commit()
            self.Desconectar()

        except psycopg2.errors.ForeignKeyViolation as e:

                sucesso = False
                description_error = "Esse medicamento está sendo usado por algum paciente. É necessário deletar o agendamento antes."
        else:
            sucesso = True

        return sucesso, description_error

    def delete_agendamento(self, dados):

        cpf_enfermeiro = dados[0]
        cpf_paciente = dados[1]
        codigo_remedio = dados[2]
        sucesso = True
        exception = ""

        query = f"DELETE FROM AGENDAMENTO WHERE CPFENFERMEIRO = '{cpf_enfermeiro}' AND CPFPACIENTE = '{cpf_paciente}' AND CODIGOREMEDIO = {codigo_remedio} "

        try:
            self.Conectar()
            self.cursor.execute(query)
            self.connection.commit()
            self.Desconectar()

        except Exception as e:

            sucesso = False
            exception = e

        return sucesso, exception


