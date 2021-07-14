from numpy import array
from numpy.lib.stride_tricks import as_strided
from numpy.lib.type_check import _asfarray_dispatcher
from os import system

print("Indique las condiciones ambientales del sitio de instalación:\n")
print("HSP (kWh/m2):")
HorSP = float(input())
print("\n")

print("Temperatura (kWh/m2):")
Temp = float(input())
print("\n")

print("Seleccione el tipo de sistema, \n 1 para Off-Grid \ 2 para On-Grid\n")
SistTyp = int(input())

PlaceDat = array([HorSP, Temp])

print("Seleccione el tipo de programa:\n")
print("1. Calculo basado en el consumo\n")
print("2. Calculo basado en el área disponible\n")
print("3. Calculo basado en presupuesto disponible\n")

CalcTyp=int(input())
clear = lambda: system('clear')

if CalcTyp==1:
    Calc_CompBased(PlaceDat)
elif CalcTyp == 2:

elif CalcTyp == 3:

else:
    print("Opción invalida \n")
