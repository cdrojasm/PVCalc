from numpy import array
from numpy.lib.stride_tricks import as_strided
from numpy.lib.type_check import _asfarray_dispatcher
from os import system
from Calc_CompBased import *

print("Indique las condiciones ambientales del sitio de instalación:\n")
print("HSP (kWh/m2):")
HorSP = float(input())
print("\n")

print("Temperatura (kWh/m2):")
Temp = float(input())
print("\n")

PlaceDat = array([HorSP, Temp])

print("Seleccione el tipo de programa:\n")
print("1. Calculo basado en el consumo\n")
print("2. Calculo basado en el área disponible\n")
print("3. Calculo basado en presupuesto disponible\n")

CalcTyp=int(input())
clear = lambda: system('clear')

Select=0

if CalcTyp==1:
    LoopCompsumptionBased(PlaceDat)
    Select = 1
elif CalcTyp == 2:
    Select = 2
elif CalcTyp == 3:
    Select = 3
else:
    print("Opción invalida \n")
