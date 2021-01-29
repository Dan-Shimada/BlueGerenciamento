import pandas as pd
import numpy as np

def cabecalho_escola():
    lista_escolas = []
    lista_id_escola = []

    cabecalho_escola = {
        'ID_escola': lista_id_escola,
        'Escola': lista_escolas
    }

    df_cabecalho_escola = pd.DataFrame(cabecalho_escola)
    df_cabecalho_escola.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Escola.csv', header=True, index=False, sep=';')

def cabecalho_matricula():
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
        'Situacao': lista_Situacao,
    }
    df_cabecalho_Cursos_Alunos = pd.DataFrame(cabecalho_Curso_Alunos)
    df_cabecalho_Cursos_Alunos.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', header=True, index=False, sep=';')

def cabecalho_aluno():
    lista_id_aluno = []
    lista_nome = []
    lista_nome_completo = []
    lista_endereco = []
    lista_numero = []
    lista_cidade = []
    lista_estado = []
    lista_data_Nascimento = []
    lista_nome_Responsavel = []
    lista_Parcelas = []

    cabecalho_Alunos = {
        'id': lista_id_aluno,
        'Nome': lista_nome,
        'Nome_completo': lista_nome_completo,
        'Endereco': lista_endereco,
        'Numero': lista_numero,
        'Cidade': lista_cidade,
        'Estado': lista_estado,
        'Data_Nascimento': lista_data_Nascimento,
        'Nome_Responsavel': lista_nome_Responsavel,
        'Parcela': lista_Parcelas
    }
    df_cabecalho_Alunos = pd.DataFrame(cabecalho_Alunos)
    df_cabecalho_Alunos.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Alunos.csv', header=True, index=False, sep=';')

def maiuscula(lista):
    lista_aux = []
    for x in lista:
        separa = x.split(' ')
    for y in separa:
        maiuscula = y.capitalize()
        a = lista_aux.append(maiuscula)
    junta = ' '.join(lista_aux)
    lista.pop()
    lista.append(junta)

def criar_dataframe_aluno(dicio_alvo):
    df = pd.DataFrame(dicio_alvo)
    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Alunos.csv', header=False, index=False, sep=';', mode='a')

def criar_dataframe_matricula(dicio_alvo):
    df = pd.DataFrame(dicio_alvo)
    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', header=False, index=False, sep=';', mode='a')

def criar_dataframe_escola(dicio_alvo):
    df = pd.DataFrame(dicio_alvo)
    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Escola.csv', header=False, index=False, sep=';', mode='a')

def main():
    cond = True
    while cond:

        print('+---------------------------------------------------------------------------+')
        print('|                         BLUE STUDENT MANAGER                              |')
        print('+---------------------------------------------------------------------------+')
        print('| 1 - Criar planilhas                                                       |') # 1, 2, 3, 4 , 5, 6 OK
        print('| 2 - Cadastrar informacoes                                                 |')
        print('| 3 - Listar informacoes                                                    |') # IMPLEMENTAR
        print('| 4 - Excluir aluno                                                         |')
        print('| 5 - Alterar dados                                                         |')
        print('| 6 - Sair                                                                  |')
        print('+---------------------------------------------------------------------------+')
        opc = int(input('Escolha uma opcao: '))
        print('')

# CRIAR ARQUIVOS
        if opc == 1:
            print('+---------------------------------------------------------------------+')
            print('|                           CRIAR PLANILHAS                           |')
            print('+---------------------------------------------------------------------+')
            print('| 1 - Planilha Alunos                                                 |')
            print('| 2 - Planilha Matricula                                              |')
            print('| 3 - Planilha Escola                                                 |')
            print('+---------------------------------------------------------------------+')
            opc_plan = int(input('Escolha uma opcao: '))
            print('')

# CADASTRAR CABECALHO DO ALUNO
            if opc_plan == 1:
                cabecalho_aluno()

                print('Planilha Alunos criada')
                print(' ====================================================================== ', end='\n\n')

