from tratamento import *
import pandas as pd



def BuscadoCard(cards,datas):
  ArrayFindOK = [] 
  for i in range(0,len(cards)): 
    for a in range(0,len(cards[i]['fields'])):
     if cards[i]['fields'][a]['name'] == 'Data do Atendimento':
        #dentro de atendimento
        for b in datas:
            print('stage 3')
            if cards[i]['fields'][a]['value'] == b:
             ArrayFindOK.append(cards[i])
             break 
        break 
    
    print('QTD encontrado: ',len(ArrayFindOK))
    print(datas)
    for  i in range(0,ArrayFindOK):
       for c in range(len(ArrayFindOK[i]['fields'])):
         if ArrayFindOK[i]['fields'][c]['name'] == 'Data do Atendimento':
             print(ArrayFindOK[i]['fields'][c]['value'])
             break
 
def Introducao_Dados():
   print('==========================================================')
   print('DIA DEVE SER INFORMADO COM 2 DIGITOS E ANO COM 4 DIGITOS(2024)')
   DataInicial= input('\tINFORME A DATA INICIAL(seguir esta estrutura dd-mm-aaaa):   \t')
   DataFinal = input('\tINFORME A DATA FINAL(seguir esta estrutura dd-mm-aaaa):   \t')

   print('==========================================================')
   
   #print('\t\t\n\n Data Escolhida:  {}-{}-{}'.format(DiaInicial,Mes,Ano), ' Até {}-{}-{}'.format(DiaFinal,Mes,Ano))
   data_inicio,data_fim =DataInicial , DataFinal

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
       
       return datas_Formatadas
       

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
     
 if contador == 20:
     break
 
 print(f'{contador}/{len(List_ID)}')

print('INICANDO VIKRA2')
#print(vikra[0]['fields'])
 



print('Cards CONCLUIDOS = ',len(vikra2))


try:  
 dataFormatadas = Introducao_Dados()
 BuscadoCard(vikra2,dataFormatadas)

except:
     print("ERROR")




