------------------------ OBJETIVO ------------------------

Alimentar as planilhas presente no projeto Blue_BI a par-
tir do uso de pandas/numpy e outras bibliotecas

------------------------ UPDATES ------------------------

- 17/01/2021
	. Adicionado opcao de criar planilhas 
	(Aluno e Matricula)
	. Adicionado opcao de cadastrar o aluno 
	(nao ocorre mais a falha de copiar o DataFrame adici-
	onado no momento com o anterior)
	. Adicionado opcao de cadastro da matricula
	. Adicionado opcao de listar alunos
	(Corrigido o parse que ocorria devido ao valor None 
	no atributo sep)

- 19/01/2021
	. Tratamento dos arrays
	(A primeira letra das palavras dos campos primeiro
	nome, nome completo, endereço, cidade, estado,	nome 
	do responsável, periodo e pago/em debito serão sempre 
	salvos como maíuscula)
	
- 20/01/2021
	. Alterado o nome do id_Aluno para id da tabela 
	Matricula.csv, possibilitando realizar merge com o id
	da tabela Alunos.csv
	. Alterado a 'interface' do menu principal
	. Criado o cabecalho das opcoes para uma maior clareza
	. Adicionado opção de listar alunos aprovados/reprovados
	(colunas: id, nome_completo, cursos, media e situacao)
	. Adicionado opcao de excluir alunos
	
------------------------ OBSERVA?OES ------------------------

- Ha um outro programa que permite alimentar corretamente as 
planilhas (Blue_Cadastro_Aluno) usando somente a lib csv