# CADASTRAR CABECALHO DA MATRICULA
            if opc_plan == 2:
                cabecalho_matricula()

                print('Planilha Matricula criada')
                print(' ====================================================================== ', end='\n\n')

# CADASTRAR CABECALHO DA ESCOLA
            if opc_plan == 3:
                cabecalho_escola()

                print('Planilha Escola criada')
                print(' ====================================================================== ', end='\n\n')


# ######################################################### CADASTRO #########################################################


        if opc == 2:
            print('+---------------------------------------------------------------------+')
            print('|                           CADASTRAR DADOS                           |')
            print('+---------------------------------------------------------------------+')
            print('| 1 - Alunos                                                          |')
            print('| 2 - Matricula                                                       |')
            print('| 3 - Escola                                                          |')
            print('+---------------------------------------------------------------------+')
            opc_cadastro = int(input('Escolha uma opcao: '))

# CADASTRAR ALUNO
            if opc_cadastro == 1:
                print('+---------------------------------------------------------------------+')
                print('|                                  ALUNO                              |')
                print('+---------------------------------------------------------------------+', end='\n\n')

                lista_id_aluno_aux = []
                lista_nome_aux = []
                lista_nome_completo_aux = []
                lista_endereco_aux = []
                lista_numero_aux = []
                lista_cidade_aux= []
                lista_estado_aux = []
                lista_data_Nascimento_aux = []
                lista_nome_Responsavel_aux = []
                lista_Parcelas_aux = []

                id_aluno = int(input('ID: '))
                lista_id_aluno_aux.append(id_aluno)

                primeiro_nome = input('Primeiro Nome: ').capitalize()
                lista_nome_aux.append(primeiro_nome)

                nomeCompleto = input('Nome Completo: ')
                lista_nome_completo_aux.append(nomeCompleto)
                maiuscula(lista_nome_completo_aux)

                rua = input('Endereco: ')
                lista_endereco_aux.append(rua)
                maiuscula(lista_endereco_aux)

                numero = int(input('Numero: '))
                lista_numero_aux.append(numero)

                cidade = input('Cidade: ')
                lista_cidade_aux.append(cidade)
                maiuscula(lista_cidade_aux)

                estado = input('Estado(SSP): ').upper()
                lista_estado_aux.append(estado)

                data_Nascimento = input('Data de Nascimento(dd/mm/yyyy): ')
                lista_data_Nascimento_aux.append(data_Nascimento)

                nome_Responsavel = input('Nome do responsavel: ')
                lista_nome_Responsavel_aux.append(nome_Responsavel)
                maiuscula(lista_nome_Responsavel_aux)

                valor_parcela = float(input('Valor da parcela: '))
                lista_Parcelas_aux.append(valor_parcela)

                aluno = {
                    'id': lista_id_aluno_aux,
                    'Nome': lista_nome_aux,
                    'Nome_completo': lista_nome_completo_aux,
                    'Endereco': lista_endereco_aux,
                    'Numero': lista_numero_aux,
                    'Cidade': lista_cidade_aux,
                    'Estado': lista_estado_aux,
                    'Data_Nascimento': lista_data_Nascimento_aux,
                    'Nome_Responsavel': lista_nome_Responsavel_aux,
                    'Parcela': lista_Parcelas_aux
                }

                criar_dataframe_aluno(aluno)

                print('')
                print('Aluno {}, de ID={}, foi cadastrado.'.format(nomeCompleto, id_aluno))
                print(' ====================================================================== ', end='\n\n')

