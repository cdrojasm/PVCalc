def LoopCompsumptionBased(PlcDat):
    print("Seleccione el tipo de sistema \n 1. On-Grid\n 2. Off-Grid")
    Dat=input()
    flag = 0
    while ( flag == 0):
        if Dat == 1:
            CompsumptionOffG(PlcDat)
            flag = 1
        elif Dat == 2:
            CompsumptionOnG(PlcDat)
            flag = 1
        else:
            print("No se selecciono una opcion disponible")


def CompsumptionOffG(PlcDat):
    
    return 1
def CompsumptionOnG(PlcDat):
    return 2