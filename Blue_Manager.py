import pandas as pd
import numpy as np


def main():
    cond = True
    while cond:

        print('+---------------------------------------------------------------------+')
        print('|                         BLUE STUDENT MANAGER                        |')
        print('+---------------------------------------------------------------------+')
        print('| 1 - Criar planilhas               6 - Lista de Aprovados/Reprovados |') # 1, 2, 3, 4, 5, 6, 7,10 OK
        print('| 2 - Cadastrar aluno               7 - Excluir aluno                 |')
        print('| 3 - Cadastrar matricula           8 - Alterar notas                 |') # 8, 9           IMPLEMENTAR
        print('| 4 - Listar alunos                 9 - Alterar situacao do pagamento |')
        print('| 5 - Listar matriculas            10 - Sair                          |')
        print('+---------------------------------------------------------------------+')
        opc = int(input('Escolha uma opcao: '))
        print('')

# CRIAR ARQUIVOS
        if opc == 1:
            print('+---------------------------------------------------------------------+')
            print('|                           CRIAR PLANILHAS                           |')
            print('+---------------------------------------------------------------------+')
            print('| 1 - Criar planilha Alunos                                           |')
            print('| 2 - Criar planilha Matricula                                        |')
            print('+---------------------------------------------------------------------+')
            opc_plan = int(input('Escolha uma opcao: '))
            print('')

# CADASTRAR CABECALHO DO ALUNO
            if opc_plan == 1:
                lista_id_aluno = []
                lista_nome = []
                lista_nome_completo = []
                lista_endereco = []
                lista_numero = []
                lista_cidade = []
                lista_estado = []
                lista_data_Nascimento = []
                lista_nome_Responsavel = []

                cabecalho_Alunos = {
                    'id': lista_id_aluno,
                    'Nome': lista_nome,
                    'Nome_completo': lista_nome_completo,
                    'Endereco': lista_endereco,
                    'Numero': lista_numero,
                    'Cidade': lista_cidade,
                    'Estado': lista_estado,
                    'Data_Nascimento': lista_data_Nascimento,
                    'Nome_Responsavel': lista_nome_Responsavel
                }
                df_cabecalho_Alunos = pd.DataFrame(cabecalho_Alunos)
                df_cabecalho_Alunos.to_csv('Alunos.csv', header=True, index=False, sep=';')
                print('')
                print('Planilha Alunos criada')
                print('')
                print(' ====================================================================== ')
                print('')

# CADASTRAR CABECALHO DA MATRICULA
            if opc_plan == 2:
                lista_Cod = []
                lista_Cursos = []
                lista_Horario = []
                lista_id_Aluno = []
                lista_Pagamento = []
                lista_P1 = []
                lista_P2 = []
                lista_P3 = []
                lista_P4 = []
                lista_Media = []
                lista_Situacao = []

                cabecalho_Curso_Alunos = {
                    'Cod': lista_Cod,
                    'Cursos': lista_Cursos,
                    'Horario': lista_Horario,
                    'id': lista_id_Aluno,
                    'Pagamento': lista_Pagamento,
                    'P1': lista_P1,
                    'P2': lista_P2,
                    'P3': lista_P3,
                    'P4': lista_P4,
                    'Media': lista_Media,
                    'Situacao': lista_Situacao
                }
                df_cabecalho_Cursos_Alunos = pd.DataFrame(cabecalho_Curso_Alunos)
                df_cabecalho_Cursos_Alunos.to_csv('Matricula.csv', header=True, index=False, sep=';')
                print('')
                print('Planilha Matricula criada')
                print('')
                print(' ====================================================================== ')
                print('')