# CADASTRAR MATRICULA
            if opc_cadastro == 2:
                print('+---------------------------------------------------------------------+')
                print('|                                MATRICULA                            |')
                print('+---------------------------------------------------------------------+')
                print('| Codigo dos cursos:                                                  |')
                print('| Basico: curso01                                                     |')
                print('| Intermediario: curso02                                              |')
                print('| Avancado: curso03                                                   |')
                print('+---------------------------------------------------------------------+', end='\n\n')

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
                maiuscula(lista_Pagamento_aux)

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

                criar_dataframe_matricula(Matricula)

                print('')
                print('Matricula do aluno de ID={} foi cadastrado'.format(id_aluno_mat))
                print(' ====================================================================== ', end='\n\n')

# CADASTRAR ESCOLAS
            if opc_cadastro == 4:
                print('+---------------------------------------------------------------------+')
                print('|                CADASTRO DE ESCOLA QUE O ALUNO ESTUDA                |')
                print('+---------------------------------------------------------------------+', end='\n\n')

                lista_escola_aux = []
                lista_id_escola_aux = []

                id_escola = int(input('ID: '))
                lista_id_escola_aux.append(id_escola)

                nome_escola = input('Escola: ').capitalize()
                lista_escola_aux.append(nome_escola)

                escola = {
                    'ID_escola': lista_id_escola_aux,
                    'Escola': lista_escola_aux
                }

                criar_dataframe_escola(escola)

                print('')
                print('Escola {} criada'.format(nome_escola))
                print(' ====================================================================== ', end='\n\n')


# ######################################################### LISTAR INFORMACOES #########################################################


        if opc == 3:
            print('+---------------------------------------------------------------------+')
            print('|                            LISTAR INFORMACOES                       |')
            print('+---------------------------------------------------------------------+')
            print('| 1 - Alunos                                                          |')
            print('| 2 - Matricula                                                       |')
            print('| 3 - Escola                                                          |')
            print('+---------------------------------------------------------------------+')
            opc_listar = int(input('Escolha uma opcao: '))

# LISTAR ALUNOS
            if opc_listar == 1:
                print('+---------------------------------------------------------------------+')
                print('|                               ALUNOS                                |')
                print('+---------------------------------------------------------------------+', end='\n\n')
                with open('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Alunos.csv', mode='r') as ReadFile:
                    df = pd.read_csv(ReadFile, sep=None, engine='python')
                    print(df)
                print('')
                print(' ====================================================================== ', end='\n\n')

# LISTAR MATRICULAS
            if opc_listar == 2:
                print('+---------------------------------------------------------------------+')
                print('|                              MATRICULA                              |')
                print('+---------------------------------------------------------------------+', end='\n\n')
                with open('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', mode='r') as ReadFile:
                    df = pd.read_csv(ReadFile, sep=None, engine='python')
                    print(df)
                print('')
                print(' ====================================================================== ', end='\n\n')

# LISTAR APROVADOS / REPROVADOS
            if opc_listar == 3:
                print('+---------------------------------------------------------------------+')
                print('|                        APROVADOS/REPROVADOS                         |')
                print('+---------------------------------------------------------------------+', end='\n\n')

                with open('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Alunos.csv', mode='r') as ReadFile:
                    df_alunos = pd.read_csv(ReadFile, sep=None, engine='python')

                    sel_alunos = df_alunos[['id','Nome_completo']]

                with open('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', mode='r') as ReadFile2:
                    df_matricula = pd.read_csv(ReadFile2, sep=None, engine='python')

                    sel_matricula = df_matricula[['id', 'Cursos', 'Media', 'Situacao']]

                merge_df = pd.merge(df_alunos.iloc[:, [0, 2]], df_matricula.iloc[:, [3, 1, 9, 10]], how='left', on ='id')
                print(merge_df)
                print('')
                print(' ====================================================================== ', end='\n\n')

