from tratamento import *


listaa = [919110064,929205460,858794288,858092179]

a = []
for i in listaa:
 a.append(Analisador_ID_CARD(f'{i}'))
 try:
     a.remove(False)
 except:
  continue
 

#print(len(a))
#print(a[0][0]['created_at'])



def BuscadoCard(cards,datas):
  
  for i in range(len(cards)):
    for a in datas:
     if cards[i][0]['created_at'] == a:
       print('datas iguais: ',a)
       break
     
     
datas = ['17-02-2022','18-02-2022','17-05-2024','18-02-2023']
  
BuscadoCard(a,datas)