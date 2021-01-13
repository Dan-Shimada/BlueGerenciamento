import pandas as pd

#lista_cabecalho = ['id', 'Nome', 'Nome_completo', 'Endereco', 'Numero', 'Cidade', 'Estado', 'Data_Nascimento', 'Nome_Responsavel']
lista_id_aluno = []
lista_nome = []
lista_nome_completo = []
lista_rua = []
lista_numero = []
lista_cidade = []
lista_estado = []
lista_data_Nascimento = []
lista_nome_Responsavel = []

def appendDFToCSV_void(df, csvFilePath, sep=";"):
    import os
    if not os.path.isfile('alunos_teste_2.csv'):
        df.to_csv('alunos_teste_2.csv', mode='a', index=False, sep=sep, header=True)
    elif len(df.columns) != len(pd.read_csv('alunos_teste_2.csv', nrows=1, sep=sep).columns):
        raise Exception("Columns do not match!! Dataframe has " + str(
            len(df.columns)) + " columns. CSV file has " + str(
            len(pd.read_csv('alunos_teste_2.csv', nrows=1, sep=sep).columns)) + " columns.")
    elif not (df.columns == pd.read_csv('alunos_teste_2.csv', nrows=1, sep=sep).columns).all():
        raise Exception("Columns and column order of dataframe and csv file do not match!!")
    else:
        df.to_csv('alunos_teste_2.csv', mode='a', index=False, sep=sep, header=False)

def main():
    cond = True
    while cond:

        print("#####################################")
        print("#      BLUE STUDENT MANAGER         #")
        print("#####################################")
        print("| 1 - Cadastrar aluno               |")
        print("| 2 - Listar alunos                 |")
        print("| 3 - Excluir aluno                 |")
        print("| 4 - Cadstrar matricula            |")
        print("| 5 - Alterar notas                 |")
        print("| 6 - Alterar situacao do pagamento |")
        print("| 7 - Sair                          |")
        print("|___________________________________|")
        opc = int(input("Escolha uma opcao: "))

        if opc == 1:
            print('Para voltar no meu anterior, digite -1')

            id_aluno = int(input("ID: "))

            if id_aluno == -1:
                print('Cadastro finalizado.')
                break
            lista_id_aluno.append(id_aluno)

            primeiro_nome = input("Primeiro Nome: ")
            lista_nome.append(primeiro_nome)

            nomeCompleto = input("Nome Completo: ")
            lista_nome_completo.append(nomeCompleto)

            rua = input("Endereco: ")
            lista_rua.append(rua)

            numero = int(input("Numero: "))
            lista_numero.append(numero)

            cidade = input("Cidade: ")
            lista_cidade.append(cidade)

            estado = input("Estado: ")
            lista_estado.append(estado)

            data_Nascimento = input("Data de Nascimento: ")
            lista_data_Nascimento.append(data_Nascimento)

            nome_Responsavel = input("Nome do responsavel: ")
            lista_nome_Responsavel.append(nome_Responsavel)

            dados_alunos = list(zip(lista_id_aluno, lista_nome, lista_nome_completo, lista_rua, lista_numero, lista_cidade, lista_estado, lista_data_Nascimento, lista_nome_Responsavel))

            df = pd.DataFrame(dados_alunos, columns=
            [
                'id',
                'Nome',
                'Nome_completo',
                'Endereco',
                'Numero',
                'Cidade',
                'Estado',
                'Data_Nascimento',
                'Nome_Responsavel'
            ])
            appendDFToCSV_void(df, 'alunos_teste_2.csv', sep=';')

            #df.to_csv('alunos_teste_2.csv', index=False, sep=';', header=True)

        if opc == 2: # OK
            with open('alunos_teste_2.csv', mode='r') as ReadFile:
                df = pd.read_csv(ReadFile, sep=None)
                print(df)

            #Location = r'C:\Users\Dan\Desktop\Blue_Cadastro_2\alunos_teste_2.csv'
            #df = pd.read_csv(Location)
            #print(df)

        if opc == 3: # OK
            deletar_aluno_index = int(input('Escreva o index do aluno a ser deletado: '))
            df.drop(deletar_aluno_index, inplace=True)
            a = pd.DataFrame(df)
            a.to_csv('alunos_teste_2.csv', sep=';')
            #df.to_csv('alunos_teste_3.csv', index=False)
            print("Aluno deletado")
        if opc == 7:
            break

main()