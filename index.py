from tratamento import *
import pandas as pd
from criandoRelatorio import *



def BuscadoCard(cards,datas):
  ArrayFindOK = [] 
  contadorr  = 0
  for i in range(0,len(cards)): 
    print(f'CONTADOR  = {contadorr}          CARDS LEM  = {len(cards)}')
    contadorr = contadorr +1
    for a in range(0,len(cards[i]['fields'])):
     if cards[i]['fields'][a]['name'] == 'Data do Atendimento':
        #dentro de atendimento
        for b in datas:
            if cards[i]['fields'][a]['value'] == b:
             ArrayFindOK.append(cards[i])
             print('stage 3')
             break
             
        
    
  print('QTD encontrado: ',len(ArrayFindOK))
  return ArrayFindOK
"""r,

    for  i in range(0,len(ArrayFindOK)):
       for c in range(len(ArrayFindOK[i]['fields'])):
         if ArrayFindOK[i]['fields'][c]['name'] == 'Data do Atendimento':
             print(ArrayFindOK[i]['fields'][c]['value'])
             break
""" 
def Introducao_Dados():
   print('==========================================================')
   print('DIA DEVE SER INFORMADO COM 2 DIGITOS E ANO COM 4 DIGITOS(2024)')
   DataInicial= input('\tINFORME A DATA INICIAL(seguir esta estrutura dd-mm-aaaa):   \t')
   DataFinal = input('\tINFORME A DATA FINAL(seguir esta estrutura dd-mm-aaaa):   \t')

   print('==========================================================')
   
   #print('\t\t\n\n Data Escolhida:  {}-{}-{}'.format(DiaInicial,Mes,Ano), ' Até {}-{}-{}'.format(DiaFinal,Mes,Ano))
   data_inicio,data_fim =DataInicial , DataFinal
   #data_inicio = '01-04-2024'
   #data_fim = '01-05-2024'

   try:
       data_inicio = pd.to_datetime(data_inicio, format='%d-%m-%Y')
       data_fim = pd.to_datetime(data_fim, format='%d-%m-%Y')
       
       # Garantindo que a data de início seja anterior ou igual à data de fim
       if data_inicio > data_fim:
           raise ValueError("A data de início deve ser anterior ou igual à data de fim.")
       
       # Criando uma série de datas entre o intervalo especificado
       datas = pd.date_range(start=data_inicio, end=data_fim)
       
       # Convertendo a série de datas para uma lista e imprimindo
       lista_datas = datas.tolist()
       datas_Formatadas = []
       for data in lista_datas:
           datas_Formatadas.append(data.strftime('%d-%m-%Y'))
       
       
       return datas_Formatadas,data_inicio,data_fim
       

   except ValueError as ve:
       print(f"Erro de valor: {ve}")
   except Exception as e:
       print(f"Ocorreu um erro: {e}")
       
   
       
       
    

 
lista_id_inicial_pagina = AfterInitial()
lista_afters = After()
listas_de_ids_parcial = CapturedID(lista_afters)

List_ID = lista_id_inicial_pagina + listas_de_ids_parcial
print(len(List_ID))




vikra2 = []
contador = 0
print(f"CARREGANDO INFORMAÇÕES DOS CARDS DO PIPE = {pipe_id}")
for i in List_ID:
 vikra2.append(Analisador_ID_CARD(f"{i}"))
 try:
     vikra2.remove(False)
     contador = contador + 1
 except:
     contador = contador + 1
     
 
 print(f'{contador}/{len(List_ID)}')

print('INICANDO VIKRA2')
#print(vikra[0]['fields'])
#print(vikra2)
 



print('Cards CONCLUIDOS = ',len(vikra2))


def Dtwo(array):
    nome = []
    date_of_atendimento = []
    
    for a in range(0,len(array)):
        for i in range(0,len(array[a]['fields'])):
            if array[a]['fields'][i]['name'] == 'Nome do MEI':
                nome.append(array[a]['fields'][i]['value'])
            elif array[a]['fields'][i]['name'] == 'Data do Atendimento':
                date_of_atendimento.append(array[a]['fields'][i]['value'])
                
    for i in range(0,len(nome)):
        print(f'\tNomes : {nome[i]} \tData de Atendimento: {date_of_atendimento[i]}')
            
            
    return nome,date_of_atendimento
            

dataFormatadas,data_inicio,data_fim = Introducao_Dados()
lista_de_cards_filtrados = BuscadoCard(vikra2,dataFormatadas)
print('TAMANHO = ',len(lista_de_cards_filtrados))
nome,DataDeAtendimento = Dtwo(lista_de_cards_filtrados)

criar_relatorio(Tituloo='Relatorio BMI MicroCredito',periodo=f'Periodo que Foi Determinado: {data_inicio.strftime('%d-%m-%Y')} / {data_fim.strftime('%d-%m-%Y')}',Nome=nome,DataDoAtendimento=DataDeAtendimento)




