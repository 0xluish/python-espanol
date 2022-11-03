año = int(input("\nIngrese el año del que desea saber si es bisiesto o no: "))
def añoBisiesto(año):
    if(año%4 != 0 or año%400 != 0):
        print(f"El año {año} no es bisiesto\n")
    elif(año%4 == 0 and año%100 == 0 and año%400 == 0):
        print(f"El año {año} sí es bisiesto\n")
añoBisiesto(año)