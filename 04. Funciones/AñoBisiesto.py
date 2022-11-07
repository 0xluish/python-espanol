año = int(input("\nIngrese el año del que desea saber si es bisiesto o no: "))
def añoBisiesto(año):
    if(año%4 == 0):
        if(año%100 != 0 or año%400 == 0):
            print(f'El año {año} sí es bisiesto')
        else:
            print(f'El año {año} no es bisiesto')          
    else:   
        print(f'El año {año} no es bisiesto')
añoBisiesto(año)