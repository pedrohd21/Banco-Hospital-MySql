from hospital import Medico, Paciente, Consulta
import os


if __name__ == '__main__':
    medico = Medico()
    paciente = Paciente()
    consulta = Consulta()

    print('HOSPITAL')

    while True:
        opcao = int(input("(1) Médico \n"
                          "(2) Pasciente\n"
                          "(3) Consulta\n"
                          "(4) Sair\n"
                          "Opção: "))
        print()
        if opcao == 1:
            while True:
                menu = int(input('(1) Adicionar Medico \n'
                              '(2) Atualizar Medico \n'
                              '(3) Adicionar Telefone\n'
                              '(4) Atualizar Telefone\n'
                              '(5) Apagar Medico\n'
                              '(6) Sair\n'
                              'Opção: '))
                print()
                if menu == 1:
                    print('Adicionar Médico: ')
                    nome = input('Nome: ')[0:30]
                    email = input('Email: ')[0:50]
                    medico.addMedico(nome, email)
                    os.system("cls")
                    
                if menu == 2:
                    while True:
                        vdd = False
                        lista = medico.listaMedico()
                        print(lista)
                        id = int(input('CRM Médico: '))
                        for v in lista:
                            if id == v:
                                nome = input('Nome: ')[0:30]
                                email = input('Email: ')[0:50]
                                medico.atualizar(id, nome, email)
                                print()
                                vdd = True
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um médico válido!')

                
                
                if menu == 3:
                    while True:
                        vdd = False
                        lista = medico.listaMedico()
                        print(lista)
                        id = int(input('CRM Médico: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                numero = input('Numero: ')[0:13]
                                while True:
                                    tipo = int(input('Tipo de celular: \n'
                                                '(1) Residencial\n'
                                                '(2) Comercial\n'
                                                '(3) Celular\n'
                                                'Opção: '))
                                    if tipo == 1:
                                        tipoTele = 'RES'
                                        medico.addTelefone(id, numero, tipoTele, 'id_medico')
                                        break
                                    if tipo == 2:
                                        tipoTele = 'COM'
                                        medico.addTelefone(id, numero, tipoTele, 'id_medico')
                                        break
                                    if tipo == 3:
                                        tipoTele = 'CEL'
                                        medico.addTelefone(id, numero, tipoTele, 'id_medico')
                                        break
                                    else:
                                        print('Digite um tipo valido.') 

                        if vdd == True:
                            os.system("cls")
                            break
                        else:
                            print('Digite um médico valido')

                        
                
                if menu == 4:
                    while True:
                        vdd = False
                        lista = medico.listTelefone('medico', 'idmedico', 'id_medico')
                        print(lista)
                        id = int(input('Numero cadastro telefone: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                numero = input('Numero: ')[0:13]
                                while True:
                                    tipo = int(input('Tipo de celular: \n'
                                                '(1) Residencial\n'
                                                '(2) Comercial\n'
                                                '(3) Celular\n'
                                                'Opção: '))
                                    if tipo == 1:
                                        tipoTele = 'RES'
                                        medico.telefoneAtualizar(numero, tipoTele, id)
                                        break
                                    if tipo == 2:
                                        tipoTele = 'COM'
                                        medico.telefoneAtualizar(numero, tipoTele, id)
                                        break
                                    if tipo == 3:
                                        tipoTele = 'CEL'
                                        medico.telefoneAtualizar(numero, tipoTele, id)
                                        break
                                    else:
                                        print('Digite numero cadastrado.')
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um numero cadastrado')
                        print()

                

                if menu == 5:
                    while True:
                        vdd = False
                        lista = medico.listaMedico()
                        print(lista)
                    
                        id = int(input('CRM Medico: '))
                        for v in lista:
                            if id == v:
                                medico.apagarMedico(id)
                                vdd = True
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um médico válido!')
                        print()
                                
                                

                if menu == 6:
                    os.system("cls")
                    break
        
        if opcao == 2:
            while True:
                menu = int(input('(1) Adicionar Paciente \n'
                                 '(2) Atualizar Paciente\n'
                                 '(3) Exame\n'
                                 '(4) Medicamento\n'
                                 '(5) Atualizar Medicamento\n'
                                 '(6) Endereço\n'
                                 '(7) Atualizar Endereço\n'
                                 '(8) Plano\n'
                                 '(9) Apagar Paciente\n'
                                 '(10) Sair\n'
                                 'Opção: '))
                print()

                if menu == 1:
                    print('Adicionar Paciente')
                    nome = input('Nome: ')[0:30]
                    cpf = input('CPF: ')[0:15]
                    email = input('Email: ')[0:30]
                    while True:
                        sexo = input('Masculino (M) \n(F) Feminino \n'
                                     'Opcao (M) ou (F): ').upper()
                        if sexo == 'M':
                            sexo = 'M'
                            break
                        if sexo == 'F':
                            sexo = 'F'
                            break
                        else:
                            print('Selecione uma opção valida.')
                            print()
                    paciente.addPaciente(nome, cpf, email, sexo)
                    os.system('cls')

                if menu == 2:
                    lista = paciente.listaPasciente()
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Paciente: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                nome = input('Nome: ')[0:30]
                                cpf = input('CPF: ')[0:15]
                                email = input('Email: ')[0:30]
                                while True:
                                    sexo = input('Masculino (M) \n(F) Feminino\n'
                                                 'Opcao (M) ou (F): ').upper()
                                    if sexo == 'M':
                                        sexo = 'M'
                                        break
                                    if sexo == 'F':
                                        sexo = 'F'
                                        break
                                    else:
                                        print('Selecione uma opção valida.')
                                        print()
                                paciente.atualizarPaciente(nome, cpf, email, sexo, id)

                        if vdd == True:
                            os.system("cls")
                            break
                        print('Selecione um paciente valido.')

                if menu == 3:
                    print('Exame')
                    lista = paciente.listaPasciente()
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Paciente: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                nome = input('Nome Exame: ')[0:50]
                                obs = input('Observação: ')[0:200]
                                resultado = input('Resultado: ')[0:400]
                                paciente.exame(nome, obs, resultado, id)
                                print()
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um paciente valido.')

                if menu == 4:
                    print('Medicamento')
                    lista = paciente.listaPasciente()
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Paciente: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                nome = input('Nome Remedio: ')[0:100]
                                tipo = input('Tipo medicamento: ')[0:100]
                                dosagem = input('Dosagem: ')[0:100]
                                paciente.medicamento(nome, tipo, dosagem, id)
                                print()
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um paciente valido.')

                if menu == 5:
                    print('Atualizar Medicamento')
                    lista = paciente.listaMedicamento()
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Medicamento: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                nome = input('Nome Remedio: ')
                                tipo = input('Tipo medicamento: ')
                                dosagem = input('Dosagem: ')
                                paciente.atualizarMedicamento(nome, tipo, dosagem, id)
                                print()
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um medicamento valido.')

                if menu == 6:
                    print('Endereco')
                    lista = paciente.listaPasciente()
                    # rua, cidade, estado, bairro, id
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Paciente: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                rua = input('Rua: ')[0:100]
                                cidade = input('Cidade: ')[0:100]
                                estado = input('Sigla Estado: ')[0:2]
                                bairro = input('Bairro: ')[0:100]
                                paciente.endereco(rua, cidade, estado, bairro, id)
                                print()
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um paciente valido.')

                if menu == 7:
                    print('Atualizar Endereço')
                    lista = paciente.listaEndereco()
                    # rua, cidade, estado, bairro, id
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Endereço: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                rua = input('Rua: ')[0:100]
                                cidade = input('Cidade: ')[0:100]
                                estado = input('Estado: ')[0:2]
                                bairro = input('Bairro: ')[0:100]
                                paciente.atualizarEndereco(rua, cidade, estado, bairro, id)
                                print()
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um endereço valido.')

                if menu == 8:
                    print('Plano')
                    lista = paciente.listaPasciente()
                    # tipo, id
                    print(lista)
                    while True:
                        vdd = False
                        id = int(input('Numero Cadastro Paciente: '))
                        for v in lista:
                            if id == v:
                                vdd = True
                                while True:
                                    tipo = input('Tipo plano: \n'
                                                 '(1) PREMIUM \n'
                                                 '(2) BASICO\n'
                                                 'Opção: ')
                                    if tipo == '1':
                                        tipo = 'PREMIUM'
                                        break
                                    if tipo == '2':
                                        tipo = 'BASICO'
                                        break
                                    else:
                                        print('Digite uma opção valida.')
                                        print()

                                paciente.plano(tipo, id)
                                print()
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um paciente valido.')

                if menu == 9:
                    print('Apagar Todos Dados.')
                    while True:
                        vdd = False
                        lista = paciente.listaPasciente()
                        print(lista)

                        id = int(input('Numero cadastro Paciente: '))
                        for v in lista:
                            if id == v:
                                paciente.apagarpaciente(id)
                                vdd = True
                        if vdd == True:
                            os.system("cls")
                            break
                        print('Digite um pasciente valido!')
                        print()
                
                if menu == 10:
                    os.system("cls")
                    break

        if opcao == 3:
            vdd = False
            print('Consulta')
            while True:
                opcao = input('(1) Consulta\n'
                      '(2) Atualizar Consulta \n'
                      '(3) sair \n'
                      'Opção: ')
                if opcao == '1':
                    vdd = True
                    nome = input('Nome consulta: ')
                    while True:
                        tipo = input('Tipo consulta: \n'
                                     '(1) CONSULTA\n'
                                     '(2) RETORNO\n'
                                     'Opção: ')
                        if tipo == '1':
                            tipo = 'CONSULTA'
                            break
                        if tipo == '2':
                            tipo = 'RETORNO'
                            break
                        else:
                            print('Digite uma opção valida.')

                    idPaciente = int(input('N° Paciente: '))
                    idMedico = int(input('CRM: '))
                    consulta.addConsulta(nome, tipo, idPaciente, idMedico)
                    os.system("cls")
                    break

                if opcao == '2':
                    lista = paciente.listaConsulta()
                    print(lista)
                    while True:
                        id = int(input('Numero Consulta: '))
                        vdd = False
                        for v in lista:
                            if id == v:
                                vdd = True
                                nome = input('Nome consulta: ')
                                while True:
                                    tipo = input('Tipo consulta: \n'
                                                 '(1) CONSULTA\n'
                                                 '(2) RETORNO\n'
                                                 'Opção: ')
                                    if tipo == '1':
                                        tipo = 'CONSULTA'
                                        break
                                    if tipo == '2':
                                        tipo = 'RETORNO'
                                        break
                                    else:
                                        print('Digite uma opção valida.')
                                consulta.atualizarConsulta(nome, tipo, id)
                        if vdd == True:
                            os.system('cls')
                            break
                        print('Digite uma opção valida')

                if opcao == '3':
                    os.system('cls')
                    break
                else:
                    print('Digite uma opação valida.')
        
        if opcao == 4:
            print('Obrigado Por Usar!')
            break

        # else:
        #     print('Escolha uma opção valida.')
