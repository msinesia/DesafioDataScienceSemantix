# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:01:03 2019

@author: maria.s.matias
"""

#bibliotecas
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier

#workspace
os.chdir('C:/Users/maria.s.matias/Desktop/MestradoEachUsp/semantix/DesafioDataScienceSemantix')
os.getcwd()

#importar o data set - treinamento e teste
data_train_bank = pd.read_csv('bank-full.csv',sep=';')
data_teste_bank = pd.read_csv('bank.csv', sep=';')

#visualizar o data set - treinamento e teste
data_train_bank.head()
data_teste_bank.head()

#quantidade linhas e colunas - treinamento e teste
data_train_bank.shape
data_teste_bank.shape

#renomeando as colunas - treinamento e teste
data_train_bank.columns = ['idade','profissão','estado civil','formação','crédito liberado','saldo anual','financiamento hab',
                           'empréstimo','tipo contato','ultimo dia contato','ultimo mes contato','duraçao chamada seg.',
                          'qtd contatos realizados','diferença dias contato','contatos antes campanha','resultado campanha ant','resul campanha atual']

data_teste_bank.columns = ['idade','profissão','estado civil','formação','crédito liberado','saldo anual','financiamento hab',
                           'empréstimo','tipo contato','ultimo dia contato','ultimo mes contato','duraçao chamada seg.',
                          'qtd contatos realizados','diferença dias contato','contatos antes campanha','resultado campanha ant','resul campanha atual']

#visualizar o data set - treinamento e teste
data_train_bank.head()
data_teste_bank.head()

#remover colunas - treinamento e teste
data_train_bank.drop(['ultimo dia contato','ultimo mes contato','duraçao chamada seg.'],axis=1, inplace=True)
data_teste_bank.drop(['ultimo dia contato','ultimo mes contato','duraçao chamada seg.'],axis=1, inplace=True)

#validar dataset - treinamento e teste
data_train_bank.shape
data_teste_bank.shape

#validar dataset - treinamento e teste
data_train_bank.head()
data_teste_bank.head()

#tratar atributos categóricos - treinamento e teste
data_train_bank_cat = pd.get_dummies(data_train_bank, columns=['profissão','estado civil', 'formação', 'tipo contato', 'resultado campanha ant'])
data_teste_bank_cat = pd.get_dummies(data_teste_bank, columns=['profissão','estado civil', 'formação', 'tipo contato', 'resultado campanha ant'])

#tratar atributos binários (discretos) - treinamento e teste
data_train_bank_cat.replace({'crédito liberado': 'yes', 'financiamento hab': 'yes', 'empréstimo': 'yes', 'resul campanha atual': 'yes'}, 1, inplace = True)
data_train_bank_cat.replace({'crédito liberado': 'no', 'financiamento hab': 'no', 'empréstimo': 'no', 'resul campanha atual': 'no'}, 0, inplace = True)

data_teste_bank_cat.replace({'crédito liberado': 'yes', 'financiamento hab': 'yes', 'empréstimo': 'yes', 'resul campanha atual': 'yes'}, 1, inplace = True)
data_teste_bank_cat.replace({'crédito liberado': 'no', 'financiamento hab': 'no', 'empréstimo': 'no', 'resul campanha atual': 'no'}, 0, inplace = True)

#tratar dados coluna diferença dias contato (-1) - treinamento e teste
data_train_bank_cat.replace({'diferença dias contato': -1}, 0, inplace = True)
data_teste_bank_cat.replace({'diferença dias contato': -1}, 0, inplace = True)

#validar valores nulos - treinamento e teste
data_train_bank_cat.isnull().sum()
data_teste_bank_cat.isnull().sum()

#data set pre processado para treinamento e teste
data_train_bank_new = data_train_bank_cat
data_teste_bank_new = data_teste_bank_cat

#treinando o modelo - árvore de decisão
data_train = data_train_bank_new.drop ('resul campanha atual',axis=1)
data_class = data_train_bank_new['resul campanha atual']

model_tree = DecisionTreeClassifier(max_depth=15, random_state=0)
model_tree.fit(data_train,data_class)
model_tree.score(data_train,data_class) #~90%

#dataframe para teste sem atributo "rótulo"
data_teste_noclass = data_teste_bank_new.drop ('resul campanha atual',axis=1)
data_teste_class = data_teste_bank_new['resul campanha atual']

#testando o modelo - árvore de decisão
result_teste_bank = pd.DataFrame()
result_teste_bank = data_teste_bank 
result_teste_bank['rotulo teste'] = model_tree.predict(data_teste_noclass)
result_teste_bank.replace({'rotulo teste': 1},'yes', inplace=True)
result_teste_bank.replace({'rotulo teste': 0},'no', inplace=True)
result_teste_bank.to_excel('resultado_predicao.xlsx', index=False)
model_tree.score(data_teste_noclass,data_teste_class)

data_train_bank_new.to_excel('dados_treinamento_tratados.xlsx', index=False)
data_train_bank_new.shape

