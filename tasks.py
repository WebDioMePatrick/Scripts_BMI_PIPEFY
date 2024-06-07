from tratamento import *


listaa = [919110064,929205460,858794288,858092179]

a = []
for i in listaa:
 a.append(Analisador_ID_CARD(f'{i}'))
 try:
     a.remove(False)
 except:
  continue
 



print(len(a))

petr = a[0]
print(petr[0]['created_at'])

horario = petr[0]['created_at']

#2024-05-17T01:14:35Z
horario[5]+horario[6]#dia
horario[8]+horario[9] #mes
horario[0]+horario[1]+horario[2]+horario[3] # ano


