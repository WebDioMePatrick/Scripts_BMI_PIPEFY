from tratamento import *

 
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



print('Cards CONCLUIDOS = ',len(vikra2))




