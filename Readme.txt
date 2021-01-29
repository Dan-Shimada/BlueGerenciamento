------------------------------ OBJETIVO ------------------------------

Alimentar as planilhas presente no projeto Blue_BI a par-
tir do uso de pandas/numpy e outras bibliotecas

------------------------------ UPDATES ------------------------------

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

- 24/01/2021	
	. Refatoração do código
		. Criado as funções
			. cabecalho_matricula()
			. cabecalho_aluno()
			. maiuscula()
			. criar_dataframe_aluno()
			. criar_dataframe_matricula()
			. aprovado_reprovado()
	. Corrigido bug na opção excluir

- 25/01/2021
	. Opção de alterar as notas P1, P2, P3 e P4 foram implementadas
	(ao alterar uma das notas, a coluna de Media e Situacao são
	alterados automaticamente)
	. Opção de alterar a situacao de pagamento foi implementado
	
- 26/01/2021
	. Alterado o path dos arquivos para a pasta do Blue - Power BI
	
- 29/01/2021
	. Simplificação do menu principal
	
------------------------------ OBSERVACOES ------------------------------


