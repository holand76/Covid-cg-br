import ast
import time


with open ('covid.json','r') as file:
    a = file.readlines()


tamanho = len(a)
print(type(a))
print('tipo')

lista_contendoOsDicionarios = []

for index in range(tamanho):
    #print(a[index])
    if a[index] in ('][','[',']',']\n','][\n'):
        continue
    

    try:
    
        transforma_paradict = ast.literal_eval(a[index])
        #print(transforma_paradict,"\n")
#        time.sleep(1) #pra debug
        
    except:
        continue

    for key in transforma_paradict:
        lista_auxiliar = [] #para editar as strings

        for linha in transforma_paradict[key]: 

            string = linha

            c = string.replace('<h1 class="titulo-recebidas-aplicadas">','')
            c = c.replace('</h1>','')
            c = c.replace('<b>','')
            c = c.replace('</b>','')
            c = c.replace('<h2 class="valor-recebidas-aplicadas">','')
            c = c.replace('</h2>','')
            
            lista_auxiliar.append(c)
#           print(c,'limpo')
        
        transforma_paradict[key] = [lista_auxiliar]
        #print('resultado final ')
        #print(transforma_paradict)
        #print(type(transforma_paradict))
    #    for i in transforma_paradict:
            #print(i)
    #time.sleep(1)
    print(transforma_paradict)
    lista_contendoOsDicionarios.append(transforma_paradict)

with open('dados.py','w') as arquivo:
    string = str(lista_contendoOsDicionarios) #so da pra escrevers strings nos arquivos
    string = 'listaCOVID = '+string 
    arquivo.write(string)

#for i in a:
 #   if a in ('][\n','[\n'):
  #      continue 
   # c = i.replace('<h1 class="titulo-recebidas-aplicadas">','')
   # c = c.replace('</h1>','')
   # c = c.replace('<b>','')
   # c = c.replace('</b>','')
   # print(c)