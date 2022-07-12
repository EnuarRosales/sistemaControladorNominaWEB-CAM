import csv, json
from ctypes.wintypes import PINT


leyendoJSON = open('C:/Users/User/Desktop/sistemaControladorNominaWEB-CAM/pruebaEstudio.json','r')
content  = leyendoJSON.read()
dict_entities = json.loads(content)

lista_cedula =[]
lista_nombre = []
lista_modalidad=[]
lista_nickname =[]
lista_tokenChaturbate =[]
lista_valor_dolares=[]
lista_nomina =[]
lista_porcentaje=[]
lista_dolares_a_pesos =[]

with open('C:/Users/User/Desktop/sistemaControladorNominaWEB-CAM/baseDatos.csv','r',newline='') as archivo:
        archivo_entrada = csv.reader(archivo, delimiter=';')         
        
            #print(chaturbate)
        with open ('C:/Users/User/Desktop/sistemaControladorNominaWEB-CAM/nomina.csv','w',newline='') as archivo:
            archivo_salida = csv.writer(archivo, delimiter=';')            
            #creaamos encabezado 
            archivo_salida.writerow(['CEDULA','NOMBRE','MODALIDAD','NICKNAME','TOKEN_CHATURBATE','TOKEN_A_DOLAR','PORCENTAJE','DOLAR_A_PESOS'])

            next (archivo_entrada)

            for fila in archivo_entrada:

                cedula = fila[0]
                nombre = fila[1]
                modalidad=fila[2]
                chaturbate =fila[3]

                lista_cedula.append(cedula)
                lista_nombre.append(nombre)
                lista_modalidad.append(modalidad)
                lista_nickname.append(chaturbate) 
                
                if modalidad == "MONITOR"   or modalidad == "OFICIOS_VARIOS":
                    porcentaje = 100
                    lista_porcentaje.append(porcentaje)
                    
                elif modalidad == "SATELITE":
                    porcentaje = 80
                    lista_porcentaje.append(porcentaje)
                    
                elif modalidad == "ESTUDIO":
                    porcentaje = 60
                    lista_porcentaje.append(porcentaje)        
                                                                                                    
                for i in range(len(dict_entities['stats'][0]['rows'])):

                    if chaturbate == dict_entities['stats'][0]['rows'][i][0]: 

                        token = dict_entities['stats'][0]['rows'][i][1]
                        valorTokens = dict_entities['stats'][0]['rows'][i][2]                      

                        lista_tokenChaturbate.append(token)
                        lista_valor_dolares.append(valorTokens)                   
                                                        
            for i in lista_valor_dolares:
                    trmDolar = 3600
                    total= trmDolar*i
                    lista_dolares_a_pesos.append(total)     
                
            for j in range(len(lista_cedula)):
                lista_nomina.append(lista_cedula[j])                
                lista_nomina.append(lista_nombre[j])
                lista_nomina.append(lista_modalidad[j])
                lista_nomina.append(lista_nickname[j])
                lista_nomina.append(lista_tokenChaturbate[j])
                lista_nomina.append(lista_valor_dolares[j])
                           
             
                archivo_salida.writerow([lista_cedula[j],lista_nombre[j],lista_modalidad[j],lista_nickname[j],
                                         lista_tokenChaturbate[j],lista_valor_dolares[j],lista_porcentaje[j],
                                         lista_dolares_a_pesos[j]])
            
            
            
        print("hola pinchao")
        
      
        
            
            
            
            

     
          





            #print(lista_tokenChaturbate)
            




                    







                

                #print(chaturbate)






