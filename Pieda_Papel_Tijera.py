import random


print("-------------------------------------------------")
print("------------PIEDRA, PAPEL O TIJERA---------------")
print("-------------------------------------------------")





print("1 -----------> Piedra: ")
print("2------------> Papel: ")
print("3 -----------> TIjera: ")



opcion = int(input("Seleccione la opcion con la quiera jugar: "))



if(opcion==1) :
    Rta = "Piedra"
elif(opcion==2):
    Rta = "Papel"
elif(opcion==3):
    Rta = "Tijera"
else:
    opcion>3 and opcion<0
    Rta = "La opcion que ha escogido no es valida"

  
Computadora = random

n = random.randint(1,3)
if(n==1) :
    n = "Piedra"
elif(n==2):
    n = "Papel"
elif(n==3):
    n = "Tijera"





       
print("usted ha escogido la opcion: " + str(Rta) ) 
print("La computadora ha escogido : " + str(n))



