import numpy


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

    LData = numpy.reshape(numpy.array(range(0,3*NumLoad)),(NumLoad,3))
    for i in range(NumLoad):
        DataLoad=list(map(int,input().split()))
        for j in range(3):
            LData[i][j]=DataLoad[j]
            #print("La fila ",i," Columna ",j," Contiene el valor ",LData[i][j])
    
    print(LData)
    TotPot = 0
    TotEng = 0
    for i in range(NumLoad):
        TotPot = TotPot + LData[i,0]
        TotEng = TotEng + LData[i,0]*LData[i,1]
        print("\n")
        print(TotPot)
        print("\n")
        print(TotEng)
        print("\n")
        print(LData[i,0]," ",LData[i,1])
        print("\n")



def CompsumptionOnG(PlcDat):
    return 2