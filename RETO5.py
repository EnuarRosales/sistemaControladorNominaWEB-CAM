

from ast import With
import csv, json
import math
from operator import index
from statistics import mean

def clima():
#importamos el archivo csv de tesla y lo leemos
    with open('C:/Users/User/Downloads/archivo/data.csv','r',newline='') as archivo:
        archivo_entrada = csv.reader(archivo, delimiter=',')

        #se crea la ruta donde se va aguardar el nuevo archivo ya tabulado 
        with open ('C:/Users/User/Downloads/archivo/data_nuevo.csv','w',newline='') as archivo:
            archivo_salida = csv.writer(archivo, delimiter='\t')            
            #creaamos encabezado 
            archivo_salida.writerow(['id','location','temperature','pressure','above_avg_temp','above_avg_pres'])  

            next (archivo_entrada)            
                    

            lista_temperatura1= []
            lista_temperatura2= []
            lista_temperatura3= []
            lista_temperatura4= []
            lista_temperatura5= []

            lista_presion_admosferoca1= []
            lista_presion_admosferoca2= []
            lista_presion_admosferoca3= []
            lista_presion_admosferoca4= []
            lista_presion_admosferoca5= []

             


            for fila in archivo_entrada:
                
                id = fila[0]
                locacio = fila[1]
                temperatura=float(fila[2])
                presion_admosferica = float(fila[3])

                if (locacio=="1"):
                    lista_temperatura1.append(temperatura)
                    lista_presion_admosferoca1.append(presion_admosferica)
                elif(locacio=="2"):
                    lista_temperatura2.append(temperatura)
                    lista_presion_admosferoca2.append(presion_admosferica)

                elif(locacio=="3"):
                    lista_temperatura3.append(temperatura)
                    lista_presion_admosferoca3.append(presion_admosferica)

                elif(locacio=="4"):
                    lista_temperatura4.append(temperatura)
                    lista_presion_admosferoca4.append(presion_admosferica)

                elif(locacio=="5"):
                    lista_temperatura5.append(temperatura)
                    lista_presion_admosferoca5.append(presion_admosferica)

                archivo_salida.writerow([id,locacio,temperatura,presion_admosferica])                   
                

            print(id) 

                    
            promedio_temperatura1=round(sum(lista_temperatura1)/len(lista_temperatura1),1)
            promedio_temperatura2=round(sum(lista_temperatura2)/len(lista_temperatura2),1)
            promedio_temperatura3=round(sum(lista_temperatura3)/len(lista_temperatura3),1)
            promedio_temperatura4=round(sum(lista_temperatura4)/len(lista_temperatura4),1)
            promedio_temperatura5=round(sum(lista_temperatura5)/len(lista_temperatura5),1)

            promedio_presion_atmosferica1=round(sum(lista_presion_admosferoca1)/len(lista_presion_admosferoca1),1)
            promedio_presion_atmosferica2=round(sum(lista_presion_admosferoca2)/len(lista_presion_admosferoca2),1)
            promedio_presion_atmosferica3=round(sum(lista_presion_admosferoca3)/len(lista_presion_admosferoca3),1)
            promedio_presion_atmosferica4=round(sum(lista_presion_admosferoca4)/len(lista_presion_admosferoca4),1)
            promedio_presion_atmosferica5=round(sum(lista_presion_admosferoca5)/len(lista_presion_admosferoca5),1)

                                                            



            


            datos = {}
            datos ["1"] = [promedio_temperatura1,promedio_presion_atmosferica1]
            datos ["2"] = [promedio_temperatura2,promedio_presion_atmosferica2]
            datos ["3"] = [promedio_temperatura3,promedio_presion_atmosferica3]
            datos ["4"] = [promedio_temperatura4,promedio_presion_atmosferica4]
            datos ["5"] = [promedio_temperatura5,promedio_presion_atmosferica5]
            


            with open ('C:/Users/User/Downloads/archivo/datos.json','w',newline='') as archivo:
                json.dump(datos,archivo)    
                    
            

clima()   












    




















            