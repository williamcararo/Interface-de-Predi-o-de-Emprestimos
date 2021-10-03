from os import write
from typing import Text
import pandas as pd
#from pycaret.regression import load_model 
import streamlit as st
from sklearn.metrics import accuracy_score
from streamlit.proto.RootContainer_pb2 import SIDEBAR
from streamlit.proto.Slider_pb2 import Slider
import joblib


model = joblib.load('C:/Users/William Cararo/Videos/Curso - Data Science/módulo 11 - machine learning/cap06-ml-producao-materiais-apoio/notebook-dataset/model.pkl')

#Título do app
st.header("""
**Sistema de previsão de empréstimos** \n
Este Aplicativo utiliza os dados de entrada realizar a predição do modelo""")

#Cabeçalho criado
st.subheader('Informações Preenchidas:')


#nome do usuário
sexo = st.sidebar.selectbox('Sexo: ', ('Feminino', 'Masculino'))
st.write('Sexo:', sexo)
dependentes = st.sidebar.selectbox("Quantidade de dependentes",(1,2,3,('mais que 3')))
st.write('Dependentes:', dependentes)
#if x == 'mais que 3':
#    st.write('caraio mais que 3 dependentes')
#else:
#    st.write('Dependentes:', x)
casado = st.sidebar.selectbox('Casado: ', ("Sim","Não"))
st.write('Casado: ', casado)
graduado = st.sidebar.selectbox('Graduado: ', ("Sim", "Não"))
st.write('Graduação concluída: ', graduado)
trabalho = st.sidebar.selectbox('Trabalho por conta: ', ("Sim", "Não"))
st.write('Trabalho por conta: ', trabalho)
rendimento = st.sidebar.number_input("Rendimento")
if rendimento > 0:
    st.write('Rendimento informado: ', rendimento,'Reais')
else:
    st.write('Rendimento informado: ', rendimento)
valor_emprestimo = st.sidebar.number_input("Valor do emprestimos: ")
if valor_emprestimo > 0:
    st.write('Valor do empréstimo informado: ', round(valor_emprestimo,2), 'Reais')
else:
    st.write('Valor do empréstimo informado: ', valor_emprestimo)

#Transformando strings em boleanos:
graduado = 1 if graduado == "Sim" else 0
casado = 1 if casado == "Sim" else 0
sexo = 1 if sexo == "Masculino" else 0
trabalho = 1 if trabalho == "Sim" else 0


# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Predição")

# verifica se o botão foi acionado
if btn_predict:
    data_teste = pd.DataFrame()

    data_teste["sexo"] =	[sexo]
    data_teste["dependentes"] =	[dependentes]    
    data_teste["casado"] = [casado]
    data_teste["graduado"] = [graduado]	
    data_teste["trabalho"] = [trabalho]
    data_teste["rendimento"] = [rendimento]
    data_teste["valor_emprestimo"] = [valor_emprestimo]

    
   # imprime os dados de teste    
   # print(data_teste)

    #realiza a predição
    result = model.predict(data_teste) 
        #model,data = data_teste)["Label"]
    
    st.subheader("O Resultado da solicitação do emprestimo foi :")
    result = 'Aprovado. Aguarde novos detalhes sobre sua solicitação.' if result == [1] else "Negada. Tente entrar em contato com seu gerente de contas."
    
    st.write(result)

