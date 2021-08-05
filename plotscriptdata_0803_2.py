# Written by Giovanna Cottin (gfcottin@gmail.com)
# Editted by Joseph Mina (jmina@caltech.edu)
import os,sys
import numpy as np
import math

mX    = np.linspace(250, 3000, 100) # values of heavy Higgs mass to scan through
lam   = np.linspace(0.22, 0.22, 1) # values of lambda Hdd to scan through

madgraph_path = '/storage/af/user/jmina/LLP-Reinterpretation/MG5_aMC_v2_7_3'
output_dir = '/storage/af/user/jmina/Plots/Daniel_Plots/Fig5/Plot3_Data_0803_2'
#if not os.path.isdir(output_dir+"/m"+str(mass)+"_l"+str(lamv)):os.makedirs(output_dir+"/m"+str(mass)+"_l"+str(lamv))
if not os.path.isdir(output_dir):os.makedirs(output_dir)
#if not os.path.isdir(output_dir+''):os.makedirs(output_dir+'HNL_mg5_GRID_tau')

for mass in mX:
    for lamv in lam:
	f = open(output_dir+"/m"+str(round(mass, 2))+"_l"+str(lamv),'w')
        f.write("import model /storage/af/user/jmina/LLP-Reinterpretation/madgraph_models/SFV_2HDM_uptype\n")
        f.write("define p = g u c d s u~ c~ d~ s~\n")
	f.write("define j = g u c d s u~ c~ d~ s~\n")
        f.write("define l+ = e+ mu+\n")
        f.write("define l- = e- mu-\n")
        f.write("define vl = ve vm vt\n")
        f.write("define vl~ = ve~ vm~ vt~\n")
	f.write("generate d d~ > h1 h1 NP=99\n")
	f.write("output "+output_dir+"/Plot3_Q_Data/m"+str(round(mass, 2))+"_l"+str(lamv)+"\n")
        f.write("launch\n")
        f.write("set nevents 1000\n")
        f.write("set use_syst False\n")
        f.write("set l2 0.0\n")
        f.write("set l3 0.0\n")
        f.write("set lR7 0.0\n")
        f.write("set cosbma 0.025\n")
        f.write("set xi 0.0\n")
        f.write("set mh1 125.0\n")
        f.write("set mh2 "+str(mass)+"\n")
        f.write("set mh3 "+str(mass)+"\n")
        f.write("set mhc "+str(mass)+"\n")
        f.write("set GDR1x1 "+str(lamv)+"\n")
        f.write("set GDR2x2 0.0\n")
        f.write("set GDR3x3 0.0\n")
        f.write("set Wh2 Auto\n")
        f.write("set Wh3 Auto\n")
        f.write("set Whc Auto\n")
        f.close()
