import pymysql


class Medico:
    def __init__(self):
        self.conn = pymysql.connect(db='hospital', user='root', passwd='1234')
        self.cursor = self.conn.cursor()

    def addMedico(self, nome, email):
        self.cursor.execute(f'INSERT INTO medico (nome, email) VALUES ("{nome}", "{email}")')
        self.conn.commit()

    def atualizar(self, id, nome, email):
        self.cursor.execute(f'UPDATE medico set nome = "{nome}", email= "{email}" where idmedico = "{id}"')
        self.conn.commit()

    def addTelefone(self, id, numero, tipo, id_medPas):
        self.cursor.execute(f'INSERT INTO telefone (numero, tipo, {id_medPas}) VALUES ("{numero}", "{tipo}", "{id}")')
        self.conn.commit()

    def telefoneAtualizar(self, numero, tipo, id):
        self.cursor.execute(f'UPDATE telefone set numero="{numero}", tipo="{tipo}" where idtelefone="{id}"')
        self.conn.commit()

    def listaMedico(self):
        print(f'Medico Cadastrados')
        self.cursor.execute(f'SELECT * FROM medico')
        lista = []
        print(f'{"CRM":^5} {"Nome":^15} {"Email:":^30}')
        for linha in self.cursor:
            print(f'{linha[0]:^5} {linha[1]:^15} {linha[2]:^30} ')
            lista.append(linha[0])
        return lista

    def listTelefone(self, desc1, id1, id2):
        lista = []
        print(f'{desc1} Cadastrados')
        self.cursor.execute('select t.idtelefone, m.nome, m.email, t.numero, t.tipo'
                            f' from {desc1} m'
                            ' inner join telefone t'
                            f' on m.{id1} = t.{id2}')
        
        print(f'{"N° Cadastro":^15} {"Nome":^10} {"Email":^25} {"Numero":^12} {"Tipo":^10}')
        for linha in self.cursor:
            print(f'{linha[0]:^15} {linha[1]:^10} {linha[2]:^25} {linha[3]:^12} {linha[4]:^10}')
            lista.append(linha[0])
        print()
        return lista

    def apagarMedico(self, id):
        self.cursor.execute(f'DELETE FROM telefone where id_medico = "{id}"')
        self.cursor.execute(f'DELETE FROM medico where idmedico = "{id}"')
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


class Paciente(Medico):
    def addPaciente(self, nome, cpf, email, sexo):
        self.cursor.execute(
            f'INSERT INTO paciente (nome, cpf, email, sexo) VALUES ("{nome}", "{cpf}", "{email}", "{sexo}")')
        self.conn.commit()

    def atualizarPaciente(self, nome, cpf, email, sexo, id):
        self.cursor.execute(
            f'UPDATE paciente set nome="{nome}", cpf="{cpf}", email="{email}", sexo="{sexo}" where idpaciente="{id}"')
        self.conn.commit()

    def listaPasciente(self):
        print(f'Medico Cadastrados')
        self.cursor.execute(f'SELECT * FROM paciente')
        lista = []
        print(f'{"N° Pasciente":^15} {"Nome":^15} {"Email:":^30}')
        for linha in self.cursor:
            print(f'{linha[0]:^15} {linha[1]:^15} {linha[2]:^30} ')
            lista.append(linha[0])
        return lista

    def exame(self, nome, observacao, resultado, id):
        self.cursor.execute(
            f'INSERT INTO exame (nome, observacao, resultado, id_paciente) VALUES("{nome}", "{observacao}", "{resultado}", "{id}")')
        self.conn.commit()

    def medicamento(self, nome, tipo, dosagem, id):
        self.cursor.execute(
            f'INSERT INTO medicamento(nome, tipo, dosagem, id_paciente) VALUES("{nome}", "{tipo}", "{dosagem}", "{id}")')
        self.conn.commit()

    def atualizarMedicamento(self, nome, tipo, dosagem, id):
        self.cursor.execute(
            f'UPDATE medicamento set nome="{nome}", tipo="{tipo}", dosagem="{dosagem}" where idmedicamento="{id}"')
        self.conn.commit()

    def listaMedicamento(self):
        lista = []
        print('Medicamentos: ')
        self.cursor.execute('select m.idmedicamento, m.nome, p.idpaciente, p.nome '
                            'from paciente p '
                            'inner join medicamento m '
                            'on p.idpaciente = m.id_paciente ')
        print(f'{"N° Cadastro":^15} {"Medicamento":^15} {"N° Pasciente":^15} {"Nome":^15}')
        for linha in self.cursor:
            print(f'{linha[0]:^15} {linha[1]:^15} {linha[2]:^15} {linha[3]:^15}')
            lista.append(linha[0])

        print()
        return lista


    def endereco(self, rua, cidade, estado, bairro, id):
        self.cursor.execute(
            f'INSERT INTO endereco(rua, cidade, estado, bairro, id_paciente) VALUES("{rua}", "{cidade}", "{estado}", "{bairro}", "{id}")')
        self.conn.commit()

    def atualizarEndereco(self, rua, cidade, estado, bairro, id):
        self.cursor.execute(
            f'UPDATE endereco set rua="{rua}", cidade="{cidade}", estado="{estado}", bairro="{bairro}" where idendereco="{id}"')
        self.conn.commit()

    def listaEndereco(self):
        lista = []
        print('Medicamentos: ')
        self.cursor.execute('select e.idendereco, p.idpaciente, p.nome '
                            'from paciente p '
                            'inner join endereco e '
                            'on p.idpaciente = e.id_paciente ')
        print(f'{"N° Cadastro":^15} {"N° Pasciente":^15} {"Nome":^15}')
        for linha in self.cursor:
            print(f'{linha[0]:^15} {linha[1]:^15} {linha[2]:^15}')
            lista.append(linha[0])
        print()
        return lista

    def plano(self, tipo, id):
        self.cursor.execute(f'INSERT INTO plano(tipo, id_paciente) VALUES("{tipo}", "{id}")')
        self.conn.commit()

    def listaConsulta(self):
        print(f'Consultas Cadastradas')
        self.cursor.execute(f'SELECT idconsulta, nome FROM consulta')
        lista = []
        print(f'{"N° Consulta":^15} {"Nome":^15} {"Data:":^30}')
        for linha in self.cursor:
            print(f'{linha[0]:^15} {linha[1]:^15}  ')
            lista.append(linha[0])
        return lista

    def apagarpaciente(self, id):
        self.cursor.execute(f'DELETE FROM exame where id_paciente = "{id}"')
        self.cursor.execute(f'DELETE FROM telefone where id_paciente = "{id}"')
        self.cursor.execute(f'DELETE FROM MEDICAMENTO where id_paciente = "{id}"')
        self.cursor.execute(f'DELETE FROM ENDERECO where id_paciente = "{id}"')
        self.cursor.execute(f'DELETE FROM PLANO where id_paciente = "{id}"')
        self.cursor.execute(f'DELETE FROM paciente where idpaciente = "{id}"')
        self.cursor.execute(f'DELETE FROM CONSULTA where id_paciente = "{id}"')
        self.conn.commit()


class Consulta(Medico):
    def addConsulta(self, nome, tipo, id_pasciente, id_medico):
        self.cursor.execute(f'INSERT INTO consulta(nome, tipo, id_paciente, id_medico) VALUES("{nome}", "{tipo}", "{id_pasciente}", "{id_medico}")')
        self.conn.commit()

    def atualizarConsulta(self, nome, tipo, id):
        self.cursor.execute(f'UPDATE consulta set nome="{nome}", tipo="{tipo}" where idconsulta="{id}"')
        self.conn.commit()