# CADASTRAR ALUNO
        if opc == 2:
            print('+---------------------------------------------------------------------+')
            print('|                          CADASTRO DE ALUNO                          |')
            print('+---------------------------------------------------------------------+')
            print('')
            lista_id_aluno_aux = []
            lista_nome_aux = []
            lista_nome_completo_aux = []
            lista_endereco_aux = []
            lista_numero_aux = []
            lista_cidade_aux= []
            lista_estado_aux = []
            lista_data_Nascimento_aux = []
            lista_nome_Responsavel_aux = []

            nomeCompleto_aux = []

            id_aluno = int(input('ID: '))
            lista_id_aluno_aux.append(id_aluno)

            primeiro_nome = input('Primeiro Nome: ').capitalize()
            lista_nome_aux.append(primeiro_nome)

            nomeCompleto = input('Nome Completo: ')
            lista_nome_completo_aux.append(nomeCompleto)

            for x in lista_nome_completo_aux:
                separa = x.split(' ')
                for y in separa:
                    maiuscula = y.capitalize()
                    a = nomeCompleto_aux.append(maiuscula)
            junta = ' '.join(nomeCompleto_aux)
            lista_nome_completo_aux.pop()
            lista_nome_completo_aux.append(junta)

            rua = input('Endereco: ').capitalize()
            lista_endereco_aux.append(rua)

            numero = int(input('Numero: '))
            lista_numero_aux.append(numero)

            cidade = input('Cidade: ').capitalize()
            lista_cidade_aux.append(cidade)

            estado = input('Estado(SSP): ').upper()
            lista_estado_aux.append(estado)

            data_Nascimento = input('Data de Nascimento(dd/mm/yyyy): ')
            lista_data_Nascimento_aux.append(data_Nascimento)

            nome_Responsavel = input('Nome do responsavel: ').capitalize()
            lista_nome_Responsavel_aux.append(nome_Responsavel)

            #dados_alunos = list(zip(lista_id_aluno, lista_nome, lista_nome_completo, lista_rua, lista_numero, lista_cidade, lista_estado, lista_data_Nascimento, lista_nome_Responsavel))
            aluno = {
                'id': lista_id_aluno_aux,
                'Nome': lista_nome_aux,
                'Nome_completo': lista_nome_completo_aux,
                'Endereco': lista_endereco_aux,
                'Numero': lista_numero_aux,
                'Cidade': lista_cidade_aux,
                'Estado': lista_estado_aux,
                'Data_Nascimento': lista_data_Nascimento_aux,
                'Nome_Responsavel': lista_nome_Responsavel_aux
            }
            df_aluno = pd.DataFrame(aluno)
            # appendDFToCSV_void(df, 'alunos_teste_2.csv', sep=';')
            df_aluno.to_csv('Alunos.csv', header=False, index=False, sep=';', mode='a')
            print('')
            print('Aluno {}, de ID={}, foi cadastrado.'.format(nomeCompleto, id_aluno))
            print('')
            print(' ====================================================================== ')
            print('')

# CADASTRAR MATRICULA
        if opc == 3:
            print('+---------------------------------------------------------------------+')
            print('|                        CADASTRO DA MATRICULA                        |')
            print('+---------------------------------------------------------------------+')
            print('| Codigo dos cursos:                                                  |')
            print('| Basico: curso01                                                     |')
            print('| Intermediario: curso02                                              |')
            print('| Avancado: curso03                                                   |')
            print('+---------------------------------------------------------------------+')
            print('')
            lista_Cod_aux = []
            lista_Cursos_aux = []
            lista_Horario_aux = []
            lista_id_Aluno_aux = []
            lista_Pagamento_aux = []
            lista_P1_aux = []
            lista_P2_aux = []
            lista_P3_aux = []
            lista_P4_aux = []
            lista_Media_aux = []
            lista_Situacao_aux = []

            cod_mat = input('Codigo da matricula: ')
            lista_Cod_aux.append(cod_mat)

            if cod_mat == 'curso01':
                curso_mat = 'Basico'
            elif cod_mat == 'curso02':
                curso_mat = 'Intermediario'
            elif cod_mat == 'curso03':
                curso_mat = 'Avancado'
            lista_Cursos_aux.append(curso_mat)
            print('Curso: {}'.format(curso_mat))

            horario_mat = input('Periodo: ').capitalize()
            lista_Horario_aux.append(horario_mat)

            id_aluno_mat = int(input('ID aluno: '))
            lista_id_Aluno_aux.append(id_aluno_mat)

            pagamento_mat = input('Pago/Em Debito: ').capitalize()
            lista_Pagamento_aux.append(pagamento_mat)

            p1_mat = float(input('P1: '))
            lista_P1_aux.append(p1_mat)

            p2_mat = float(input('P2: '))
            lista_P2_aux.append(p2_mat)

            p3_mat = float(input('P3: '))
            lista_P3_aux.append(p3_mat)

            p4_mat = float(input('P4: '))
            lista_P4_aux.append(p4_mat)

            if p1_mat == 0.0 and p2_mat == 0.0 and p3_mat == 0.0 and p4_mat == 0.0:
                media_mat = 0.0
                situacao_mat = 'Reprovado'
            else:
                media_mat = (p1_mat + p2_mat + p3_mat + p4_mat) / 4.0

            lista_Media_aux.append(media_mat)
            print('Media: {:.2f}'.format(media_mat))

            if media_mat >= 7.0:
                situacao_mat = 'Aprovado'
            elif media_mat < 7.0:
                situacao_mat = 'Reprovado'

            lista_Situacao_aux.append(situacao_mat)
            print('Situacao: {}'.format(situacao_mat))

            Matricula = {
                'Cod': lista_Cod_aux,
                'Cursos': lista_Cursos_aux,
                'Horario': lista_Horario_aux,
                'id_Aluno': lista_id_Aluno_aux,
                'Pagamento': lista_Pagamento_aux,
                'P1': lista_P1_aux,
                'P2': lista_P2_aux,
                'P3': lista_P3_aux,
                'P4': lista_P4_aux,
                'Media': lista_Media_aux,
                'Situacao': lista_Situacao_aux
            }
            df_cabecalho_Cursos_Alunos = pd.DataFrame(Matricula)
            df_cabecalho_Cursos_Alunos.to_csv('Matricula.csv', header=False, index=False, sep=';', mode='a')
            print('')
            print('Matricula do aluno de ID={} foi cadastrado'.format(id_aluno_mat))
            print(' ====================================================================== ')
            print('')

