import requests
import json
import pandas as pd
import time
from collections import OrderedDict

url = "https://api.pipefy.com/graphql"
token = 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MTc2OTQzNjksImp0aSI6IjA1ZmM3ZWVmLTVmNTYtNGQwOC04ODlkLTQxYTE2MzRmMTJjZCIsInN1YiI6MzA0MTgzNzk4LCJ1c2VyIjp7ImlkIjozMDQxODM3OTgsImVtYWlsIjoicHJvamV0b2JhaGlhbWVpQGdtYWlsLmNvbSJ9fQ.y1QnXR1u9wTtaxWs6vIjFklc0BxMisnRmxuFnwkw3p3v0QYSdmfTsPDbzrBZI2SZXBleILEVjh-ev5gBGUrQTQ'



headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
pipe_id = "303861827"
dataBaseId = []

def AllCards(pipe_id,after):
 query2 = f"""
 {{
   allCards(pipeId: {pipe_id} , first: 50, after:"{after}"){{
     pageInfo {{
       hasNextPage
       endCursor
     }}
     edges {{
       node {{
         id
       }}
     }}
   }}
 }}
 """
 response = requests.post(url, headers=headers, json={"query": query2})
 data = response.json()['data']['allCards']['edges']
 for i in data:
   dataBaseId.append(i['node']['id'])
 DataBaseIdOffDuplicate = list(OrderedDict.fromkeys(dataBaseId))
 return DataBaseIdOffDuplicate


dataBaseAfter = []
def AnaliseAfter():
 ResponseInit= f"""
  {{
    allCards(pipeId:{pipe_id}, first: 50){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
  
 response = requests.post(url, headers=headers, json={"query": ResponseInit})
 init = response.json()['data']['allCards']
 control = init
 while control['pageInfo']['hasNextPage'] == True:
   cursor = control['pageInfo']['endCursor']
   print(cursor)

   dataBaseAfter.append(cursor)
   OuterAfter= f"""
  {{
    allCards(pipeId:{pipe_id}, first: 50, after: "{cursor}"){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
   response = requests.post(url, headers=headers, json={"query": OuterAfter})
   control = (response.json()['data']['allCards'])



 return dataBaseAfter


def Init(pipe_id):
 query = f"""
  {{
    allCards(pipeId:{pipe_id},first: 50){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
 response = requests.post(url, headers=headers, json={"query": query})
 
 
 print(response.json())


def After():
 query3 = f"""
  {{
    allCards(pipeId:{pipe_id},first: 50){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
 response = requests.post(url, headers=headers, json={"query": query3})
 controlador = response.json()['data']['allCards']
 databaseAA = []
 
 while controlador['pageInfo']['hasNextPage'] == True:
     databaseAA.append(controlador['pageInfo']['endCursor'])
     print(controlador['pageInfo']['endCursor'])
     
     QueryAtualized = f"""
  {{
    allCards(pipeId:{pipe_id},first: 50,after:"{controlador['pageInfo']['endCursor']}"){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
     response = requests.post(url, headers=headers, json={"query": QueryAtualized})
     controlador = (response.json()['data']['allCards'])
     
     
 DataBaseOfDuplicate = list(OrderedDict.fromkeys(databaseAA))
 print(len(databaseAA)) 
 return DataBaseOfDuplicate
     
     
  
def CapturedID(after):
 dataBaseId = []
  
 for i in after:
  query = f"""
  {{
    allCards(pipeId:{pipe_id},first: 50,after:"{i}"){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
  
  response = requests.post(url, headers=headers, json={"query": query})
  data = response.json()['data']['allCards']['edges']
 
  for i in data:
     dataBaseId.append(i['node']['id'])
     print(i['node']['id'])
 DataBaseIdOffDuplicate = list(OrderedDict.fromkeys(dataBaseId))
 return DataBaseIdOffDuplicate




def AfterInitial():
  ListInit = []
  query = f"""
  {{
    allCards(pipeId:{pipe_id},first: 50){{
      pageInfo {{
        hasNextPage
        endCursor
      }}
      edges {{
        node {{
          id
        }}
      }}
    }}
  }}
  """
  
  response = requests.post(url, headers=headers, json={"query": query})
  data = response.json()['data']['allCards']['edges']
  for i in data:
     ListInit.append(i['node']['id'])
     print(i['node']['id'])
  return ListInit
  


vikra = []  
def Analisador_ID_CARD(idCard):
 query = f"""
{{
  card(id: "{idCard}") {{
    title
    created_at
    fields {{
      name
      value
      
       }}
    
    current_phase {{
      id
      name
    }}
    }}
  }} """
  
 response = requests.post(url, headers=headers, json={"query": query})
 datat = response.json()['data']['card']
 print(datat)
 vikra.append(datat)
 return vikra
      
"""  
lista_id_inicial_pagina = AfterInitial()
lista_afters = After()
listas_de_ids_parcial = CapturedID(lista_afters)

List_ID = lista_id_inicial_pagina + listas_de_ids_parcial
print(len(List_ID))

"""


vikra2 = Analisador_ID_CARD('929205460')

print(len(vikra2))
print(vikra2[0]['fields'][3])


