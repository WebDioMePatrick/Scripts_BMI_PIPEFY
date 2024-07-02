from tratamento import *
import pandas as pd
from criandoRelatorio import *
import os



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
   print('==========================================================ByPatrick')
   print('DIA DEVE SER INFORMADO COM 2 DIGITOS E ANO COM 4 DIGITOS(2024)')
   DataInicial= input('\tINFORME A DATA INICIAL(seguir esta estrutura dd-mm-aaaa):   \t')
   DataFinal = input('\tINFORME A DATA FINAL(seguir esta estrutura dd-mm-aaaa):   \t')

   print('==========================================================')
   
   data_inicio,data_fim =DataInicial , DataFinal
   #data_inicio = '01-04-2024'
   #data_fim = '30-04-2024'

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
     
 
 print(f'CARREGANDO CARDS DO PIPE: {contador}/{len(List_ID)}')

print('INICANDO VIKRA2')
#print(vikra[0]['fields'])
#print(vikra2)
 



print('Cards CONCLUIDOS = ',len(vikra2))


def Dtwo(array):
    nome = []
    date_of_atendimento = []
    valorTotal = []
    
    for a in range(0, len(array)):
        nome_val = 'campo vazio no card'
        date_val = 'campo vazio no card'
        valor_val = 'campo vazio no card'
    
        for i in range(0, len(array[a]['fields'])):
            field_name = array[a]['fields'][i]['name']
            field_value = array[a]['fields'][i]['value']
    
            if field_name == 'Nome do MEI':
                nome_val = field_value
            elif field_name == 'Data do Atendimento':
                date_val = field_value
            elif field_name == 'Qual pagamento deve ser realizado?':
                if field_value != '' and field_value is not None:
                    valor_val = field_value
                else:
                    valor_val = 'campo vazio no card'
    
        nome.append(nome_val)
        date_of_atendimento.append(date_val)
        valorTotal.append(valor_val)
        
            
        for i in range(0,len(nome)):
            print(f'\tNomes : {nome[i]} \tData de Atendimento: {date_of_atendimento[i]}')
            
        
        
        print(F'LEN NAME = {len(nome)}')
        
        print(F'LEN DATE DE ATENDIMENTO = {len(date_of_atendimento)}')
        
        print(F'LEN VALOR = {len(valorTotal)}')
        print(valorTotal)
    
              
    return nome,date_of_atendimento,valorTotal
            




dataFormatadas,data_inicio,data_fim = Introducao_Dados()
lista_de_cards_filtrados = BuscadoCard(vikra2,dataFormatadas)
print('TAMANHO = ',len(lista_de_cards_filtrados))
nome,DataDeAtendimento,valorTotal = Dtwo(lista_de_cards_filtrados)

if len(nome) and len(DataDeAtendimento)and len(valorTotal) != 0:
 os.system('cls')
 sucess = criar_relatorio(Tituloo='Relatorio BMI MicroCredito',periodo=f'{data_inicio.strftime('%d-%m-%Y')} / {data_fim.strftime('%d-%m-%Y')}',Nome=nome,DataDoAtendimento=DataDeAtendimento,valor=valorTotal,INICIO=data_inicio.strftime('%d-%m-%Y'),FIM=data_fim.strftime('%d-%m-%Y'))
 print(sucess)
elif len(nome) == 0:
            os.system('cls')
            print("\t\t\n\nNão ha dados especificados nesse periodo\n\n")

print('\n\n=================================================================BYPatrick')
continuar  = input('\t\tDeseja Continuar   (1:Sim)(0:Não):\t')

if continuar == '1':
    os.system('cls')
    while continuar =='1':
        dataFormatadas,data_inicio,data_fim = Introducao_Dados()
        lista_de_cards_filtrados = BuscadoCard(vikra2,dataFormatadas)
        print('TAMANHO = ',len(lista_de_cards_filtrados))
        nome,DataDeAtendimento,valorTotal = Dtwo(lista_de_cards_filtrados)

        if len(nome) and len(DataDeAtendimento)and len(valorTotal) != 0:
         sucess = criar_relatorio(Tituloo='Relatorio BMI MicroCredito',periodo=f'{data_inicio.strftime('%d-%m-%Y')} / {data_fim.strftime('%d-%m-%Y')}',Nome=nome,DataDoAtendimento=DataDeAtendimento,valor=valorTotal,INICIO=data_inicio.strftime('%d-%m-%Y'),FIM=data_fim.strftime('%d-%m-%Y'))
         print(sucess)
        elif len(nome) == 0:
            os.system('cls')
            print("\t\t\n\nNão ha dados especificados nesse periodo\n\n")
            
        print('\n\n=================================================================BYPatrick')
        continuar  = input('\t\tDeseja Continuar   (1:Sim)(0:Não):\t')

if continuar == '0':
    os.system('exit')