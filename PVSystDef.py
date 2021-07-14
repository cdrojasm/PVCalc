#
# This Function Extracts Database of PV System Components
#
#
# Function develop the extraction of data and store it in 
# an array structure according to component type.
# Component types involves Inverters, Microinverters, 
# PV modules, Wires, Solar DC controllers, etc.
# 
# first Version Carlos David Rojas Montano, EXIA
# 

import xlrd
PyPath = "D:\USUARIO\Documents\PythonProy\DBPV.xlsm"
Excel_WB = xlrd.open_workbook(PyPath)
Excel_WB = xlrd.open_workbook(PyPath)

