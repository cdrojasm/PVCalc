def LoopCompsumptionBased(PlcDat): 
    flag = 0
    while flag == 0:
        print("Seleccione el tipo de sistema \n 1. Off-Grid\n 2. On-Grid")
        Dat=int(input())
        if Dat == 1:
            CompsumptionOffG(PlcDat)
            flag = 1
        elif Dat == 2:
            CompsumptionOnG(PlcDat)
            flag = 1
        else:
            print("No se selecciono una opcion disponible")


def CompsumptionOffG(PlcDat):
    print("Inserte la cantidad de cargas:\n")
    CLU=0
    while(CLU==0):
        NumLoad=int(input())
        if(NumLoad>1):
            CLU=1
        else:
            print("\n Numero de cargas debe ser un entero positivo")

    print("Inserte la Potencia instantanea, horas de uso y tensión de operación")
    print("\n Todo debe estar separado por comas e ingresarse como enteros")
    print("\n")

    for i in range(NumLoad):
        DataLoad=list(map(int,input().split()))
        print(DataLoad)
    return 1
def CompsumptionOnG(PlcDat):
    return 2