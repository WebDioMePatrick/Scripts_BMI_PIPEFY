import requests
import json
import pandas as pd
from collections import OrderedDict

url = "https://api.pipefy.com/graphql"
token = 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJQaXBlZnkiLCJpYXQiOjE3MTc2OTQzNjksImp0aSI6IjA1ZmM3ZWVmLTVmNTYtNGQwOC04ODlkLTQxYTE2MzRmMTJjZCIsInN1YiI6MzA0MTgzNzk4LCJ1c2VyIjp7ImlkIjozMDQxODM3OTgsImVtYWlsIjoicHJvamV0b2JhaGlhbWVpQGdtYWlsLmNvbSJ9fQ.y1QnXR1u9wTtaxWs6vIjFklc0BxMisnRmxuFnwkw3p3v0QYSdmfTsPDbzrBZI2SZXBleILEVjh-ev5gBGUrQTQ'



headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
pipe_id = "303861827"
dataBaseId = []


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
 print('Carregando AFTERS')
 while controlador['pageInfo']['hasNextPage'] == True:
     databaseAA.append(controlador['pageInfo']['endCursor'])
     
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
 print('CONCLUIDO = ',len(databaseAA),' Carregados') 
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
  print("CARREGANDO IDS ...")
  for i in data:
     dataBaseId.append(i['node']['id'])
 DataBaseIdOffDuplicate = list(OrderedDict.fromkeys(dataBaseId))
 print("IDS CARREGADOS!!!")
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
      name
    }}
    }}
  }} """
  
 response = requests.post(url, headers=headers, json={"query": query})
 datat = response.json()['data']['card']

 if datat['current_phase']['name'] == 'Concluído': #captured card concluido
   vikra.append(datat)
   return vikra # se condição for satisfeito sera retornada
 else:
   return False #para remover em um possivel tratamento
       
 
      
