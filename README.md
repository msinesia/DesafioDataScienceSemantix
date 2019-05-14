# DesafioDataScienceSemantix
DesafioDataScienceSemantix


Objetivo: saber quais clientes do banco, através de uma campanha da marketing, irão aceitar um empréstimo.
Questões a responder analisando o Data Set: 
1. Qual profissão tem mais tendência a fazer um empréstimo? De qual tipo?
2. Fazendo uma relação entre número de contatos e sucesso da campanha quais
são os pontos relevantes a serem observados?
3. Baseando-se nos resultados de adesão desta campanha qual o número médio e
o máximo de ligações que você indica para otimizar a adesão?
4. O resultado da campanha anterior tem relevância na campanha atual?
5. Qual o fator determinante para que o banco exija um seguro de crédito?
6. Quais são as características mais proeminentes de um cliente que possua
empréstimo imobiliário?

Passos:
Data Set utilizado: https://archive.ics.uci.edu/ml/datasets/bank+marketing#

1. entender o data set 
>> do que se tratam os dados
>> quantos e quais são os atributos
>> qual tipo de cada atributo
>> se há dados para treinamento e testes

2. pré processamento dos dados
>> dados treinamento
>> dados teste

3. modelo machine learning - algoritmo supervisionado (problema de classificação)
>> como o data set já está rotulado, pode ser usado um algoritmo de machine learning supervisionado, para prever quais clientes aceitaram o empréstimo

Antes de executar o script, é preciso atualizar o workspace para evitar erros ao importar os data sets:
os.chdir('INFORME_DIR')
os.getcwd()

O script foi desenvolvido usando Python (IDE Spyder). 
As bibliotecas utilizadas: 
>> pandas
>> sklearn -- https://scikit-learn.org/stable/
>> os

Referências: 
>>https://scikit-learn.org/stable/
>>https://pandas.pydata.org/

A biblioteca sklearn disponibiliza vários pacotes de algoritmos de machine learning (supervisionado, não supervisionado, semi supervisionado)

Foi utilizado o algoritmo de árvore de decisão (classificação binária) para prever quais clientes aceitaram o empréstimo
Este algoritmo se aplica para classificação binária.
Taxa de acerto: ~92%
É possível aplicar outros algoritmos supervisionados para comparar os resultados e avaliar qual o melhor classificador, exemplo:
naive bayes, svm, redes neurais

Ainda usando árvore de decisão é possível melhorar a taxa de acerto aumentando a profundidade da árvore, através do parâmetro max_depth=15
Porém, como o data set de testes são dados aleatórios do data set de treinamento, pode ocorrer overfiting do modelo.

As análises de comportamento foram realizadas utilizando Excel. Detalhes a seguir:

Questões + respostas

1. Qual profissão tem mais tendência a fazer um empréstimo? De qual tipo?
>> detalhes dos gráficos: no arquivo questao1.xlsx
>> Profissionais da área de gestão tem mais tendência a fazer empréstimos: ~25% dos resgistros que aceitaram empréstimo via campanha analisada
>> Destes, ~33% tem financiamento habitacional

2. Fazendo uma relação entre número de contatos e sucesso da campanha quais
são os pontos relevantes a serem observados?
>> detalhes dos gráficos: no arquivo questao2&3.xlsx
>> a análise foi realizada com base em ranges da quantidade de chamadas, em 3 visões
1ª considerando sucesso entre: até 10 | até 20 | até 30 | acima de 30
2ª considerando sucesso entre: até 10 | até 5
3ª considerando sucesso entre: até 2 | até 5

é possível perceber pelo gráfico que até 5 tentativas tem-se um valor considerável de sucesso: ~95%
indo mais a fundo é possível perceber que até 2 tentativas tem-se um valor alto de sucesso: ~75%

desta forma, podemos concluir que a quantidade de contatos realizados com o cliente não é fator determinante para o sucesso da campanha. Inclusive pelo fato que nos casos onde o cliente não aceitou o empréstimo, há cenários com mais de 30 chamadas realizadas !

3. Baseando-se nos resultados de adesão desta campanha qual o número médio e
o máximo de ligações que você indica para otimizar a adesão?
>> detalhes da análise no arquivo: questao2&3.xlsx
>> número médio: 5 tentativas
>> número máximo: 10 tentativas

4. O resultado da campanha anterior tem relevância na campanha atual?
>> detalhes da análise no arquivo: questao4.xlsx
>> não há uma relevância significativa, em vista que em torno de ~18% dos clientes que aceitaram a campanha anterior,
aceitaram a campanha atual.
o que poderia alterar este cenário seria a obtenção de mais detalhes do resultado da campanha anterior categorizado como
indefinido / não informado, o qual está concentrando +60% dos clientes que aceitaram a campanha atual

5. Qual o fator determinante para que o banco exija um seguro de crédito?
>> clientes com mais de um empréstimo e com saldo anual < 0: realizando uma análise considerando mais de uma dimensão
>> clientes sem crédito liberado: realizando uma análise considerando apenas uma dimensão


6. Quais são as características mais proeminentes de um cliente que possua
empréstimo imobiliário?
>> detalhes da análise: arquivo questao6.xlsx
>> este perfil de cliente:
tem idade > 30 anos
não tém crédito default
não tem saldo negativo anual
não contrata mais de um empréstimo
é um forte candidato a aceitar a campanha atual
profissão predominante : "blue-collar"
são pessoas casadas e formação predominante secundária - ensino médio 

Detalhes dos arquivos disponibilizados:
>> bank.csv : dados de testes
>> bank-full.csv: dados de treinamento
>> bank_names.txt: detalhes do data set, incluindo o dicionário dos atributos
>> dados_treinamento_tratados.xlsx: dados pré processados antes de treinar o modelo de ML
>> resultado_predicao.xlsx: dados usados nos testes com o rótulo da predição realizada pelo algoritmo mais o rótulo contido no arquivo bank.csv
>> script_.py: script em python com os passos para pré processamento, treinamento e teste do modelo de ML - árvore de decisão
>>>>> arquivo abaixo contém dados usados para análise das questões solicitadas no desafio <<<<<
>> questao1.xlsx
>> questao2&3.xlsx
>> questao4.xlsx
>> questao5.xlsx
>> questao6.xlsx