# DELETAR ALUNO
        if opc == 4:
            print('+---------------------------------------------------------------------+')
            print('|                            EXCLUIR ALUNO                            |')
            print('+---------------------------------------------------------------------+', end='\n\n')

            lista_del_index = []

            df = pd.read_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Alunos.csv', sep=None, engine='python')
            deletar_aluno_index = int(input('Escreva o index do aluno a ser deletado: '))
            lista_del_index.append(deletar_aluno_index)
            dropa_linha = df.drop(lista_del_index[0], inplace=True)
            reseta_index = df.reset_index(drop=True, inplace=True)
            df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Alunos.csv', sep=';')

            print('Aluno deletado')
            print(' ====================================================================== ', end='\n\n')


# ######################################################### LISTAR INFORMACOES #########################################################


        if opc == 5:
            print('+---------------------------------------------------------------------+')
            print('|                          ALTERAR INFORMACOES                        |')
            print('+---------------------------------------------------------------------+')
            print('| 1 - Notas                                                           |')
            print('| 2 - Matricula                                                       |')
            print('+---------------------------------------------------------------------+')
            opc_alterar = int(input('Escolha uma opcao: '))

# ALTERAR NOTAS
            if opc_alterar == 1:
                print('+---------------------------------------------------------------------+')
                print('|                            ALTERAR NOTAS                            |')
                print('+---------------------------------------------------------------------+')
                print('| 1 - Alterar nota P1               |')
                print('| 2 - Alterar nota P2               |')
                print('| 3 - Alterar nota P3               |')
                print('| 4 - Alterar nota P4               |')
                print('+-----------------------------------+')
                opc_nota = int(input('Digite sua opcao: '))
                print('')

                if opc_nota == 1:

                    print('+---------------------------------------------------------------------+')
                    print('|                           ALTERAR NOTA P1                           |')
                    print('+---------------------------------------------------------------------+', end='\n\n')

                    df = pd.read_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=None, engine='python')

                    p1_col = 'P1'
                    p2_col = 'P2'
                    p3_col = 'P3'
                    p4_col = 'P4'
                    media_col = 'Media'
                    situacao_col = 'Situacao'

                    indice = int(input('indice:'))
                    p1_novo = float(input('P1: '))

                    df.loc[indice, p1_col] = p1_novo
                    nota_p2 = df.loc[indice, p2_col]
                    nota_p3 = df.loc[indice, p3_col]
                    nota_p4 = df.loc[indice, p4_col]
                    situacao_atual = df.loc[indice, situacao_col]

                    nova_media = (p1_novo + nota_p2 + nota_p3 + nota_p4) / 4
                    df.loc[indice, media_col] = nova_media

                    if nova_media >= 7:
                        df.loc[indice, situacao_col] = 'Aprovado'
                    elif nova_media < 7:
                        df.loc[indice, situacao_col] = 'Reprovado'

                    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=';', index=False)

                    print('Nota P1 do aluno de ID={} foi alterado para {}'.format(indice+1, p1_novo))
                    print(' ====================================================================== ', end='\n\n')

                if opc_nota == 2:
                    print('+---------------------------------------------------------------------+')
                    print('|                           ALTERAR NOTA P2                           |')
                    print('+---------------------------------------------------------------------+', end='\n\n')

                    df = pd.read_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=None, engine='python')

                    p1_col = 'P1'
                    p2_col = 'P2'
                    p3_col = 'P3'
                    p4_col = 'P4'
                    media_col = 'Media'
                    situacao_col = 'Situacao'

                    indice = int(input('indice:'))
                    p2_novo = float(input('P2: '))

                    nota_p1 = df.loc[indice, p1_col]
                    df.loc[indice, p2_col] = p2_novo
                    nota_p3 = df.loc[indice, p3_col]
                    nota_p4 = df.loc[indice, p4_col]
                    situacao_atual = df.loc[indice, situacao_col]

                    nova_media = (nota_p1 + p2_novo + nota_p3 + nota_p4) / 4
                    df.loc[indice, media_col] = nova_media

                    if nova_media >= 7:
                        df.loc[indice, situacao_col] = 'Aprovado'
                    elif nova_media < 7:
                        df.loc[indice, situacao_col] = 'Reprovado'

                    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=';', index=False)

                    print('Nota P2 do aluno de ID={} foi alterado para {}'.format(indice+1, p2_novo))
                    print(' ====================================================================== ', end='\n\n')

                if opc_nota == 3:
                    print('+---------------------------------------------------------------------+')
                    print('|                           ALTERAR NOTA P3                           |')
                    print('+---------------------------------------------------------------------+', end='\n\n')

                    df = pd.read_csv('Matricula.csv', sep=None, engine='python')

                    p1_col = 'P1'
                    p2_col = 'P2'
                    p3_col = 'P3'
                    p4_col = 'P4'
                    media_col = 'Media'
                    situacao_col = 'Situacao'

                    indice = int(input('indice:'))
                    p3_novo = float(input('P3: '))

                    nota_p1 = df.loc[indice, p1_col]
                    nota_p2 = df.loc[indice, p2_col]
                    df.loc[indice, p3_col] = p3_novo
                    nota_p4 = df.loc[indice, p4_col]
                    situacao_atual = df.loc[indice, situacao_col]

                    nova_media = (nota_p1 + nota_p2 + p3_novo + nota_p4) / 4
                    df.loc[indice, media_col] = nova_media

                    if nova_media >= 7:
                        df.loc[indice, situacao_col] = 'Aprovado'
                    elif nova_media < 7:
                        df.loc[indice, situacao_col] = 'Reprovado'

                    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=';', index=False)

                    print('Nota P3 do aluno de ID={} foi alterado para {}'.format(indice+1, p3_novo))
                    print(' ====================================================================== ', end='\n\n')

                if opc_nota == 4:
                    print('+---------------------------------------------------------------------+')
                    print('|                           ALTERAR NOTA P4                           |')
                    print('+---------------------------------------------------------------------+', end='\n\n')

                    df = pd.read_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=None, engine='python')

                    p1_col = 'P1'
                    p2_col = 'P2'
                    p3_col = 'P3'
                    p4_col = 'P4'
                    media_col = 'Media'
                    situacao_col = 'Situacao'

                    indice = int(input('indice:'))
                    p4_novo = float(input('P4: '))

                    nota_p1 = df.loc[indice, p1_col]
                    nota_p2 = df.loc[indice, p2_col]
                    nota_p3 = df.loc[indice, p3_col]
                    df.loc[indice, p4_col] = p4_novo
                    situacao_atual = df.loc[indice, situacao_col]

                    nova_media = (nota_p1 + nota_p2 + nota_p3 + p4_novo) / 4
                    df.loc[indice, media_col] = nova_media

                    df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=';', index=False)

                    print('Nota P4 do aluno de ID={} foi alterado para {}'.format(indice+1, p4_novo))
                    print(' ====================================================================== ', end='\n\n')

# ALTERAR SITUACAO DO PAGAMENTO
            if opc_alterar == 2:
                print('+---------------------------------------------------------------------+')
                print('|                    ALTERAR SITUACAO DO PAGAMENTO                    |')
                print('+---------------------------------------------------------------------+', end='\n\n')

                df = pd.read_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=None,
                                 engine='python')
                indice = int(input('indice:'))
                pagamento_col = 'Pagamento'
                pagamento_novo = input('Pagamento(Pago/Em Debito): ').capitalize()

                df.loc[indice, pagamento_col] = pagamento_novo
                df.to_csv('C:\\Users\\Dan\\Desktop\\Blue - Power Bi\\Cursos_Alunos.csv', sep=';', index=False)

                print('')
                print('Situacao do pagamento do aluno de ID={} foi alterado para {}'.format(indice + 1,
                                                                                            pagamento_novo))
                print(' ====================================================================== ', end='\n\n')

# SAIR
        if opc == 11:
            print('PROGRAMA FINALIZADO')
            break

main()