# LISTAR ALUNOS
        if opc == 4:
            print('+---------------------------------------------------------------------+')
            print('|                               ALUNOS                                |')
            print('+---------------------------------------------------------------------+')
            print('')
            with open('Alunos.csv', mode='r') as ReadFile:
                df = pd.read_csv(ReadFile, sep=None, engine='python')
                print(df)
            print('')
            print(' ====================================================================== ')
            print('')

# LISTAR MATRICULAS
        if opc == 5:
            print('+---------------------------------------------------------------------+')
            print('|                              MATRICULA                              |')
            print('+---------------------------------------------------------------------+')
            print('')
            with open('Matricula.csv', mode='r') as ReadFile:
                df = pd.read_csv(ReadFile, sep=None, engine='python')
                print(df)
            print('')
            print(' ====================================================================== ')
            print('')

# LISTAR APROVADOS / REPROVADOS
        if opc == 6:
            print('+---------------------------------------------------------------------+')
            print('|                        APROVADOS/REPROVADOS                         |')
            print('+---------------------------------------------------------------------+')
            print('')
            with open('Alunos.csv', mode='r') as ReadFile:
                df_alunos = pd.read_csv(ReadFile, sep=None, engine='python')

                sel_alunos = df_alunos[['id','Nome_completo']]

            with open('Matricula.csv', mode='r') as ReadFile2:
                df_matricula = pd.read_csv(ReadFile2, sep=None, engine='python')

                sel_matricula = df_matricula[['id', 'Cursos', 'Media', 'Situacao']]

            merge_df = pd.merge(df_alunos.iloc[:, [0, 2]], df_matricula.iloc[:, [3, 1, 9, 10]], how='left', on ='id')
            print(merge_df)
            print('')
            print(' ====================================================================== ')
            print('')

# DELETAR ALUNO
        if opc == 7:
            print('+---------------------------------------------------------------------+')
            print('|                            EXCLUIR ALUNO                            |')
            print('+---------------------------------------------------------------------+')
            print('')
            deletar_aluno_index = int(input('Escreva o index do aluno a ser deletado: '))
            df.drop(deletar_aluno_index, inplace=True)
            a = pd.DataFrame(df)
            a.to_csv('Alunos.csv', sep=';')
            #df.to_csv('alunos_teste_3.csv', index=False)
            print('Aluno deletado')
            print(' ====================================================================== ')
            print('')

# ALTERAR NOTAS
        if opc == 8:
            print('+---------------------------------------------------------------------+')
            print('|                            ALTERAR NOTAS                            |')
            print('+---------------------------------------------------------------------+')
            print('| 1 - Alterar nota P1               |')
            print('| 2 - Alterar nota P2               |')
            print('| 3 - Alterar nota P3               |')
            print('| 4 - Alterar nota P4               |')
            print('+-----------------------------------+')
            opc_nota = int(input('Digite sua opcao: '))

            if opc_nota == 1:
                '''
                print('+---------------------------------------------------------------------+')
                print('|                           ALTERAR NOTA P1                           |')
                print('+---------------------------------------------------------------------+')

                select_index = int(input('Digite o indice do aluno: '))

                df = pd.read_csv('Matricula.csv')
                new_p1 = float(input('P1: '))
                df.iloc[select_index - 1, 5] = new_p1
                #df.to_csv('Matricula.csv', header=False, index=False, sep=';')
                '''
            if opc_nota == 2:
                print('+---------------------------------------------------------------------+')
                print('|                           ALTERAR NOTA P2                           |')
                print('+---------------------------------------------------------------------+')
            if opc_nota == 3:
                print('+---------------------------------------------------------------------+')
                print('|                           ALTERAR NOTA P3                           |')
                print('+---------------------------------------------------------------------+')
            if opc_nota == 4:
                print('+---------------------------------------------------------------------+')
                print('|                           ALTERAR NOTA P4                           |')
                print('+---------------------------------------------------------------------+')
                '''
                select_index = int(input('Digite o indice do aluno: '))
                df = pd.read_csv('Matricula.csv')
                new_p4 = float(input('P1: '))
                df.at[select_index - 1, 'P1'] = new_p4
                df.to_csv('Matricula.csv', header=False, index=False, sep=';')

                print('')
                print(' ====================================================================== ')
                '''

# ALTERAR SITUACAO DO PAGAMENTO
        if opc == 9:
            pass
# SAIR
        if opc == 10:
            break

main()

