# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

"Constants"

"Latent Heat of Vaporization for Water"
L_w = 40.68
w_0 = 657959000
w_a = 11.99
T_w = 4982.85
number = 19
R_load = 135

def g_s(K_matrix,T_a,T_e):
    return (R_load+K_matrix*(T_a-T_e))/(L_w*(w_0*np.exp(-T_w/(T_e+273))-w_a))



import csv
with open('KMatrix_23C_1Amp.csv','r') as K_matrixcsvfile, open('AT_'+str(number)+'_'+str(w_a)+'.csv','r', encoding='utf-8-sig') as T_acsvfile, open('LT_'+str(number)+'.csv','r', encoding='utf-8-sig') as T_ecsvfile, open('conductance_turmeric_'+str(number)+'.csv','w') as outputfile:
    K_matrix = csv.reader(K_matrixcsvfile, delimiter = ',', quotechar='\n')
    T_a = csv.reader(T_acsvfile, delimiter = ',', quotechar='\n')
    T_e = csv.reader(T_ecsvfile, delimiter = ',', quotechar='\n')
    while True:
        K_matrixrow=next(K_matrix)
        T_arow=next(T_a)
        T_erow=next(T_e)
        rowlength=len(T_arow)
        rowindex=0
        while rowindex < rowlength:
            K_matrixvalue=float(K_matrixrow[rowindex])
            T_avalue=float(T_arow[rowindex])
            T_evalue=float(T_erow[rowindex])
            conductance=g_s(K_matrixvalue,T_avalue,T_evalue)
            outputfile.write(str(conductance))
            rowindex+=1
            if rowindex < rowlength:
                outputfile.write(',')
        outputfile.write('\n') 

#with open('KMatrix_23C_1Amp.csv','r') as K_matrixcsvfile, open('AirTempMatrix_1.csv','r', encoding='utf-8-sig') as T_acsvfile, open('LeafTempMatrix_1.csv','r', encoding='utf-8-sig') as T_ecsvfile: